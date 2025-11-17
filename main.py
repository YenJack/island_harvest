# main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models, schemas, crud
from auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from datetime import timedelta
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

Base.metadata.create_all(bind=engine)
app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# token endpoint
@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username, "user_id": user.id}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

# get current user
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

# register user
@app.post("/users", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# Protected example: get me
@app.get("/me", response_model=schemas.User)
def read_me(current_user = Depends(get_current_user)):
    return current_user

# sensor CRUD (protected)
@app.post("/sensors", response_model=schemas.Sensor)
def create_sensor(sensor: schemas.SensorCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.create_sensor(db, sensor)

@app.get("/sensors", response_model=list[schemas.Sensor])
def read_sensors(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.get_sensors(db)

@app.get("/sensors/{id}", response_model=schemas.Sensor)
def read_sensor(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    s = crud.get_sensor(db, id)
    if not s:
        raise HTTPException(status_code=404, detail="Not found")
    return s

@app.put("/sensors/{id}", response_model=schemas.Sensor)
def put_sensor(id: int, sensor: schemas.SensorCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    s = crud.update_sensor(db, id, sensor.dict())
    return s

@app.delete("/sensors/{id}")
def del_sensor(id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    crud.delete_sensor(db, id)
    return {"ok": True}

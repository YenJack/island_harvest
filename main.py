from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, User, Farm, Device, Sensor
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------------------------------
# User CRUD
# ------------------------------
@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/users/{id}", response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == id).first()

@app.put("/users/{id}", response_model=schemas.User)
def update_user(id: int, new_data: schemas.UserCreate, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == id).update(new_data.dict())
    db.commit()
    return db.query(User).filter(User.id == id).first()

@app.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == id).delete()
    db.commit()
    return {"status": "ok"}


# ------------------------------
# Farm CRUD
# ------------------------------
@app.post("/farms", response_model=schemas.Farm)
def create_farm(farm: schemas.FarmCreate, db: Session = Depends(get_db)):
    db_farm = Farm(**farm.dict())
    db.add(db_farm)
    db.commit()
    db.refresh(db_farm)
    return db_farm

@app.get("/farms", response_model=list[schemas.Farm])
def get_all_farms(db: Session = Depends(get_db)):
    return db.query(Farm).order_by(Farm.id.desc()).all()

@app.get("/farms/{id}", response_model=schemas.Farm)
def get_farm(id: int, db: Session = Depends(get_db)):
    return db.query(Farm).filter(Farm.id == id).first()

@app.put("/farms/{id}", response_model=schemas.Farm)
def update_farm(id: int, farm: schemas.FarmCreate, db: Session = Depends(get_db)):
    db.query(Farm).filter(Farm.id == id).update(farm.dict())
    db.commit()
    return db.query(Farm).filter(Farm.id == id).first()

@app.delete("/farms/{id}")
def delete_farm(id: int, db: Session = Depends(get_db)):
    db.query(Farm).filter(Farm.id == id).delete()
    db.commit()
    return {"status": "ok"}


# ------------------------------
# Device CRUD
# ------------------------------
@app.post("/devices", response_model=schemas.Device)
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    db_device = Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

@app.get("/devices", response_model=list[schemas.Device])
def get_all_devices(db: Session = Depends(get_db)):
    return db.query(Device).order_by(Device.id.desc()).all()

@app.get("/devices/{id}", response_model=schemas.Device)
def get_device(id: int, db: Session = Depends(get_db)):
    return db.query(Device).filter(Device.id == id).first()

@app.put("/devices/{id}", response_model=schemas.Device)
def update_device(id: int, device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    db.query(Device).filter(Device.id == id).update(device.dict())
    db.commit()
    return db.query(Device).filter(Device.id == id).first()

@app.delete("/devices/{id}")
def delete_device(id: int, db: Session = Depends(get_db)):
    db.query(Device).filter(Device.id == id).delete()
    db.commit()
    return {"status": "ok"}



# ------------------------------
# Sensor CRUD
# ------------------------------
@app.post("/sensors", response_model=schemas.Sensor)
def create_sensor(sensor: schemas.SensorCreate, db: Session = Depends(get_db)):
    db_sensor = Sensor(**sensor.dict())
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

@app.get("/sensors", response_model=list[schemas.Sensor])
def get_all_sensors(db: Session = Depends(get_db)):
    return db.query(Sensor).order_by(Sensor.id.desc()).all()

@app.get("/sensors/{id}", response_model=schemas.Sensor)
def get_sensor(id: int, db: Session = Depends(get_db)):
    return db.query(Sensor).filter(Sensor.id == id).first()

@app.put("/sensors/{id}", response_model=schemas.Sensor)
def update_sensor(id: int, sensor: schemas.SensorCreate, db: Session = Depends(get_db)):
    db.query(Sensor).filter(Sensor.id == id).update(sensor.dict())
    db.commit()
    return db.query(Sensor).filter(Sensor.id == id).first()

@app.delete("/sensors/{id}")
def delete_sensor(id: int, db: Session = Depends(get_db)):
    db.query(Sensor).filter(Sensor.id == id).delete()
    db.commit()
    return {"status": "ok"}

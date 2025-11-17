# crud.py
from sqlalchemy.orm import Session
import models, schemas
from auth import get_password_hash, verify_password

# user
def create_user(db: Session, user: schemas.UserCreate):
    hashed = get_password_hash(user.password)
    db_user = models.User(username=user.username, userPassword=hashed, emailAddress=user.emailAddress, fullName=user.fullName)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    u = db.query(models.User).filter(models.User.username == username).first()
    if not u: return None
    if not verify_password(password, u.userPassword):
        return None
    return u

# sensor
def create_sensor(db: Session, sensor: schemas.SensorCreate):
    s = models.Sensor(**sensor.dict())
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

def get_sensors(db: Session):
    return db.query(models.Sensor).order_by(models.Sensor.id.desc()).all()

def get_sensor(db: Session, id: int):
    return db.query(models.Sensor).filter(models.Sensor.id == id).first()

def update_sensor(db: Session, id: int, data: dict):
    db.query(models.Sensor).filter(models.Sensor.id == id).update(data)
    db.commit()
    return db.query(models.Sensor).filter(models.Sensor.id == id).first()

def delete_sensor(db: Session, id: int):
    db.query(models.Sensor).filter(models.Sensor.id == id).delete()
    db.commit()
    return True

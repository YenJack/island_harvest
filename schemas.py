# schemas.py
from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    fullName: Optional[str] = None
    phoneNumber: Optional[str] = None
    registrationDate: Optional[str] = None
    lastLoginDate: Optional[str] = None
    emailAddress: Optional[str] = None
    userId: Optional[str] = None
    username: Optional[str] = None
    deviceList: Optional[str] = None
    farmList: Optional[str] = None
    sharedDevices: Optional[str] = None
    sharedFarms: Optional[str] = None

class UserCreate(UserBase):
    username: str
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

# Sensor
class SensorBase(BaseModel):
    sensorCategory: str
    sensorProductName: str
    sensorSerialNumber: str
    name: Optional[str] = None

class SensorCreate(SensorBase):
    pass

class Sensor(SensorBase):
    id: int
    class Config:
        orm_mode = True

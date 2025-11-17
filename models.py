# models.py
from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    fullName = Column(String, nullable=True)
    phoneNumber = Column(String, nullable=True)
    registrationDate = Column(String, nullable=True)
    lastLoginDate = Column(String, nullable=True)
    emailAddress = Column(String, nullable=True, unique=True)
    userId = Column(String, nullable=True)
    username = Column(String, nullable=True, unique=True)
    userPassword = Column(String, nullable=True)  # hashed
    deviceList = Column(String, nullable=True)
    farmList = Column(String, nullable=True)
    sharedDevices = Column(String, nullable=True)
    sharedFarms = Column(String, nullable=True)

class Farm(Base):
    __tablename__ = "farms"
    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    farmName = Column(String, nullable=True)
    farmNumber = Column(String, nullable=True)
    deviceArray = Column(String, nullable=True)
    photoDirName = Column(String, nullable=True)
    farmerName = Column(String, nullable=True)
    farmType = Column(String, nullable=True)
    cropName = Column(String, nullable=True)
    farmAddress = Column(String, nullable=True)
    isDeleted = Column(String, nullable=True)
    coordinates = Column(String, nullable=True)
    boundary = Column(String, nullable=True)
    cultivationStatus = Column(String, nullable=True)
    lastModifiedDate = Column(String, nullable=True)
    landArea = Column(String, nullable=True)
    userId = Column(String, nullable=True)
    sharedFarmsWith = Column(String, nullable=True)

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    scene = Column(String, nullable=False)
    name = Column(String, nullable=False)
    iconPath = Column(String, nullable=False)
    sensors = Column(String, nullable=False)
    isControlType = Column(Integer, nullable=False)
    productId = Column(String, nullable=True)
    serialNumber = Column(String, nullable=True)
    sensorList = Column(String, nullable=True)
    farmNumber = Column(String, nullable=True)
    sharedDevicesWith = Column(String, nullable=True)
    automationSetting = Column(String, nullable=True)
    devicePassword = Column(String, nullable=True)
    factoryResetStatus = Column(String, nullable=True)

class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    sensorCategory = Column(String, nullable=False)
    sensorProductName = Column(String, nullable=False)
    sensorSerialNumber = Column(String, nullable=False)
    name = Column(String, nullable=True)

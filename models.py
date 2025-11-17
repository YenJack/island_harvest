from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullName = Column(String)
    phoneNumber = Column(String)
    registrationDate = Column(String)
    lastLoginDate = Column(String)
    emailAddress = Column(String)
    userId = Column(String)
    username = Column(String)
    userPassword = Column(String)
    deviceList = Column(String)
    farmList = Column(String)
    sharedDevices = Column(String)
    sharedFarms = Column(String)


class Farm(Base):
    __tablename__ = "farms"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float)
    lon = Column(Float)
    farmName = Column(String)
    farmNumber = Column(String)
    deviceArray = Column(String)
    photoDirName = Column(String)
    farmerName = Column(String)
    farmType = Column(String)
    cropName = Column(String)
    farmAddress = Column(String)
    isDeleted = Column(String)
    coordinates = Column(String)
    boundary = Column(String)
    cultivationStatus = Column(String)
    lastModifiedDate = Column(String)
    landArea = Column(String)
    userId = Column(String)
    sharedFarmsWith = Column(String)


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    scene = Column(String)
    name = Column(String)
    iconPath = Column(String)
    sensors = Column(String)
    isControlType = Column(Integer)
    productId = Column(String)
    serialNumber = Column(String)
    sensorList = Column(String)
    farmNumber = Column(String)
    sharedDevicesWith = Column(String)
    automationSetting = Column(String)
    devicePassword = Column(String)
    factoryResetStatus = Column(String)


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    sensorCategory = Column(String)
    sensorProductName = Column(String)
    sensorSerialNumber = Column(String)
    name = Column(String)

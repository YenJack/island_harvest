from pydantic import BaseModel

# ------------------------------
# User
# ------------------------------
class UserBase(BaseModel):
    fullName: str | None = None
    phoneNumber: str | None = None
    registrationDate: str | None = None
    lastLoginDate: str | None = None
    emailAddress: str | None = None
    userId: str | None = None
    username: str | None = None
    userPassword: str | None = None
    deviceList: str | None = None
    farmList: str | None = None
    sharedDevices: str | None = None
    sharedFarms: str | None = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode = True


# ------------------------------
# Farm
# ------------------------------
class FarmBase(BaseModel):
    lat: float
    lon: float
    farmName: str | None = None
    farmNumber: str | None = None
    deviceArray: str | None = None
    photoDirName: str | None = None
    farmerName: str | None = None
    farmType: str | None = None
    cropName: str | None = None
    farmAddress: str | None = None
    isDeleted: str | None = None
    coordinates: str | None = None
    boundary: str | None = None
    cultivationStatus: str | None = None
    lastModifiedDate: str | None = None
    landArea: str | None = None
    userId: str | None = None
    sharedFarmsWith: str | None = None

class FarmCreate(FarmBase):
    pass

class Farm(FarmBase):
    id: int
    class Config:
        orm_mode = True


# ------------------------------
# Device
# ------------------------------
class DeviceBase(BaseModel):
    scene: str
    name: str
    iconPath: str
    sensors: str
    isControlType: int
    productId: str | None = None
    serialNumber: str | None = None
    sensorList: str | None = None
    farmNumber: str | None = None
    sharedDevicesWith: str | None = None
    automationSetting: str | None = None
    devicePassword: str | None = None
    factoryResetStatus: str | None = None

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int
    class Config:
        orm_mode = True


# ------------------------------
# Sensor
# ------------------------------
class SensorBase(BaseModel):
    sensorCategory: str
    sensorProductName: str
    sensorSerialNumber: str
    name: str | None = None

class SensorCreate(SensorBase):
    pass

class Sensor(SensorBase):
    id: int
    class Config:
        orm_mode = True

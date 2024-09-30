from pydantic import BaseModel, Field
from datetime import datetime

class SensorValue(BaseModel):
    device_id: str
    device_name: str
    sensor_no: int
    unit: str
    location: str
    latitude: float
    longitude: float
    type: str
    value: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class SensorValueUpdate(BaseModel):
    device_name: str
    sensor_no: int
    unit: str
    location: str
    latitude: float
    longitude: float
    type: str
    value: float
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class SensorDevice(BaseModel):
    device_number: str
    device_name: str
    board: str
    os: str
    manager_name: str

class SensorDeviceUpdate(BaseModel):
    device_name: str
    board: str
    os: str
    manager_name: str

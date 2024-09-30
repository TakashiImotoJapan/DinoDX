from typing import List
from bson import ObjectId
from app.models.sensor import SensorDevice, SensorDeviceUpdate
from motor.motor_asyncio import AsyncIOMotorClient

class DeviceService:
    def __init__(self, db):
        self.collection = db.sensor_devices

    async def create_device(self, device: SensorDevice):
        result = await self.collection.insert_one(device.dict())
        if result.inserted_id:
            return device
        return None

    async def list_devices(self) -> List[SensorDevice]:
        devices = await self.collection.find().to_list(100)
        return devices

    async def get_device(self, id: str) -> SensorDevice:
        device = await self.collection.find_one({"_id": ObjectId(id)})
        return device

    async def update_device(self, id: str, device_update: SensorDeviceUpdate):
        update_data = {k: v for k, v in device_update.dict().items() if v is not None}
        result = await self.collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.modified_count:
            return await self.get_device(id)
        return None

    async def delete_device(self, id: str):
        result = await self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

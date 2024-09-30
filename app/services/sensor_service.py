from typing import List
from bson import ObjectId
from app.models.sensor import SensorValue, SensorValueUpdate
from motor.motor_asyncio import AsyncIOMotorClient

class SensorService:
    def __init__(self, db):
        self.collection = db.sensor_values

    async def create_sensor_value(self, sensor_value: SensorValue):
        result = await self.collection.insert_one(sensor_value.dict())
        if result.inserted_id:
            return sensor_value
        return None

    async def list_sensor_values(self) -> List[SensorValue]:
        sensor_values = await self.collection.find().to_list(100)
        return sensor_values

    async def get_sensor_value(self, id: str) -> SensorValue:
        sensor_value = await self.collection.find_one({"_id": ObjectId(id)})
        return sensor_value

    async def update_sensor_value(self, id: str, sensor_value_update: SensorValueUpdate):
        update_data = {k: v for k, v in sensor_value_update.dict().items() if v is not None}
        result = await self.collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.modified_count:
            return await self.get_sensor_value(id)
        return None

    async def delete_sensor_value(self, id: str):
        result = await self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

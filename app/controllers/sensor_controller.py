from fastapi import HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from typing import List
from app.models.sensor import SensorValue, SensorValueUpdate
from app.services.sensor_service import SensorService
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

def get_sensor_service(request: Request):
    return SensorService(request.app.mongodb)

async def create_sensor_value_form(request: Request):
    return templates.TemplateResponse("create_sensor.html", {"request": request})

async def create_sensor_value(sensor_value: SensorValue, service: SensorService = Depends(get_sensor_service)):
    result = await service.create_sensor_value(sensor_value)
    if result:
        return result
    raise HTTPException(status_code=400, detail="Failed to insert sensor value")

async def list_sensor_values(service: SensorService = Depends(get_sensor_service)):
    return await service.list_sensor_values()

async def get_sensor_value(id: str, service: SensorService = Depends(get_sensor_service)):
    result = await service.get_sensor_value(id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Sensor value not found")

async def update_sensor_value(id: str, sensor_value_update: SensorValueUpdate, service: SensorService = Depends(get_sensor_service)):
    result = await service.update_sensor_value(id, sensor_value_update)
    if result:
        return result
    raise HTTPException(status_code=400, detail="Failed to update sensor value")

async def delete_sensor_value(id: str, service: SensorService = Depends(get_sensor_service)):
    result = await service.delete_sensor_value(id)
    if result:
        return {"message": "Sensor value deleted"}
    raise HTTPException(status_code=404, detail="Sensor value not found")

async def read_root(request: Request, service: SensorService = Depends(get_sensor_service)):
    sensor_values = await service.list_sensor_values()
    return templates.TemplateResponse("index.html", {"request": request, "sensor_values": sensor_values})


async def edit_sensor_value(request: Request, id: str, service: SensorService = Depends(get_sensor_service)):
    sensor_value = await service.get_sensor_value(id)
    return templates.TemplateResponse("edit.html", {"request": request, "sensor_value": sensor_value})

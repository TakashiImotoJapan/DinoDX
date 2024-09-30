from fastapi import HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from typing import List
from app.models.sensor import SensorDevice, SensorDeviceUpdate
from app.services.device_service import DeviceService
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

def get_device_service(request: Request):
    return DeviceService(request.app.mongodb)

async def create_device_form(request: Request):
    return templates.TemplateResponse("create_device.html", {"request": request})

async def create_device(device: SensorDevice, service: DeviceService = Depends(get_device_service)):
    result = await service.create_device(device)
    if result:
        return result
    raise HTTPException(status_code=400, detail="Failed to insert device")

async def list_devices(service: DeviceService = Depends(get_device_service)):
    return await service.list_devices()

async def get_device(id: str, service: DeviceService = Depends(get_device_service)):
    result = await service.get_device(id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Device not found")

async def update_device(id: str, device_update: SensorDeviceUpdate, service: DeviceService = Depends(get_device_service)):
    result = await service.update_device(id, device_update)
    if result:
        return result
    raise HTTPException(status_code=400, detail="Failed to update device")

async def delete_device(id: str, service: DeviceService = Depends(get_device_service)):
    result = await service.delete_device(id)
    if result:
        return {"message": "Device deleted"}
    raise HTTPException(status_code=404, detail="Device not found")

async def read_devices(request: Request, service: DeviceService = Depends(get_device_service)):
    devices = await service.list_devices()
    return templates.TemplateResponse("device_index.html", {"request": request, "devices": devices})

async def edit_device(request: Request, id: str, service: DeviceService = Depends(get_device_service)):
    device = await service.get_device(id)
    return templates.TemplateResponse("device_edit.html", {"request": request, "device": device})

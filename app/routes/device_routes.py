from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.controllers import device_controller

router = APIRouter()

router.get("/", response_class=HTMLResponse)(device_controller.read_devices)
router.get("/{id}/edit", response_class=HTMLResponse)(device_controller.edit_device)

router.get("/create", response_class=HTMLResponse)(device_controller.create_device_form)
router.post("/create", response_model=device_controller.SensorDevice)(device_controller.create_device)

router.get("/", response_model=list[device_controller.SensorDevice])(device_controller.list_devices)
router.get("/{id}", response_model=device_controller.SensorDevice)(device_controller.get_device)
router.put("/{id}", response_model=device_controller.SensorDevice)(device_controller.update_device)
router.delete("/{id}")(device_controller.delete_device)


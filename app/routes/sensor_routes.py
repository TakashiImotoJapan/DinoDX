from fastapi import APIRouter
from app.controllers import sensor_controller
from fastapi.responses import HTMLResponse

router = APIRouter()

router.get("/", response_class=HTMLResponse)(sensor_controller.read_root)
router.get("/{id}/edit", response_class=HTMLResponse)(sensor_controller.edit_sensor_value)
router.get("/create", response_class=HTMLResponse)(sensor_controller.create_sensor_value_form)

router.post("/", response_model=sensor_controller.SensorValue)(sensor_controller.create_sensor_value)
router.get("/", response_model=list[sensor_controller.SensorValue])(sensor_controller.list_sensor_values)
router.get("/{id}", response_model=sensor_controller.SensorValue)(sensor_controller.get_sensor_value)
router.put("/{id}", response_model=sensor_controller.SensorValue)(sensor_controller.update_sensor_value)
router.delete("/{id}")(sensor_controller.delete_sensor_value)


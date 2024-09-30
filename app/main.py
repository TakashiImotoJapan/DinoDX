from fastapi import FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorClient
from app.routes import sensor_routes, device_routes
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# MongoDBに接続
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.sensor_data
app.mongodb = db

# テンプレートの設定
templates = Jinja2Templates(directory="app/templates")

# ルーターの設定
app.include_router(sensor_routes.router, prefix="/sensor-values", tags=["sensor-values"])
app.include_router(device_routes.router, prefix="/devices", tags=["devices"])

# ルートエンドポイントを追加
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

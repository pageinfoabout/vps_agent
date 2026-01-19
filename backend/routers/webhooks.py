import sys
import json
from fastapi import Request, APIRouter

router = APIRouter(tags=["webhooks"])

@router.post("/webhooks/caller")
async def livekit_webhook(request: Request):
    # ✅ МАКСИМАЛЬНАЯ ОТЛАДКА
    print("🔥 WEBHOOK HIT v1!", flush=True)
    sys.stdout.flush()
    
    body = await request.body()
    print(f"📦 Body: {body.decode()}", flush=True)
    
    auth_header = request.headers.get("Authorization")
    print(f"🔑 Auth: {auth_header}", flush=True)
    
    # Простой парсинг
    data = json.loads(body)
    print(f"📡 EVENT: {data.get('event')}", flush=True)
    
    return {"status": "ok"}

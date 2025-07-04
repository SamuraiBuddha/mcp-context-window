from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.post("/remaining")
async def remaining(payload: dict):
    msgs  = payload["messages"]
    model = payload.get("model", MODEL)
    used  = tokens_used(msgs, model)
    return {
        "model": model,
        "max_context": MAX_CONTEXT,
        "used": used,
        "remaining": max(MAX_CONTEXT - used, 0),
        "percent_full": round(used / MAX_CONTEXT * 100, 2)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8008)

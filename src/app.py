"""

"""

from fastapi import FastAPI

api = FastAPI()

@api.get("/healthz")
async def health():
    return "healthy"
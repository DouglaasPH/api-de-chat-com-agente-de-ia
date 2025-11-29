from fastapi import FastAPI
from api.routers.math import router as math_router


app = FastAPI()


app.include_router(math_router)
from fastapi import FastAPI
from config.router import routes

app = FastAPI()
app.include_router(routes)
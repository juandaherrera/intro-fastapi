import os

import uvicorn

from config.database import Base, engine
from fastapi import FastAPI
from middlewares.error_handler import ErrorHandler
from routers import delete, get, post, put

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Aprendiendo FastApi',
    description='Una API solo por diversión',
    version='0.2.0',
)

app.add_middleware(ErrorHandler)


app.include_router(get.router)
app.include_router(post.router)
app.include_router(put.router)
app.include_router(delete.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

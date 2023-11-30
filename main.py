from fastapi import FastAPI
from paths import delete, get, post, put

app = FastAPI(
    title='Aprendiendo FastApi',
    description='Una API solo por diversión',
    version='0.1.0',
)

app.include_router(get.router)
app.include_router(post.router)
app.include_router(put.router)
app.include_router(delete.router)

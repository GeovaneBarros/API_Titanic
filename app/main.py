import uvicorn
from fastapi import FastAPI

from routers import predict_router

app = FastAPI(
    title="Titanic",
    version='0.0.1'
)

app.include_router(predict_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)

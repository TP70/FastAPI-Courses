import uvicorn as uvicorn
from fastapi import FastAPI
from views import routers

app = FastAPI()


def configure():
    app.include_router(routers.router)


configure()
if __name__ == '__main__':
    uvicorn.run(app, debug=True)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import userRouter
from model.User import Base
import database.database as database

app = FastAPI()
app.include_router(router=userRouter)
Base.metadata.create_all(database.engine)


# Configuración de CORS para permitir solicitudes desde cualquier origen (puede ajustar esto para limitar los orígenes permitidos)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app)
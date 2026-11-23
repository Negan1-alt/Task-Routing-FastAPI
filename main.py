from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from task_routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["GET","POST","PUT","PATCH","DELETE"],
    allow_origins=["http://localhost:5173"],
    allow_headers=["*"]
)

app.include_router(router)

@app.get("/")
def Hello():
    return {"message":"Hello world"}

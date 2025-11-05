from fastapi import FastAPI
from accounts.routers import account_router

app = FastAPI()

app.include_router(account_router.router)

@app.get('/')
def index() -> str:
    return 'Seja bem-vindo(a)'

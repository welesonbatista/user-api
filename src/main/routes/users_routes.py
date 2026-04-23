from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_router = APIRouter(tags=["Usuários"])

@users_router.post("/users")
async def criar_usuario():
    return JSONResponse(content={"message": "Usuário criado com sucesso"}, status_code=201)

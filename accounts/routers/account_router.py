from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal

router = APIRouter(prefix = '/contas')

class AccountResponse(BaseModel):
    id: int
    value: Decimal
    typ: str

class AccountRequest(BaseModel):
    value: Decimal
    typ: str


@router.get('/', response_model=AccountResponse)
def show():
    return AccountResponse(
        id=1, value=100.00, typ='Pagar'
    )

@router.post('/criar', response_model=AccountResponse, status_code=201)
def create(account: AccountRequest):
    return AccountResponse(
        id=2, 
        value=account.value,
        typ=account.typ
    )

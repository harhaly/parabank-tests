from pydantic import BaseModel, Field, field_validator, StrictBool
from typing import Optional


class Accounts_accountsID_transactions(BaseModel):
    id: int
    accountId: int
    type: str
    date: str
    amount: int
    description: str


class Accounts_accountsID(BaseModel):
    id: int
    customerId: int
    type: str
    balance: float


class CustomerID_positions(BaseModel):
    positionId: int
    customerId: int
    name: str
    symbol: str
    shares: int
    purchasePrice: int


class RequestLoan(BaseModel):
    try:
        responseDate: str
        loanProviderName: str
        approved: bool
        message: Optional[str] = None
        accountId: int
    except ValueError as exc:
        print(repr(exc.errors()[0]['type']))


class Address(BaseModel):
    street: str
    city: str
    state: str
    zipCode: str


class Post_custoner_info(BaseModel):
    id: int
    firstName: str
    lastName: str
    address: Address
    phoneNumber: str
    ssn: str

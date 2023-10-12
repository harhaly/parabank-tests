from pydantic import BaseModel
from typing import Optional


class AccountsAccountsIDTransactions(BaseModel):
    id: int
    accountId: int
    type: str
    date: str
    amount: int
    description: str


class AccountsAccountsID(BaseModel):
    id: int
    customerId: int
    type: str
    balance: float


class CustomerIDPositions(BaseModel):
    positionId: int
    customerId: int
    name: str
    symbol: str
    shares: int
    purchasePrice: int


class RequestLoan(BaseModel):
    responseDate: str
    loanProviderName: str
    approved: bool
    message: Optional[str] = None
    accountId: int


class Address(BaseModel):
    street: str
    city: str
    state: str
    zipCode: str


class PostCustomerInfo(BaseModel):
    id: int
    firstName: str
    lastName: str
    address: Address
    phoneNumber: str
    ssn: str


class PositionIDStartDateEndDate(BaseModel):
    symbol: str
    date: str
    closingPrice: int


class PostBillPay(BaseModel):
    payeeName: str
    amount: int
    accountId: int

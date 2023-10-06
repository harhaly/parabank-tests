from pydantic import BaseModel, Field, field_validator


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


class Accounts_accountsID_transactions_amount(BaseModel):
    id: int
    accountId: int
    type: str
    date: str
    amount: int
    description: str


class Customers_customerID_accounts(BaseModel):
    id: int
    customerId: int
    type: str
    balance: float


class AccountID_transactions_month_type(BaseModel):
    id: int
    accountId: int
    type: str
    date: str
    amount: str
    description: str


class AccountID_transactions_fromdate_todate(BaseModel):
    id: int
    accountId: int
    type: str
    date: str
    amount: int
    description: str


class AccountID_transactions_ondate(BaseModel):
    id: int
    accountId: int
    type: str
    date: str
    amount: str
    description: str


class CustomerID_positions(BaseModel):
    positionId: int
    customerId: int
    name: str
    symbol: str
    shares: int
    purchasePrice: int


class AccountID_transactions_ondate(BaseModel):
    id: int
    accountId: int
    type: str
    date: str
    amount: int
    description: str

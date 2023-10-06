from pydantic import BaseModel, Field, field_validator


class Post(BaseModel):
    id: int
    customerId: int
    type: str
    balance: float

    @field_validator('id')
    def check_that_id_is_less_than_two(cls, v):
        if v > 2000000:
            raise ValueError('Id is not less than two')
        else:
            return v

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

class Post_customers_customersId_positions(BaseModel):
    positionId: int
    customerId: str
    name: str
    symbol: str
    shares: int
    purchasePrice: int


#[{'id': 13455, 'customerId': 12434, 'type': 'CHECKING', 'balance': 515.5}]
#{'id': 16763, 'firstName': 'qw', 'lastName': 'qw', 'address': {'street': 'qw', 'city': 'qw', 'state': 'qw', 'zipCode': 'qw'}, 'phoneNumber': 'qw', 'ssn': 'qw'}

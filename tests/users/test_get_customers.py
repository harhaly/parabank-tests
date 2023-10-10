import pytest
import requests

from src.baseclasses.response import Response, Response_json
from src.pydantic_schemas.get_customers import Post, Post_custoner_info, Post_customers_customersId_positions





def test_validate_customres_customerid_positions(get_customer_customerid_position):
    """
    Тест: валидация на значения в полях json customres_customerid_positions
    :param get_customer_customerid_position:
    :return:
    """
    test_object = Response_json(get_customer_customerid_position)
    test_object.assert_status_code(200)
    test_object.validate(Post_customers_customersId_positions)


# def test_validate_customer_customerid_accounts(get_customer_customerid_accounts):
#     """
#     Тест валидация customer_customerid_accounts
#     :param get_customers_id:
#     :return:
#     """
#     test_object = Response_json(get_customer_customerid_accounts)
#     test_object.assert_status_code(200).validate(Post)

# def test_validate_customer_customerid(get_customer_customerid):
#     """
#     Тест: валидация на значения в полях json customer_customerid_accounts
#     :param get_customer_customerid:
#     :return:
#     """
#     test_object = Response_json(get_customer_customerid)
#     test_object.assert_status_code(200)
#     test_object.validate(Post_custoner_info)
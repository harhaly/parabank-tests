import pytest
from src.baseclasses.response import Response, Response_json
from src.pydantic_schemas.get_accounts import *


def test_post_createAccount(post_createAccount):
    """
    Тест валидация POST createAccount
    :param post_createAccount:
    :return:
    """
    test_object = Response_json(post_createAccount)
    test_object.assert_status_code(200).validate(Accounts_accountsID)


def test_post_deposit(post_deposit):
    """
    Тест валидация POST deposit
    :param post_deposit:
    :return:
    """
    test_object = Response(post_deposit)
    test_object.assert_status_code(200).validate_str()


def test_post_withdraw(post_withdraw):
    """
    Тест валидация POST withdraw
    :param post_deposit:
    :return:
    """
    test_object = Response(post_withdraw)
    test_object.assert_status_code(200).validate_str()


def test_post_transfer(post_transfer):
    """
    Тест валидация POST transfer
    :param post_transfer:
    :return:
    """
    test_object = Response(post_transfer)
    test_object.assert_status_code(200).validate_str()

# @pytest.skip
# def test_billpay():
#     pass


def test_post_update_info(post_update_info):
    """
    Тест валидация POST transfer
    :param post_transfer:
    :return:
    """
    test_object = Response(post_update_info)
    test_object.assert_status_code(200).validate_str()


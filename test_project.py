import pytest
from project import what_to_do, alert, expiry
from datetime import date, timedelta
from tabulate import tabulate
from unittest.mock import patch

date_plus_three = (date.today() + timedelta(days=3)).strftime("%Y-%m-%d")
date_plus_five = (date.today() + timedelta(days=5)).strftime("%Y-%m-%d")

FOOD = [
        ["Bananas", date_plus_five],
        ["Apples", date_plus_three],
    ]

HEADERS = ["Food", "Expiry date"]

def test_what_to_do():
    input_value = "  shOW "
    with patch('builtins.input', return_value=input_value):
        result = what_to_do()
    assert result == "show"

def test_alert():
    assert alert(3, FOOD) == tabulate([["Apples", date_plus_three]], headers=HEADERS, tablefmt="grid")
    assert alert(5, FOOD) == tabulate([["Apples", date_plus_three], ["Bananas", date_plus_five]], headers=HEADERS, tablefmt="grid")
    assert alert(2, FOOD) == None

def test_expiry():
    input_value = "3"
    with patch('builtins.input', return_value=input_value):
        result = expiry(FOOD)
    assert result == tabulate([["Apples", date_plus_three]], headers=HEADERS, tablefmt="grid")
    input_value = "1"
    with patch('builtins.input', return_value=input_value):
        result = expiry(FOOD)
    assert result == None

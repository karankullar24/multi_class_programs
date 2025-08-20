from lib.cat_facts import *
from unittest.mock import Mock


def test_get_cat_fact():
    requester_mock = Mock()
    response_mock = Mock()

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {"fact":"Cats can be right-pawed or left-pawed.","length":38}

    catfact = CatFacts(requester_mock)
    assert catfact.provide() == "Cat fact: Cats can be right-pawed or left-pawed."
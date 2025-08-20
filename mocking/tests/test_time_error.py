from lib.time_eror import *
from unittest.mock import Mock

def test_error():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime" : 1755697652.5}
    timer_mock = Mock(namne="timer")
    timer_mock.time.return_value = 1755697652

    timeerror = TimeError(requester_mock,timer_mock)
    assert timeerror.error() == 0.5

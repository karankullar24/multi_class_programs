from lib.secret_diary import *
from unittest.mock import Mock
import pytest

def test_can_instantiate_secret_diary():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    assert secret_diary.diary == diary
    assert secret_diary.unlocked == False

def test_can_unlock_secret_diary():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.unlocked == True

def test_can_lock_secret_diary():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.unlocked == True
    secret_diary.lock()
    assert secret_diary.unlocked == False 

def test_can_not_read_locked_secret_diary():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

def test_can_read_unlocked_secret_diary():
    diary = Mock()
    diary.read.return_value = "My diary entry"
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "My diary entry"

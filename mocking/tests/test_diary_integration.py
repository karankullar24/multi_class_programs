from lib.secret_diary import *
from lib.diary import *
import pytest

def test_secret_diary_instantiates_with_diary():
    diary = Diary("My diary entry")
    secret_diary = SecretDiary(diary)
    assert secret_diary.diary == diary

def test_initially_secret_diary_is_locked():
    diary = Diary("My diary entry")
    secret_diary = SecretDiary(diary)
    assert secret_diary.unlocked == False

def test_can_unlock_secret_diary():
    diary = Diary("My diary entry")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.unlocked == False

def test_can_lock_secret_diary():
    diary = Diary("My diary entry")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.unlocked == False
    secret_diary.lock()
    assert secret_diary.unlocked == True 

def test_can_not_read_locked_diary():
    diary = Diary("My diary entry")
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

def test_can_read_unlocked_diary():
    diary = Diary("My diary entry")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "My diary entry"

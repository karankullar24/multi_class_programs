from lib.diary import *
import pytest


def test_best_entry_with_no_entry_raises_exception():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(1,1)
    error_message = str(e.value)
    assert error_message == "No entries"

def test_all_with_no_entries_returns_empty_list():
    diary = Diary()
    assert diary.all() == []

def test_reading_time_with_no_entry_raises_exception():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(1)
    error_message = str(e.value)
    assert error_message == "No entries"
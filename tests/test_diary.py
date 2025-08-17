from lib.diary import *
import pytest

"""
Initially
There are no entries
"""

def test_no_entries():
    diary = Diary()
    diary.all() == []

def test_best_entry_with_no_entry_raises_exception():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(1)
    error_message = str(e.value)
    assert error_message == "No entries"

def test_reading_time_no_entries_raises_exception():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.reading_time(1)
    error_message = str(e.value)
    assert error_message == "No entries"
from lib.diary import *
import pytest

def test_all_with_no_entries_returns_empty_list():
    diary = Diary()
    assert diary.all() == []

def test_best_entry_with_no_entry_raises_exception():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.readable_entry(1,1)
    error_message = str(e.value)
    assert error_message == "No entries"

def test_complete_with_no_entry_raises_exception():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.complete()
    error_message = str(e.value)
    assert error_message == "No entries"

def test_incomplete_with_no_entry_raises_exception():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.incomplete()
    error_message = str(e.value)
    assert error_message == "No entries"

def test_tru_to_add_non_object_to_diary():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.add(1)
    error_message = str(e.value)
    assert error_message == 'The diary can only hold experiences, contacts or todos.'
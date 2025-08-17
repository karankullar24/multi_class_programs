from lib.diary import *
from lib.diary_entry import *
import pytest

"""
Given a diary entry
Can add instances to Diary
"""

def test_can_add_diary_entries_to_diary():
    diary = Diary()
    entry1 = DiaryEntry("Title 1","My first diary entry")
    entry2 = DiaryEntry("Title 2","My second diary entry that's got more in it to read")
    entry3 = DiaryEntry("Title 3", "My third diary entry that has considerably more to read because I'm so happy that my multi-class program is working so well. How amazing is that, oh my god.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.all() == [entry1,entry2,entry3]

def test_can_count_words_of_all_entries():
    diary = Diary()
    entry1 = DiaryEntry("Title 1","My first diary entry")
    entry2 = DiaryEntry("Title 2","My second diary entry that's got more in it to read")
    entry3 = DiaryEntry("Title 3", "My third diary entry that has considerably more to read because I'm so happy that my multi-class program is working so well. How amazing is that, oh my god.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.count_words() == 44

def test_reading_time_for_whole_diary():
    diary = Diary()
    entry1 = DiaryEntry("Title 1","My first diary entry")
    entry2 = DiaryEntry("Title 2","My second diary entry that's got more in it to read")
    entry3 = DiaryEntry("Title 3", "My third diary entry that has considerably more to read because I'm so happy that my multi-class program is working so well. How amazing is that, oh my god.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.reading_time(1) == 44

def test_best_entry_when_time_and_wpm_equal_to_entry():
    diary = Diary()
    entry1 = DiaryEntry("Title 1","My first diary entry")
    entry2 = DiaryEntry("Title 2","My second diary entry that's got more in it to read")
    entry3 = DiaryEntry("Title 3", "My third diary entry that has considerably more to read because I'm so happy that my multi-class program is working so well. How amazing is that, oh my god.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.find_best_entry_for_reading_time(1,4) == entry1

def test_best_entry_when_time_and_wpm_close_to_middle_size_entry():
    diary = Diary()
    entry1 = DiaryEntry("Title 1","My first diary entry")
    entry2 = DiaryEntry("Title 2","My second diary entry that's got more in it to read")
    entry3 = DiaryEntry("Title 3", "My third diary entry that has considerably more to read because I'm so happy that my multi-class program is working so well. How amazing is that, oh my god.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.find_best_entry_for_reading_time(1,11) == entry2

def test_best_entry_again():
    diary = Diary()
    entry1 = DiaryEntry("Title 1","My first diary entry")
    entry2 = DiaryEntry("Title 2","My second diary entry that's got more in it to read")
    entry3 = DiaryEntry("Title 3", "My third diary entry that has considerably more to read because I'm so happy that my multi-class program is working so well. How amazing is that, oh my god.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.find_best_entry_for_reading_time(1,10) == entry1

def test_best_entry_again2():
    diary = Diary()
    entry1 = DiaryEntry("Title 1","My first diary entry")
    entry2 = DiaryEntry("Title 2","My second diary entry that's got more in it to read")
    entry3 = DiaryEntry("Title 3", "My third diary entry that has considerably more to read because I'm so happy that my multi-class program is working so well. How amazing is that, oh my god.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.find_best_entry_for_reading_time(1,28) == entry2

def test_best_entry_again3():
    diary = Diary()
    entry1 = DiaryEntry("Title 1","My first diary entry")
    entry2 = DiaryEntry("Title 2","My second diary entry that's got more in it to read")
    entry3 = DiaryEntry("Title 3", "My third diary entry that has considerably more to read because I'm so happy that my multi-class program is working so well. How amazing is that, oh my god.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.find_best_entry_for_reading_time(1,40) == entry3
    
def test_best_entry_with_no_suitable_entry():
    diary = Diary()
    entry1 = DiaryEntry("Title 1","My first diary entry")
    entry2 = DiaryEntry("Title 2","My second diary entry that's got more in it to read")
    entry3 = DiaryEntry("Title 3", "My third diary entry that has considerably more to read because I'm so happy that my multi-class program is working so well. How amazing is that, oh my god.")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(1,3) == None
    error_message = str(e.value)
    assert error_message == "No suitable entry"
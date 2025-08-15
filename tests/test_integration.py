from lib.diary import *
from lib.diary_entry import *


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
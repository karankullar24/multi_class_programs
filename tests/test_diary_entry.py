from lib.diary_entry import *

"""
Given a title and contents
Instantiates with properties
"""


def test_initialises_with_title_and_contents():
    diary_entry = DiaryEntry("Title 1","My first diary entry")
    assert diary_entry.title == "Title 1"
    assert diary_entry.contents == "My first diary entry"

"""
Given a diary entry
Can count words in contents
"""

def test_count_words():
    diary_entry = DiaryEntry("Title 1","My first diary entry")
    assert diary_entry.count_words() == 4

def test_reading_time():
    diary_entry = DiaryEntry("Title 1","My first diary entry")
    assert diary_entry.reading_time(1) == 4

def test_reading_chunk_first_use():
    diary_entry = DiaryEntry("Title 1","My first diary entry")
    assert diary_entry.reading_chunk(1,1) == "My"

def test_reading_chunk_second_use():
    diary_entry = DiaryEntry("Title 1","My first diary entry")
    first = diary_entry.reading_chunk(1,1)
    second = diary_entry.reading_chunk(1,1)
    assert second == "first"

def test_reading_chunk_resets():
    diary_entry = DiaryEntry("Title 1","My first diary entry")
    first = diary_entry.reading_chunk(1,1)
    second = diary_entry.reading_chunk(1,3)
    third = diary_entry.reading_chunk(1,1)
    assert third == "My"

def test_reading_chunk_exceeds():
    diary_entry = DiaryEntry("Title 1","My first diary entry")
    assert diary_entry.reading_chunk(1,5) == "My first diary entry"
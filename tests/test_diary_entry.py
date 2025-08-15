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
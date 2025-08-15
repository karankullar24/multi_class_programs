from lib.diary import *

"""
Initially
There are no entries
"""

def test_no_entries():
    diary = Diary()
    diary.all() == []


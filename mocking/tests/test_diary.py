from lib.diary import *

def test_set_contents_property():
    diary = Diary("My diary entry")
    assert diary.contents == "My diary entry"

def test_can_read_contents():
    diary = Diary("My diary entry")
    assert diary.read() == "My diary entry"
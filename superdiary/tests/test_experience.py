from lib.experience import *
import pytest

def test_can_add_experience_and_set_properties():
    experience1 = Experience("Title 1","My first diary entry")
    assert experience1.title == "Title 1"
    assert experience1.contents == "My first diary entry"

def test_can_count_words_in_contents():
    experience1 = Experience("Title 1","My first diary entry")
    assert experience1.count_words() == 4

def test_adding_title_is_int_raises_exception():
    with pytest.raises(Exception) as e:
        experience1 = Experience(1,"My first diary entry")
    error_message = str(e.value)
    assert error_message == "Titles and contents must be created as strings"

def test_adding_title_is_bool_raises_exception():
    with pytest.raises(Exception) as e:
        experience1 = Experience(True,"My first diary entry")
    error_message = str(e.value)
    assert error_message == "Titles and contents must be created as strings"

def test_adding_contents_is_int_raises_exception():
    with pytest.raises(Exception) as e:
        experience1 = Experience("Title 1",1)
    error_message = str(e.value)
    assert error_message == "Titles and contents must be created as strings"

def test_adding_contents_is_bool_raises_exception():
    with pytest.raises(Exception) as e:
        experience1 = Experience("Title 1",True)
    error_message = str(e.value)
    assert error_message == "Titles and contents must be created as strings"
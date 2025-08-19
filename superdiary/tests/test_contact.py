from lib.contact import *
import pytest

def test_can_add_contact_and_set_properties():
    contact1 = Contact("Anjali","07456844748")
    assert contact1.name == "Anjali"
    assert contact1.number == "07456844748"

def test_adding_empty_name_raises_exception():
    with pytest.raises(Exception) as e:
        contact1 = Contact("","07456844748")
    error_message = str(e.value)
    assert error_message == "You can't create a blank contact name or number"

def test_adding_empty_number_raises_exception():
    with pytest.raises(Exception) as e:
        contact1 = Contact("","07456844748")
    error_message = str(e.value)
    assert error_message == "You can't create a blank contact name or number"

def test_adding_non_string_number_raises_exception():
    with pytest.raises(Exception) as e:
        contact1 = Contact("Anjali",7456844748)
    error_message = str(e.value)
    assert error_message == "Number must start with 0, be 11 digits long and be a string"

def test_adding_without_leading0_number_raises_exception():
    with pytest.raises(Exception) as e:
        contact1 = Contact("Anjali","77456844748")
    error_message = str(e.value)
    assert error_message == "Number must start with 0, be 11 digits long and be a string"

def test_adding_too_long_number_raises_exception():
    with pytest.raises(Exception) as e:
        contact1 = Contact("Anjali","04547456844748")
    error_message = str(e.value)
    assert error_message == "Number must start with 0, be 11 digits long and be a string"

def test_adding_too_short_number_raises_exception():
    with pytest.raises(Exception) as e:
        contact1 = Contact("Anjali","04844748")
    error_message = str(e.value)
    assert error_message == "Number must start with 0, be 11 digits long and be a string"

def test_adding_name_is_int_raises_exception():
    with pytest.raises(Exception) as e:
        contact1 = Contact(1,"04844748")
    error_message = str(e.value)
    assert error_message == "Names must be created as strings"

def test_adding_task_is_bool_raises_exception():
    with pytest.raises(Exception) as e:
        contact1 = Contact(True,"04844748")
    error_message = str(e.value)
    assert error_message == "Names must be created as strings"
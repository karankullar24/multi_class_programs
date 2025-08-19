from lib.diary import *
from lib.experience import *
from lib.todo import *
from lib.contact import *
import pytest

def test_can_add_entries_of_any_instance_type():
    diary = Diary()
    experience1 = Experience("Title 1","My first diary entry")
    todo1 = Todo("Go shopping")
    contact1 = Contact("Anjali","07456844748")
    diary.add(experience1)
    diary.add(todo1)
    diary.add(contact1)
    assert diary.entries == [experience1,todo1,contact1]

def test_can_add_entries_of_any_instance_type_and_list_with_all_method():
    diary = Diary()
    experience1 = Experience("Title 1","My first diary entry")
    todo1 = Todo("Go shopping")
    contact1 = Contact("Anjali","07456844748")
    diary.add(experience1)
    diary.add(todo1)
    diary.add(contact1)
    assert diary.all() == [experience1,todo1,contact1]

def test_can_get_readable_entry_in_time_at_speed():
    diary = Diary()
    experience1 = Experience("Title 1","My first diary entry")
    todo1 = Todo("Go shopping")
    contact1 = Contact("Anjali","07456844748")
    experience2 = Experience("Title 2","My next entry is a little longer")
    diary.add(experience1)
    diary.add(todo1)
    diary.add(contact1)
    diary.add(experience2)
    assert diary.readable_entry(1,6) == experience1

def test_can_get_readable_entry_in_time_at_speed2():
    diary = Diary()
    experience1 = Experience("Title 1","My first diary entry")
    todo1 = Todo("Go shopping")
    contact1 = Contact("Anjali","07456844748")
    experience2 = Experience("Title 2","My next entry is a little longer")
    diary.add(experience1)
    diary.add(todo1)
    diary.add(contact1)
    diary.add(experience2)
    assert diary.readable_entry(1,7) == experience2

def test_can_get_contacts_as_list_of_tuples():
    diary = Diary()
    experience1 = Experience("Title 1","My first diary entry")
    todo1 = Todo("Go shopping")
    contact1 = Contact("Anjali","07456844748")
    experience2 = Experience("Title2","My next entry is a little longer")
    contact2 = Contact("Zain","07456845548")
    diary.add(experience1)
    diary.add(todo1)
    diary.add(contact1)
    diary.add(experience2)
    diary.add(contact2)
    assert diary.list_contacts() == [("Anjali","07456844748"),("Zain","07456845548")]

def test_can_get_incomplete_todos_as_list():
    diary = Diary()
    experience1 = Experience("Title 1","My first diary entry")
    todo1 = Todo("Go shopping")
    contact1 = Contact("Anjali","07456844748")
    experience2 = Experience("Title2","My next entry is a little longer")
    contact2 = Contact("Zain","07456845548")
    todo2 = Todo("Walk dog")
    diary.add(experience1)
    diary.add(todo1)
    diary.add(contact1)
    diary.add(experience2)
    diary.add(contact2)
    diary.add(todo2)
    todo2.mark_complete()
    assert diary.incomplete() == [todo1]

def test_can_get_complete_todos_as_list():
    diary = Diary()
    experience1 = Experience("Title 1","My first diary entry")
    todo1 = Todo("Go shopping")
    contact1 = Contact("Anjali","07456844748")
    experience2 = Experience("Title2","My next entry is a little longer")
    contact2 = Contact("Zain","07456845548")
    todo2 = Todo("Walk dog")
    diary.add(experience1)
    diary.add(todo1)
    diary.add(contact1)
    diary.add(experience2)
    diary.add(contact2)
    diary.add(todo2)
    todo2.mark_complete()
    assert diary.complete() == [todo2]

def test_complete_incomplete_with_no_todos_raises_exception():
    diary = Diary()
    experience1 = Experience("Title 1","My first diary entry")
    contact1 = Contact("Anjali","07456844748")
    experience2 = Experience("Title2","My next entry is a little longer")
    contact2 = Contact("Zain","07456845548")
    diary.add(experience1)
    diary.add(contact1)
    diary.add(experience2)
    diary.add(contact2)
    with pytest.raises(Exception) as e:
        diary.complete()
    error_message = str(e.value)
    assert error_message == "No todo entries"
    with pytest.raises(Exception) as e:
        diary.incomplete()
    error_message2 = str(e.value)
    assert error_message2 == "No todo entries"

def test_list_contacts_with_no_contacts_raises_exception():
    diary = Diary()
    experience1 = Experience("Title 1","My first diary entry")
    experience2 = Experience("Title2","My next entry is a little longer")
    diary.add(experience1)
    diary.add(experience2)
    with pytest.raises(Exception) as e:
        diary.list_contacts()
    error_message = str(e.value)
    assert error_message == "No contact entries"

def test_readable_entry_with_no_experiences_raises_exception():
    diary = Diary()
    todo1 = Todo("Go shopping")
    contact1 = Contact("Anjali","07456844748")
    contact2 = Contact("Zain","07456845548")
    todo2 = Todo("Walk dog")
    diary.add(todo1)
    diary.add(contact1)
    diary.add(contact2)
    diary.add(todo2)
    with pytest.raises(Exception) as e:
        diary.readable_entry(1,1)
    error_message = str(e.value)
    assert error_message == "No experience entries"

def test_no_suitable_expereince_for_time_and_speed():
    diary = Diary()
    experience1 = Experience("Title 1","My first diary entry")
    todo1 = Todo("Go shopping")
    contact1 = Contact("Anjali","07456844748")
    experience2 = Experience("Title 2","My next entry is a little longer")
    diary.add(experience1)
    diary.add(todo1)
    diary.add(contact1)
    diary.add(experience2)
    with pytest.raises(Exception) as e:
        diary.readable_entry(1,1)
    error_message = str(e.value)
    assert error_message == "No suitable entry"
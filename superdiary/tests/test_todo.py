from lib.todo import *
import pytest

def test_can_create_todo_and_get_task_and_initial_completion_status():
    task1 = Todo("Go shopping")
    assert task1.task == "Go shopping"
    assert task1.complete == False

def test_can_mark_todo_complete():
    task1 = Todo("Go shopping") 
    task1.mark_complete()
    assert task1.complete == True

def test_adding_empty_task_raises_exception():
    with pytest.raises(Exception) as e:
        task1 = Todo("")
    error_message = str(e.value)
    assert error_message == "You can't create a blank task"

def test_adding_task_is_int_raises_exception():
    with pytest.raises(Exception) as e:
        task1 = Todo(1)
    error_message = str(e.value)
    assert error_message == "Tasks must be created as strings"

def test_adding_task_is_bool_raises_exception():
    with pytest.raises(Exception) as e:
        task1 = Todo(True)
    error_message = str(e.value)
    assert error_message == "Tasks must be created as strings"
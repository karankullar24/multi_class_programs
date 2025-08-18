from lib.todo_list import *
import pytest

def test_todo_list_initially_empty():
    todo_list = TodoList()
    assert todo_list.todos == []

def test_todo_list_incomplete_method_empty_list_if_todo_list_empty():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

def test_todo_list_complete_method_empty_list_if_todo_list_empty():
    todo_list = TodoList()
    assert todo_list.complete() == []

def test_todo_list_give_up_method_raises_exception_if_todo_list_empty():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.give_up()
    error_message = str(e.value)
    assert error_message == "Empty Todo List! No tasks to give up on!"

def test_adding_non_todo_object_to_todo_list_raises_exception():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.add("Clean car")
    error_message = str(e.value)
    assert error_message == "Todo List items must be Todo objects"
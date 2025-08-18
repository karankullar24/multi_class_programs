from lib.todo_list import *
from lib.todo import *
import pytest

def test_can_add_todo_instance_to_todo_list():
    todo_list = TodoList()
    task1 = Todo("Go shopping")
    todo_list.add(task1)
    assert todo_list.todos == [task1]

def test_can_add_multiple_todo_instances_to_todo_list():
    todo_list = TodoList()
    task1 = Todo("Go shopping")
    task2 = Todo("Water plants")
    todo_list.add(task1)
    todo_list.add(task2)
    assert todo_list.todos == [task1,task2]

def test_can_list_todos_that_are_incomplete():
    todo_list = TodoList()
    task1 = Todo("Go shopping")
    task2 = Todo("Water plants")
    todo_list.add(task1)
    todo_list.add(task2)
    task1.mark_complete()
    assert todo_list.incomplete() == [task2]

def test_can_list_todos_that_are_complete():
    todo_list = TodoList()
    task1 = Todo("Go shopping")
    task2 = Todo("Water plants")
    todo_list.add(task1)
    todo_list.add(task2)
    task1.mark_complete()
    assert todo_list.complete() == [task1]

def test_giveup_makrs_all_todos_as_complete():
    todo_list = TodoList()
    task1 = Todo("Go shopping")
    task2 = Todo("Water plants")
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.give_up()
    assert todo_list.complete() == [task1,task2]
    assert todo_list.incomplete() == []

def test_adding_task_that_is_already_in_list_as_incomplete_raises_exception():
    todo_list = TodoList()
    task1 = Todo("Go shopping")
    task2 = Todo("Go shopping")
    todo_list.add(task1)
    with pytest.raises(Exception) as e:
        todo_list.add(task2)
    error_message = str(e.value)
    assert error_message == "You already have this task as incomplete in your Todo List"

def test_adding_task_that_is_already_in_list_as_complete_accepts_add():
    todo_list = TodoList()
    task1 = Todo("Go shopping")
    task2 = Todo("Go shopping")
    todo_list.add(task1)
    task1.mark_complete()
    todo_list.add(task2)
    assert todo_list.todos == [task1,task2]

def test_give_up_raises_exception_if_all_taks_are_complete_already():
    todo_list = TodoList()
    task1 = Todo("Go shopping")
    task2 = Todo("Water plants")
    todo_list.add(task1)
    todo_list.add(task2)
    task1.mark_complete()
    task2.mark_complete()
    with pytest.raises(Exception) as e:
        todo_list.give_up()
    error_message = str(e.value)
    assert error_message == "Chill out, all tasks are complete already!"
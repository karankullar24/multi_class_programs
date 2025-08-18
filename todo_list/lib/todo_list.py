from lib.todo import *

class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        if not isinstance(todo,Todo):
            raise Exception("Todo List items must be Todo objects")
        for todo_object in self.todos:
            if todo_object.task == todo.task and todo_object.complete == False:
                raise Exception("You already have this task as incomplete in your Todo List")
        self.todos.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_todos = [todo_object for todo_object in self.todos if todo_object.complete == False]
        return incomplete_todos
    
    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_todos = [todo_object for todo_object in self.todos if todo_object.complete == True]
        return complete_todos

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        if self.todos == []:
            raise Exception("Empty Todo List! No tasks to give up on!")
        if all(todo_object.complete for todo_object in self.todos):
            raise Exception("Chill out, all tasks are complete already!")
        for todo_object in self.todos:
            todo_object.mark_complete()

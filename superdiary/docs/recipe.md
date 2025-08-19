# Diary tracking experiences,tasks and contacts Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to-cou see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌──────────────────────────────────────────────────────────────┐      ┌────────────────────────────────────┐   
│Diary                                                         │      │ Experience(title,contents)         │   
│Owns list of                                                  │      │                                    │   
│- experience                                                  │      │ -title                             │   
│- todos                                                       │      │ -contents                          │   
│- contacts                                                    │      │                                    │   
│                                                              ├────► │ -count_words()                     │   
│-add(experience)                                              │      │  => int of total words in contents │   
│-add(todo)                                                    │      │                                    │   
│-add(contact)                                                 │      │                                    │   
│                                                              │      └────────────────────────────────────┘   
│-read_diary()                                                 │                                               
│ => "title1"                                                  │                                               
│    "contents1"                                               │      ┌───────────────────────────────────────┐
│    "title2"                                                  │      │  Todo(task,False)                     │
│    "contents2"...                                            │      │                                       │
│    "task1"                                                   │      │  -task                                │
│    "incomplete"                                              ├─────►│  -completion as bool                  │
│    "task2"                                                   │      │                                       │
│    "complete"                                                │      │  -mark_complete()                     │
│    "contact1"                                                │      │   => sets completion to True          │
│    "number1"                                                 │      │                                       │
│     ...                                                      │      └───────────────────────────────────────┘
│                                                              │                                               
│-readable_entry(wpm,minutes)                                  │      ┌──────────────────────────────────────┐ 
│  => longest experience readable in time as strings           │      │  Contact(name,number)                │ 
│     instance of entry                                        │      │                                      │ 
│                                                              │      │  -name                               │ 
│                                                              ├─────►│  -number                             │ 
│-list_contacts()                                              │      │                                      │ 
│  => [(contact1,number1),(contact2,number2)....)              │      │                                      │ 
│                                                              │      │                                      │ 
│-complete()                                                   │      │                                      │ 
│ => list complete todos                                       │      └──────────────────────────────────────┘ 
│                                                              │                                               
│-incomplete()                                                 │                                               
│ => list incomplete todos                                     │                                               
│                                                              │                                               
└──────────────────────────────────────────────────────────────┘                                               
```

_Also design the interface of each class in more detail._
     
```python
class Diary():

    def __init__(self):
        # Side-effects:
        #   Initially a empty lists of experiences, todos and contacts
        pass # No code here yet

    def add(self, entry):
        # Parameters:
        #   entry: an instance of Experience, Todo or Contact
        # Side-effects:
        #   Adds the entry to the relevant property of the self object
        pass # No code here yet

    def readable_entry(self, wpm,minutes):
        # Parameters:
        #  wpm: int representing reading speed in words per minute
        #  minutes: int representing time availble
        # Returns:
        #   Instance of expereinece readable within time
        pass # No code here yet
    
    def list_contacts(self):
        # Returns:
        #   List of tuples (contact,number)
        pass # No code here yet

    def complete(self):
        # Returns:
        #   List of complete Todo instances 
        pass # No code here yet

    def incomplete(self):
        # Returns:
        #   List of incomplete Todo instances
        pass # No code here yet

class Experience():
    # User-facing properties:
    #   title: string
    #   contents: string

    def __init__(self, title, contents): 
        # Parameters:
        #   title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass # No code here yet

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass # No code here yet

class Todo():
    # User-facing properties:
    #   task: string

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

class Contact():
    # User-facing properties:
    #   name: string
    #   number: string

    def __init__(self, name, number):
        # Parameters:
        #   name: a string representing the name of the contact
        #   number: a string representing the contact phone number
        # Side-effects:
        #   Sets the nanme property
        #   Sets the number property
        pass
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a diary
When we add an experience, a todo and a contact
We can
"""
diary = Diary()
experience1 = Experience("Title 1","My first diary entry")
todo1 = Todo("Go shopping")
contact1 = Contact("Anjali","07456844748")
Diary.add(experience1)
Diary.add(todo1)
Diary.add(contact1)
diary.entries # => [experience1, todo1, contact1]

"""
Given a diary
When we have a reading speed and available time to read 
We can select suitable entry to read
"""
diary = Diary()
experience1 = Experience("Title 1","My first diary entry")
todo1 = Todo("Go shopping")
contact1 = Contact("Anjali","07456844748")
experience2 = Experience("Title2","My next entry is a little longer")
diary.add(experience1)
diary.add(todo1)
diary.add(contact1)
diary.add(experience2)
diary.readable_entry(1,6) # => experience2

"""
Given a diary
We can list contacts
"""
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
diary.list_numbers # => [("Anjali","07456844748"),("Zain","07456845548")]

"""
Given a diary
We can list complete todos
"""
diary = Diary()
experience1 = Experience("Title 1","My first diary entry")
todo1 = Todo("Go shopping")
contact1 = Contact("Anjali","07456844748")
expereinece2 = Experience("Title2","My next entry is a little longer")
contact2 = Contact("Zain","07456845548")
todo2 = Todo("Walk dog")
diary.add(experience1)
diary.add(todo1)
diary.add(contact1)
diary.add(experience2)
diary.add(contact2)
diary.add(todo2)
todo2.mark_complee()
diary.complete() # => [todo2]

"""
Given a diary
We can list incomplete todos
"""
diary = Diary()
experience1 = Experience("Title 1","My first diary entry")
todo1 = Todo("Go shopping")
contact1 = Contact("Anjali","07456844748")
expereinece2 = Experience("Title2","My next entry is a little longer")
contact2 = Contact("Zain","07456845548")
todo2 = Todo("Walk dog")
todo2.mark_complee()
diary.add(experience1)
diary.add(todo1)
diary.add(contact1)
diary.add(experience2)
diary.add(contact2)
diary.add(todo2)
diary.incomplete() # => [todo1]

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given an experience with a title and contents
We see the title and contents reflected in the relevant property
"""
experience1 = Experience("Title 1","My first diary entry")
expereinece1.title # => "Title 1"
expereinece1.contents # => "My first diary entry"

"""
Given an experience with a title and contents
We can count words in contents
"""
experience1 = Experience("Title 1","My first diary entry")
expereinece1.title # => "Title 1"
expereinece1.contents # => "My first diary entry"
expereinece1.count_words() # => int 4

"""
Given a task to complete 
We can see the the task in the task property and set completion to false
"""
todo1 = Todo("Go shopping")
todo1.task # => "Go shopping"
todo1.complete # => False as bool

"""
Given a task 
We can set the task as complete
"""
todo1 = Todo("Go shopping")
todo1.mark_complete() # => "Go shopping"
todo1.complete # => True as bool

"""
Given a contact with name and number 
We can see the the name and number in the relvant property  in the task property and set completion to false
"""
contact1 = Contact("Anjali","07456844748")
# contact1.name => "Anjali"
# contact1.number => "07456844748"

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
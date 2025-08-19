from lib.experience import *
from lib.todo import *
from lib.contact import *

class Diary():

    def __init__(self):
        # Side-effects:
        #   Initially a empty lists of experiences, todos and contacts
        self.entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of Experience, Todo or Contact
        # Side-effects:
        #   Adds the entry to the relevant property of the self object
        self.entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries

    def readable_entry(self, wpm,minutes):
        # Parameters:
        #  wpm: int representing reading speed in words per minute
        #  minutes: int representing time availble
        # Returns:
        #   Instance of expereinece readable within time
        if self.all() == []:
            raise Exception("No entries")
        
        if not any([isinstance(entry,Experience) for entry in self.all()]):
            raise Exception("No experience entries")   
             
        total_words_readable = wpm * minutes
        entry_words_dict = {entry: entry.count_words() for entry in self.all() if isinstance(entry,Experience) and entry.count_words() <= total_words_readable}
        try:
            return max(entry_words_dict, key = entry_words_dict.get)
        except ValueError:
            raise Exception("No suitable entry")

    def list_contacts(self):
        # Returns:
        #   List of tuples (contact,number)
        if self.all() == []:
            raise Exception("No entries")
        
        if not any([isinstance(entry,Contact) for entry in self.all()]):
            raise Exception("No contact entries")
        
        contact_list = [(entry.name,entry.number) for entry in self.all() if isinstance(entry,Contact)]
        return contact_list 
    
    def complete(self):
        # Returns:
        #   List of complete Todo instances 
        if self.all() == []:
            raise Exception("No entries")
        
        if not any([isinstance(entry,Todo) for entry in self.all()]):
            raise Exception("No todo entries")
        
        complete_todos = [entry for entry in self.all() if isinstance(entry,Todo) and entry.complete]
        return complete_todos

    def incomplete(self):
        # Returns:
        #   List of incomplete Todo instances
        if self.all() == []:
            raise Exception("No entries")
        
        if not any([isinstance(entry,Todo) for entry in self.all()]):
            raise Exception("No todo entries")
        
        incomplete_todos = [entry for entry in self.all() if isinstance(entry,Todo) and not entry.complete]
        return incomplete_todos


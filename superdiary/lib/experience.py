class Experience():
    # User-facing properties:
    #   title: string
    #   contents: string

    def __init__(self, title, contents): 
        # Parameters:
        #   title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties

        if not isinstance(title,str) or not isinstance(contents,str) :
            raise Exception("Titles and contents must be created as strings")
        
        self.title = title
        self.contents = contents

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.contents.split())

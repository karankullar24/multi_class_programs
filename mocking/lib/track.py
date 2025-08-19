class Track:
    def __init__(self, title, artist):
        # title and artist are both strings
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        return keyword in self.title or keyword in self.artist
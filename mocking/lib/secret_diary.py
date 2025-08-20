class SecretDiary:
    def __init__(self, diary):
        # diary is an instance of Diary
        self.diary = diary
        self.unlocked = False

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        if self.unlocked:
            return self.diary.read()
        else:
            raise Exception("Go away!")

    def lock(self):
        # Locks the diary
        # Returns nothing
        self.unlocked = False

    def unlock(self):
        # Unlocks the diary
        # Returns nothing
        self.unlocked = True
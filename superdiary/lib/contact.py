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
        if name == "" or number == "":
            raise Exception("You can't create a blank contact name or number")
        if not isinstance(name,str):
            raise Exception("Names must be created as strings")
        if not isinstance(number,str) or len(number) != 11 or number[0] != "0":
            raise Exception("Number must start with 0, be 11 digits long and be a string")
        self.name = name
        self.number = number
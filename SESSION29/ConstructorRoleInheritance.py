class One:
    def __init__(self):
        print("One Constructor")

class Two:
    pass

class Three(Two, One):
    def __init__(self):
        super().__init__()

class Four(Three):
    def __init__(self):
        print("Four Constructor")

class Five(Three):
    def __init__(self):
        One.__init__(self)

five = Five()
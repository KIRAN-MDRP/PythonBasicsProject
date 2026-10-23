class NumberOne:
    def __init__(self):
        print("From Number One Constructor")

class NumberTwo(NumberOne):
    def __init__(self):
        #print("From Number Two Constructor")
        super().__init__()

nt = NumberTwo()

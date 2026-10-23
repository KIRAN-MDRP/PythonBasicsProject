from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def playerDetails(self):
        pass

    def qualifiedSelectionCommitee(self):
        return "BCCI"

class CreatePlayer(Player):

    def __init__(self):
        self.playerName = input("Enter Player Name: ")

    def playerDetails(self):
        self.battingSide = input("Enter Batting Side: ")
        self.bowlingSide = input("Enter Bowling Side: ")
        return f"Player Name: {self.playerName}, Batting Side: {self.battingSide}, Bowling Side: {self.bowlingSide}, Selection Committee: {self.qualifiedSelectionCommitee()}"

cp = CreatePlayer()
print(cp.playerDetails())

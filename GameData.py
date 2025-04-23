__author__ = 'Jeff Werner'

class AnalysisData():
     def __init__(self, GameData, WinnerExists, AIWin, AIFirst, AIChoices, OpponentChoices):
        self.GameData = GameData
        self.WinnerExists = WinnerExists
        self.AIWin = AIWin
        self.AIFirst = AIFirst
        self.AIChoices = AIChoices
        self.OpponentChoices = OpponentChoices
    #{WinnerExists: False, "AIWin": False, "AIFirst": False, "AIChoices": [], "OpponentChoices": [] }

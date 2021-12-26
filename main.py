# define Score class
class Score:
  def __init__(self, waarde=0):
    self.waarde = waarde
  def optellenScore(self, waarde):
    self.waarde = self.waarde + waarde
  def aftrekkenScore(self, waarde):
    self.waarde = self.waarde - waarde

# define Speler class
class Speler:
  def __init__(self, naam, score=0):
    self.naam = naam
    self.Score = Score(score)
  
# creating lists       
lijstSpelers = [] 
lijstScores = [5, 10, 20]
  
# appending instances to list 
lijstSpelers.append( Speler('Marc') )
lijstSpelers.append( Speler('Marieke', 5) )
lijstSpelers.append( Speler('Alexander', 11) )

# looping list
i = -1
for obj in lijstSpelers:
  i += 1
  obj.Score.optellenScore(lijstScores[i])
  print( obj.naam, obj.Score.waarde )
  obj.Score.aftrekkenScore(lijstScores[i] - 3)
  print( obj.naam, obj.Score.waarde )
  
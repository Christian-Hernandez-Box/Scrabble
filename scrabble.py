# Program Data Points
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Creating Dictionary; Combining Two Lists
letter_to_points = {letters : points for letters, points in zip(letters, points)}

# Adding Blank Tiles To The Existing Dictionary
letter_to_points[" "] = 0

# Defining Function; Returns Word-Point Valuation
def score_word(word):
  point_total = 0 
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

# Testing Function; Expected Outcome is 15
#brownie_points = score_word("BROWNIE")
#print(brownie_points)

# Dictionary Connecting Players w/ Words They've Played
player_to_words = {"player1":[" BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

# Iterate Through The Existing Dictionary & Map Total Points Accordingly
player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

# Output Current Point Total For Each Player
scrabble_point_update = "Thank you for playing Scrabble! Here is the current point standings: " + str(player_to_points)
print(scrabble_point_update)
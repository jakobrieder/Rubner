import random
#Speileinstelungen wie viele Karten pro Hand und wie oft gespielt wird
cards_per_hand = 5
games = 100000

colors = ["Herz", "Karo", "Pik", "Kreuz"]
values = ["2", "3", "4", "5", "6", "7", "8", "9",
          "10", "Bube", "Dame", "König", "Ass"]

# Ziehen der Karten

def shuffleAndDraw():
  deck = [(v, c) for c in colors for v in values]
  random.shuffle(deck)
  return deck[:cards_per_hand] # Slicing ein Teil der Liste wird zurückgegeben - ersten 5 Karten

def isPair(hand):
  valueOnly = [v for (v, c) in hand]
  for v in valueOnly:
    if valueOnly.count(v) == 2:
      return True
  return False

def isTwoPair(hand):
  valueOnly = [v for (v, c) in hand]
  pairs = 0
  counted = []
  for v in valueOnly:
    if v not in counted and valueOnly.count(v) == 2: # wenn noch nicht dgezählt und ein Paar
      pairs += 1
      counted.append(v) # hinzufügen zu der Liste der gezählten Paare
  return pairs == 2

def isThreeOfAKind(hand):
  valueOnly = [v for (v, c) in hand]
  for v in valueOnly:
    if valueOnly.count(v) == 3:
      return True
  return False

def isFourOfAKind(hand):
  valueOnly = [v for (v, c) in hand]
  for v in valueOnly:
    if valueOnly.count(v) == 4:
      return True
  return False

def isFullHouse(hand):
  return isThreeOfAKind(hand) and isPair(hand)

def isFlush(hand):
  colorOnly = [c for (v, c) in hand]
  return len(set(colorOnly)) == 1 # gibt es nur eine Farbe in der Hand --> Flush

def isStraight(hand):
  order = ["2", "3", "4", "5", "6", "7", "8",
           "9", "10", "Bube", "Dame", "König", "Ass"]
  valueOnly = [v for (v, c) in hand]
  nums = [order.index(v) for v in valueOnly] # Karten index geben damit man schaue kann ob aufeinanderfolgen
  nums.sort() # aufsteigende Sortierung
  # Keine doppelten Karten
  if len(set(nums)) != len(nums):
    return False

  if all(nums[i + 1] == nums[i] + 1 for i in range(len(nums) - 1)): #prüfen ob Karten aufeinanderfogen; wenn alle true im all Ausrdruck --> alle Werte aufeinanderfolgend; len-1 weil 4 zwischenräume
    return True

  # Spezialfall Wheel (Ass, 2, 3, 4, 5)
  wheel = set(nums) == {12, 0, 1, 2, 3}
  return wheel

def isStraightFlush(hand):
  return isFlush(hand) and isStraight(hand)

def isRoyalFlush(hand):
  if not isFlush(hand):
    return False
  order = ["2", "3", "4", "5", "6", "7", "8",
           "9", "10", "Bube", "Dame", "König", "Ass"]
  valueOnly = [v for (v, c) in hand]
  nums = [order.index(v) for v in valueOnly]
  nums.sort()
  return nums[-5:] == [8, 9, 10, 11, 12]  # letzten 5 Werte von nums müssen index für royal flush sein (und geiche Farbe wird oben durch Straight gepürft)


def main():
  results = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Four of a Kind": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a Kind": 0,
    "Two Pair": 0,
    "One Pair": 0,
    "High Card": 0
  }
# Spielen und Hand ziehen
  for i in range(games):
    hand = shuffleAndDraw()
#Zählen der Kombinationen
    if isRoyalFlush(hand):
      results["Royal Flush"] += 1
    elif isStraightFlush(hand):
      results["Straight Flush"] += 1
    elif isFourOfAKind(hand):
      results["Four of a Kind"] += 1
    elif isFullHouse(hand):
      results["Full House"] += 1
    elif isFlush(hand):
      results["Flush"] += 1
    elif isStraight(hand):
      results["Straight"] += 1
    elif isThreeOfAKind(hand):
      results["Three of a Kind"] += 1
    elif isTwoPair(hand):
      results["Two Pair"] += 1
    elif isPair(hand):
      results["One Pair"] += 1
    else:
      results["High Card"] += 1



  print(f"\nNach {games} Spielen mit {cards_per_hand} Karten pro Hnad:\n")
  print(f"{'Kombination':17s} | {'Anzahl':>8s} | {'%':>8s}") # 17 und 8 Zeichen lang; links und rechtsbündig (ChatGPT Ausgabe zur schöneren Formatierung)
  print("-" * 38)
  for name, count in results.items(): # Auswertung des Diciotnary
    percent = round(count / games * 100, 5) # % ausrechnen und auf 5 Kommastellen runden
    print(f"{name:17s} | {count:8d} | {percent:8.5f}")

if __name__ == "__main__":
  main()

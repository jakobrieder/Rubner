import random
#Speileinstelungen wie viele Karten pro Hand und wie oft gespielt wird
cards_per_hand = 5
games = 100000

colors = ["Herz", "Karo", "Pik", "Kreuz"]
values = ["2", "3", "4", "5", "6", "7", "8", "9",
          "10", "Bube", "Dame", "König", "Ass"]

# Ziehen der Karten und Mischeln

def shuffleAndDraw():
  deck = [(v, c) for c in colors for v in values] # Liste aus Tupeln
  random.shuffle(deck)
  return deck[:cards_per_hand] # Slicing - ersten 5 Karten zurückgegeben

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
    if v not in counted and valueOnly.count(v) == 2: # wenn noch nicht gezählt und ein Paar
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
  # Keine doppelten Karten - dann kann es keine Strasse sein
  if len(set(nums)) != len(nums):
    return False

  if all(nums[i + 1] == nums[i] + 1 for i in range(len(nums) - 1)): #prüfen ob Karten aufeinanderfolgen; wenn alle true im all Ausrdruck --> alle Werte aufeinanderfolgend; len-1 weil 4 zwischenräume i +1 muss noch in Liste liegen
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

# Echte Prozentwerte (Wikipedia)
truePercents = {
  "Royal Flush": 0.000154,
  "Straight Flush": 0.001385,
  "Four of a Kind": 0.02401,
  "Full House": 0.1441,
  "Flush": 0.1965,
  "Straight": 0.3925,
  "Three of a Kind": 2.1128,
  "Two Pair": 4.7539,
  "One Pair": 42.2569,
  "High Card": 50.1177
}

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

  lastHand = None

  #Spielen
  for i in range(games):
    hand = shuffleAndDraw()
    lastHand = hand
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

  print("Letzte gezogene Hand:")
  print(", ".join(f"({v}, {c})" for (v, c) in lastHand))

  print(f"\nNach {games} Spielen mit {cards_per_hand} Karten pro Hand:\n")
  print(f"{'Kombination':17s} | {'Anzahl':>8s} | {'Sim %':>10s}")
  print("-" * 42)
  simPercents = {}
  for name, count in results.items():
    percent = round(count / games * 100, 5)
    simPercents[name] = percent
    print(f"{name:17s} | {count:8d} | {percent:10.5f}")

  # Vergleich mit den echten Werten
  print("\nVergleich mit echten Werten (Wikipedia):")
  print(f"{'Kombination':17s} | {'Echt %':>10s} | {'Sim %':>10s} | {'Diff pp':>10s}")
  print("-" * 62)
  for name in results.keys():
    true_p = truePercents[name]
    sim_p = simPercents[name]
    diff = sim_p - true_p  # Prozentpunkte (Sim - Echt)
    print(f"{name:17s} | {true_p:10.5f} | {sim_p:10.5f} | {diff:10.5f}")

if __name__ == "__main__":
  main()

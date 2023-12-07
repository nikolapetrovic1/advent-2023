from functools import cmp_to_key
def count_cards(val,cards):
  hand = val[0]
  hand_dict = {}
  for card in cards:
    occurences = hand.count(card)
    if occurences > 0:
      hand_dict[card] = occurences
  return (hand_dict, hand,val[1])

def calculate_hand(hand_dict):
  #5-of-kind
  if len(hand_dict.keys()) == 1:
    return 1000
  if len(hand_dict.keys()) == 2:
    for key in hand_dict:
      #full house
      if hand_dict[key] == 3:
        return 80
      #four of kind
      if hand_dict[key] == 4:
        return 90
  if len(hand_dict.keys()) == 3:
    for key in hand_dict:
      if hand_dict[key] == 3:
        return 70
      if hand_dict[key] == 2:
        return 60
  if len(hand_dict.keys()) == 4:
    return 50
  #high card
  if len(hand_dict.keys()) == 5:
    return 1

def rank_same_hands(val1,val2):
  hand1= val1[1]
  hand2= val2[1]
  hand1_score = calculate_hand(val1[0])
  hand2_score = calculate_hand(val2[0])
  if hand1_score == hand2_score:
    for i in range(0,len(hand1)):
      if card_ranking[hand1[i]] > card_ranking[hand2[i]]:
        return 1
      if card_ranking[hand1[i]] < card_ranking[hand2[i]]:
        return -1
  if hand1_score > hand2_score:
    return 1
  else:
    return -1
  

def combined_sort(val):
  return calculate_hand(val), rank_same_hands
  

f = open("input.txt", "r")
lines = f.read().splitlines()
vals = [line.split(" ") for line in lines]

cards = ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]
cards = list(map(str,cards))
cards.reverse()
card_ranking = {}
for idx,card in enumerate(cards):
  card_ranking[card] = 10 * idx

hand_rankings = {}

hand_count = list(map(lambda val: count_cards(val,cards), vals))

hand_count = sorted(hand_count, key=cmp_to_key(rank_same_hands))
scores = list(map(lambda x:int(x[2]),hand_count))
result = 0
for i in range(0,len(scores)):
  result += scores[i] * (i+1)

print(result)
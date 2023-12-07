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
    return 100
  if len(hand_dict.keys()) == 2:
    for key in hand_dict:
      #four of kind
      if hand_dict[key] == 4:
        return 90
      #full house
      if hand_dict[key] == 3:
        return 80
  if len(hand_dict.keys()) == 3:
    for key in hand_dict:
      #triple
      if hand_dict[key] == 3:
        return 70
      #two-pairs
      if hand_dict[key] == 2:
        return 60
  #one-pair
  if len(hand_dict.keys()) == 4:
    return 50
  #high card
  if len(hand_dict.keys()) == 5:
    return 1

def rank_same_hands(val1,val2):
  hand1 = val1[1]
  hand2 = val2[1]
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

def sort_part_2(card1,card2):
  if card1[1] > card2[1]:
    return 1
  elif card1[1] < card2[1]:
    return -1
  if card_ranking[card1[0]] > card_ranking[card2[0]]:
    return 1
  elif card_ranking[card1[0]] < card_ranking[card2[0]]:
    return -1
  return 0
  

def find_strongest(hand):
  tuples = list(map(lambda x: (x,hand[x]),hand.keys()))
  tuples = sorted(tuples, key=cmp_to_key(sort_part_2),reverse=True)
  strongest = tuples[0][0]
  if strongest == 'J':
    if len(tuples) != 1:
      return tuples[1][0]
  return strongest

def apply_wildcard(hand):
  hand_dict = hand[0]
  strongest = find_strongest(hand_dict)
  if 'J' == strongest:
    return hand
  if 'J' in hand_dict:
    hand_dict[strongest] += hand_dict['J']
    del hand_dict['J']
  return hand

def calculate_score(hand_count):
  hand_count = sorted(hand_count, key=cmp_to_key(rank_same_hands))
  scores = list(map(lambda x:int(x[2]),hand_count))
  result = 0
  for i in range(0,len(scores)):
    result += scores[i] * (i+1)
  print(result)
  
def prepare_cards(cards):
  cards = list(map(str,cards))
  cards.reverse()
  card_ranking = {}
  for idx,card in enumerate(cards):
    card_ranking[card] = 10 * idx
  return cards,card_ranking

f = open("input.txt", "r")
lines = f.read().splitlines()
vals = [line.split(" ") for line in lines]

#part 1
cards = ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]
cards, card_ranking = prepare_cards(cards)
hand_count = list(map(lambda val: count_cards(val,cards), vals))
calculate_score(hand_count)

#part 2
cards = ['A', 'K', 'Q', 'T', 9, 8, 7, 6, 5, 4, 3, 2,'J']
cards, card_ranking = prepare_cards(cards)
hand_count = list(map(lambda val: count_cards(val,cards), vals))
hand_count = [apply_wildcard(hand) for hand in hand_count]
calculate_score(hand_count)
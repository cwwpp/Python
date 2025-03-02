import random
from itertools import combinations

# Define ranks and suits
ranks = "23456789TJQKA"
suits = "CDHS"
deck = [r + s for r in ranks for s in suits]

def evaluate_hand(hand):
    """A simplified hand evaluation function."""
    rank_counts = {r: sum(1 for card in hand if card[0] == r) for r in ranks}
    sorted_counts = sorted(rank_counts.values(), reverse=True)
    if sorted_counts[0] == 4:
        return 7  # Four of a Kind
    if sorted_counts[0] == 3 and sorted_counts[1] == 2:
        return 6  # Full House
    if sorted_counts[0] == 3:
        return 3  # Three of a Kind
    if sorted_counts[0] == 2 and sorted_counts[1] == 2:
        return 2  # Two Pair
    if sorted_counts[0] == 2:
        return 1  # One Pair
    return 0  # High Card

def simulate_poker_odds(hole_cards, community_cards, num_simulations=10000):
    """Simulates poker games to estimate win probability."""
    remaining_deck = [card for card in deck if card not in hole_cards + community_cards]
    opponents = 1  # Adjust for more players if needed

    win_count = 0
    tie_count = 0
    lose_count = 0

    for _ in range(num_simulations):
        random.shuffle(remaining_deck)
        remaining_community = community_cards + remaining_deck[:5 - len(community_cards)]
        opponent_hands = [remaining_deck[5 + i * 2:7 + i * 2] for i in range(opponents)]
        my_hand_strength = evaluate_hand(hole_cards + remaining_community)
        opponent_strengths = [evaluate_hand(hand + remaining_community) for hand in opponent_hands]

        if my_hand_strength > max(opponent_strengths):
            win_count += 1
        elif my_hand_strength == max(opponent_strengths):
            tie_count += 1
        else:
            lose_count += 1

    total = win_count + tie_count + lose_count
    return {
        "win": win_count / total,
        "tie": tie_count / total,
        "lose": lose_count / total
    }

hole_cards = []
community_cards = []

for i in range(1,3):
    card = input(f"Enter card no{i}: ")
    hole_cards.append(card)

odds = simulate_poker_odds(hole_cards, community_cards)
print(f"Win: {odds['win']:.2%}, Tie: {odds['tie']:.2%}, Lose: {odds['lose']:.2%}")

def com_cards(hole_cards, community_cards):
    for i in range(5):
        card = input("Community card: ")
        community_cards.append(card)
        odds = simulate_poker_odds(hole_cards, community_cards)
        print(f"Win: {odds['win']:.2%}, Tie: {odds['tie']:.2%}, Lose: {odds['lose']:.2%}")

com_cards(hole_cards)

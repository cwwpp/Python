import tkinter as tk
from tkinter import messagebox
import random
from collections import Counter

# Define ranks and suits
ranks = "23456789TJQKA"
suits = "CDHS"
deck = {r + s for r in ranks for s in suits}
rank_values = {rank: i for i, rank in enumerate(ranks)}

def is_straight(hand_ranks):
    """Checks if the given hand ranks form a straight."""
    unique_ranks = sorted(set(hand_ranks), key=lambda r: rank_values[r])
    for i in range(len(unique_ranks) - 4):
        if all(rank_values[unique_ranks[i + j]] == rank_values[unique_ranks[i]] + j for j in range(5)):
            return True, f"Straight ({unique_ranks[i]} to {unique_ranks[i + 4]})"
    return False, ""

def is_flush(hand):
    """Checks if the given hand forms a flush."""
    suits = [card[1] for card in hand]
    suit_counts = Counter(suits)
    for suit, count in suit_counts.items():
        if count >= 5:
            return True, f"Flush ({suit})"
    return False, ""

def is_royal_flush(hand):
    """Checks if the given hand forms a royal flush."""
    hand_ranks = sorted([card[0] for card in hand], key=lambda r: rank_values[r], reverse=True)
    straight, straight_desc = is_straight(hand_ranks)
    flush, flush_desc = is_flush(hand)
    if straight and flush and set(hand_ranks[-5:]) == {"T", "J", "Q", "K", "A"}:
        return True, "Royal Flush!"
    return False, ""

def evaluate_hand(hand):
    """Evaluates a poker hand and returns ranking and description."""
    hand_ranks = sorted([card[0] for card in hand], key=lambda r: rank_values[r], reverse=True)
    rank_counts = Counter(hand_ranks)
    sorted_counts = sorted(rank_counts.items(), key=lambda x: (-x[1], -rank_values[x[0]]))
    
    royal_flush, royal_flush_desc = is_royal_flush(hand)
    if royal_flush:
        return (9, royal_flush_desc)
    
    flush, flush_desc = is_flush(hand)
    straight, straight_desc = is_straight(hand_ranks)
    if flush and straight:
        return (8, f"Straight Flush ({straight_desc})")
    if sorted_counts[0][1] == 4:
        return (7, f"Four of a Kind ({sorted_counts[0][0]})")
    if sorted_counts[0][1] == 3 and sorted_counts[1][1] == 2:
        return (6, f"Full House ({sorted_counts[0][0]} over {sorted_counts[1][0]})")
    if flush:
        return (5, flush_desc)
    if straight:
        return (4, straight_desc)
    if sorted_counts[0][1] == 3:
        return (3, f"Three of a Kind ({sorted_counts[0][0]})")
    if sorted_counts[0][1] == 2 and sorted_counts[1][1] == 2:
        return (2, f"Two Pair ({sorted_counts[0][0]} and {sorted_counts[1][0]})")
    if sorted_counts[0][1] == 2:
        return (1, f"One Pair ({sorted_counts[0][0]})")
    return (0, f"High Card ({sorted_counts[0][0]})")

def validate_cards(card_input):
    """Validates card input format and checks for duplicates."""
    cards = card_input.upper().split()
    if any(card not in deck for card in cards):
        return None
    return cards

def get_suggestion(win_rate):
    """Provides a suggestion based on win percentage."""
    if win_rate > 0.5:
        return "Strong hand! You should consider playing."
    elif win_rate > 0.3:
        return "Decent hand, but be cautious."
    else:
        return "Weak hand. You might want to fold."

def simulate_odds():
    """Simulates poker odds based on user input."""
    hole_cards = validate_cards(hole_cards_entry.get())
    community_cards = validate_cards(community_cards_entry.get())
    try:
        num_opponents = int(opponents_entry.get())
        if num_opponents < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid number of opponents. Enter a positive integer.")
        return
    
    if hole_cards is None or len(hole_cards) != 2:
        messagebox.showerror("Error", "Invalid hole cards entered. Format: '7c 5h'")
        return
    if community_cards is None or len(community_cards) > 5:
        messagebox.showerror("Error", "Invalid community cards entered. Max 5 cards.")
        return
    
    remaining_deck = list(deck - set(hole_cards + community_cards))
    wins, ties, losses = 0, 0, 0
    num_simulations = 1000
    simulated_flops = []
    
    for _ in range(num_simulations):
        random.shuffle(remaining_deck)
        full_community = community_cards + remaining_deck[:5 - len(community_cards)]
        my_strength, my_desc = evaluate_hand(hole_cards + full_community)
        opponent_hands = [remaining_deck[5 + i * 2:7 + i * 2] for i in range(num_opponents)]
        best_opponent_strength, _ = max((evaluate_hand(hand + full_community) for hand in opponent_hands), key=lambda x: x[0])
        
        if my_strength > best_opponent_strength:
            wins += 1
            outcome = "Win"
        elif my_strength == best_opponent_strength:
            ties += 1
            outcome = "Tie"
        else:
            losses += 1
            outcome = "Lose"
        
        simulated_flops.append(f"{' '.join(full_community)} - {outcome} ({my_desc})")
    
    total = wins + ties + losses
    win_rate = wins / total
    suggestion = get_suggestion(win_rate)
    
    result_text.set(
        f"\nWin: {win_rate:.2%}\n"
        f"Tie: {ties/total:.2%}\n"
        f"Lose: {losses/total:.2%}\n"
        f"\n★ Hand Evaluation ★\n{my_desc}\n"
        f"\n★ Suggestion ★\n{suggestion}\n"
        f"\nSample Simulated Flops:\n" + "\n".join(simulated_flops[:5])
    )

def clear():
    """Clears the hole cards and community cards fields."""
    hole_cards_entry.delete(0, tk.END)
    community_cards_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Poker Odds Calculator")
root.geometry("600x600")
root.configure(bg="#2C3E50")

title_label = tk.Label(root, text="Poker Odds Calculator", font=("Arial", 16, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#34495E")
frame.pack(pady=10, padx=10, fill="both", expand=True)

tk.Label(frame, text="Hole Cards:", bg="#34495E", fg="white").grid(row=0, column=0)
hole_cards_entry = tk.Entry(frame)
hole_cards_entry.grid(row=0, column=1)

tk.Label(frame, text="Community Cards:", bg="#34495E", fg="white").grid(row=1, column=0)
community_cards_entry = tk.Entry(frame)
community_cards_entry.grid(row=1, column=1)

tk.Label(frame, text="Number of Opponents:", bg="#34495E", fg="white").grid(row=2, column=0)
opponents_entry = tk.Entry(frame)
opponents_entry.grid(row=2, column=1)

calculate_button = tk.Button(frame, text="Calculate Odds", command=simulate_odds, bg="#E74C3C", fg="white", font=("Arial", 12, "bold"))
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

clear_button = tk.Button(frame, text="Clear", command=clear, bg="#3498DB", fg="white", font=("Arial", 12, "bold"))
clear_button.grid(row=4, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_text, justify="left", bg="#34495E", fg="white", font=("Arial", 10))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

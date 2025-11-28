import random

with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = [q.strip() for q in f.readlines() if q.strip()]

print(random.choice(quotes))

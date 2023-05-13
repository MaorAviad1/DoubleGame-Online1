import random

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def play_card(self):
        return self.cards.pop(0)

class Card:
    def __init__(self, images):
        self.images = images

def find_common_image(card1, card2):
    return list(set(card1.images) & set(card2.images))

# Define images
all_images = ['cow', 'bike', 'plate', 'phone', 'dog', 'cloud', 'grass', 'book', 'lollipop', 'potato', 'window', 'cat', 'bat', 'notebook', 'bed'] # add more images to make it 33

# Create players
player1 = Player("User1")
player2 = Player("User2")

# Assign cards to players
for i in range(27):
    random.shuffle(all_images)
    player1.add_card(Card(all_images[:8]))
    player2.add_card(Card(all_images[8:16]))

# Game loop
for round in range(27):
    card1 = player1.play_card()
    card2 = player2.play_card()
    common_images = find_common_image(card1, card2)
    if common_images:
        print(f"Round {round+1}: {player1.name} and {player2.name} have common image(s): {common_images[0]}")
    else:
        print(f"Round {round+1}: No common images")

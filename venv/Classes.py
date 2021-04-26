from Cards import new_card


class Card:

####accept card as the input and iterate through the index [0 for level, 1 for top, etc]
    def __init__(self, new_card):
        self.new_card = new_card[0]
        self.rank = new_card[1][0]
        self.top = new_card[1][1]
        self.right = new_card[1][2]
        self.bottom = new_card[1][3]
        self.left = new_card[1][4]

    def show(self):
        if self.rank <= 5:
            print(f'You have randomly chosen a {self.new_card}. A Level {self.rank} card.')
        elif self.rank >= 6 and self.rank <= 7:
            print(f'You have randomly chosen a {self.new_card}. A Level {self.rank} Boss card.')
        elif self.rank >= 8 and self.rank <= 9:
            print(f'You have randomly chosen a {self.new_card}. A Level {self.rank} GF card.')
        elif self.rank == 10:
            print(f'You have randomly chosen a {self.new_card}. A Level {self.rank} Player card.')

class Deck:

    def __init__(self):
        pass

class Player:

    def __init__(self):
        pass

card = Card(new_card())

card.show()
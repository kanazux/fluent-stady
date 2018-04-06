import collections


card = collections.namedtuple('card', ['rank', 'suit'])


class BaralhoFrances:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'espadas ouro copas paus'.split()

    def __init__(self):
        self.cards = [card(rank, suit) for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, posicao):
        return self.cards[posicao]

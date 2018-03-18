import unittest
from random import shuffle

SUITS = ['♠', '♣', '♦', '♥']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Card:
  def __init__(self, suit: int, rank: int):
    if suit < 0 or suit >= len(SUITS):
      raise ValueError('suit must be >=0 and <= 3')
    elif rank < 0 or rank >= len(RANKS):
      raise ValueError('rank must be >=0 and <= 12')

    self.suit = suit
    self.rank = rank

  def __str__(self):
    return SUITS[self.suit] + RANKS[self.rank]

class Deck:
  def __init__(self, decks: int = 1):
    self._cards = []

    for suit in range(len(SUITS)):
      for rank in range(len(RANKS)):
        card = Card(suit, rank)
        for i in range(decks):
          self._cards.append(card)

    self.shuffle()

  def __len__(self):
    return len(self._cards)

  def shuffle(self):
    shuffle(self._cards)

  def draw(self):
    if len(self._cards) == 0:
      return None
    return self._cards.pop()

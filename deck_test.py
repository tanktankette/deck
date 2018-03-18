import unittest
from deck import Card, Deck

class TestCard(unittest.TestCase):
  def testExceptions(self):
    with self.assertRaises(ValueError):
      Card(-1, 0)
    with self.assertRaises(ValueError):
      Card(6, 0)
    with self.assertRaises(ValueError):
      Card(0, -1)
    with self.assertRaises(ValueError):
      Card(0, 13)

  def testStr(self):
    card = Card(0,2)
    self.assertEqual(str(card), '♠3')

class TestDeck(unittest.TestCase):
  def test(self):
    deck = Deck()
    self.assertEqual(len(deck), 52)

    drawn_cards = []
    for i in range(52):
      card = deck.draw()
      self.assertEqual(type(card), Card)
      self.assertTrue(str(card) not in drawn_cards)
      drawn_cards.append(str(card))

    self.assertEqual(deck.draw(), None)
import unittest
import numpy as np


class Deck:
    def __init__(self, initial_size=0):
        self.cards = ([i for i in range(53)] + [0]) * initial_size
        self.scramble()

    def scramble(self):
        self.cards = list(np.random.permutation(self.cards))

    def put_card(self, card):
        self.cards.append(card)

    def get_card(self):
        return self.cards.pop()


class MyTestCase(unittest.TestCase):
    def test_new_deck_is_empty(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 0)

    def test_new_deck_has_cards(self):
        deck = Deck(1)
        self.assertEqual(len(deck.cards), 54)

    def test_get_card_decreases_cards(self):
        deck = Deck(1)
        self.assertEqual(len(deck.cards), 54)
        card = deck.get_card()
        self.assertEqual(len(deck.cards), 53)

    def test_deck_contains_correct_cards(self):
        deck = Deck(1)
        expected_cards = [i for i in range(53)] + [0]

        self.assertCountEqual(deck.cards, expected_cards)
        deck = Deck(2)

    def test_put_card_puts_it_on_top(self):
        deck = Deck()
        deck.put_card(1)
        deck.put_card(2)
        self.assertEqual(deck.cards[-1], 2)
        self.assertEqual(len(deck.cards), 2);

    def test_get_card_returns_last_card(self):
        deck = Deck()
        deck.put_card(1)
        deck.put_card(2)
        self.assertEqual(deck.get_card(), 2)


if __name__ == '__main__':
    unittest.main()

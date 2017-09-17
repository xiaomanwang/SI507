import unittest
from SI507F17_project1_cards import *
from helper_functions import *


class CardTest(unittest.TestCase):
    def test_stringtype(self):
        card = Card()
        self.assertEqual(type(card.suit), type('aabbcc'),
        'Testing if the variable suit is a string type')   # 'aabbcc' is a str

    def test_ranktype(self):
        card = Card()
        AcetoKing = ['Ace', 'Jack', 'Queen', 'King'] + list(range(2, 11))
        # create a list which contain the four strings and nmubers form 2 to 10
        self.assertIn(card.rank, AcetoKing)
        # Testing if the variable rank holds EITHER the number or the string
        # representation as appropriate of the card rank

    def test_rank_num(self):
        card = Card()
        Numlist = list(range(1, 14))
        self.assertIn(card.rank_num, Numlist)  # Testing if rank_num is an int

    def test_print(self):
        card = Card(0, 1)
        self.assertEqual(card.__str__(), 'Ace of Diamonds')
        # Testing if string method return a proper string
# THE FIRST BUG


class DeckTest(unittest.TestCase):
    def test_Allcrads(self):  # Testing if the constructor builds a list of cards
        deck = Deck()
        All = [(x, y) for x in ['Diamonds', 'Clubs', 'Hearts', 'Spades'] for y in range(1, 14)]
        for card in deck.cards:
            self.assertIn((card.suit, card.rank_num), All)
            All.remove((card.suit, card.rank_num))

    def test_deckprint(self):  # Testing if the Deck string method return a multi-line string
        deck = Deck()
        A = ''
        for card in deck.cards:
            A += str(card.rank) + ' of ' + card.suit
            A += '\n'
        self.assertEqual(deck.__str__(), A)
# BUG. But it is the same type as the first one.

    def test_popcard(self):
        deck = Deck()
        for i in range(52):  # pop off 52 times to test if the left is empty
            deck.pop_card()
        self.assertEqual(deck.cards, [])

    def test_shuffle(self):
        deck = Deck()
        listofCard = [str(card) for card in deck.cards]
        deck.shuffle()
        listofCardAfterShuffling = [str(card) for card in deck.cards]
        # the list that after shuffling
        self.assertNotEqual(listofCard, listofCardAfterShuffling)
        # Testing if shuffle method gives a different list
        self.assertEqual(len(listofCard), len(listofCardAfterShuffling))
        # Testing if shuffle method do not change the size of the list

    def test_replacecard(self):
        deck = Deck()
        Lastcard = deck.pop_card()  # pop off the last card
        deck.replace_card(Lastcard)  # add the card we just pop off
        self.assertIn(Lastcard, deck.cards)
        # Testing if the card we pop off and add again is in the deck
        self.assertEqual(len(deck.cards), 52)
        # Testing whether the deck length is unaltered after popping off and replacing
        deck.replace_card(Lastcard)
        # Replace_card which the card instance input is already in the deck
        self.assertEqual(len(deck.cards), 52)
        # Testing whether the deck length is unaltered

    def test_sortcard(self):
        deck = Deck()
        # step one: Testing whether the two different decks have the same order after sorting
        deckoriginal = Deck()
        deck.shuffle()
        deck.sort_cards()
        self.assertEqual(str(deck), str(deckoriginal))
        # step two: After popping off, testing whether the remaining two different decks have the same order after sorting
        deck = Deck()
        deck.pop_card()
        deckoriginal = Deck()
        deckoriginal.pop_card()
        deck.shuffle()
        deck.sort_cards()
        self.assertEqual(str(deck), str(deckoriginal))
# THE SECOND BUG

    def test_deal_hand(self):
        deck = Deck()
        try:
            deck.deal_hand(52)
            self.assertEqual(len(deck.cards), 0)  # error, another bug
        except:
            self.assertEqual(1, 0)
            # If deal_hand has bugs, the except code will run, the test will fail
# THE THIRD BUG


class Test_play_war_game(unittest.TestCase):
    def test_output(self):
        self.assertIsInstance(play_war_game(testing=False), tuple)
        # Testing if the output is a tuple
        ListofOutputone = ['Player1', 'Player2', 'Tie']
        self.assertIn(play_war_game(testing=False)[0], ListofOutputone)
        # Testing if the output tuple contains a string and two integers
        self.assertIsInstance(play_war_game(testing=False)[1], int)
        self.assertIsInstance(play_war_game(testing=False)[2], int)


class Test_function_show_song(unittest.TestCase):
    def test_show_song(self):
        s = show_song()
        self.assertIsInstance(s, Song)
        self.assertTrue(isinstance(s, Song))
        # Testing if it returns a single instance of class Song
        s2 = show_song('Winner')
        print(s2)
        self.assertTrue('Winner' in str(s2))
        # Testing if the output have the input keyword

if __name__ == '__main__':
    unittest.main(verbosity=2)
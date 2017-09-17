# There are four files in project 1.
Code_description is the description of code SI507F17_project1_cards.py. It shows that what the code is supposed to do and the expected output of the code.
SI507F17_project1_cards.py is the code which contains four parts: Card class, Deck class, play_the_war function and show_song function.
helper_functions.py is some functions that will be used in the show_song function in SI507F17_project1_cards.py.
SI507F17_project1_tests.py  is used to test whether SI507F17_project1_cards.py is the correct code that match the Code_description.After testing, there exist four bugs:
The first one is in test_print (__main__.CardTest) . The supposed output is ‘Ace of Diamonds’ while the real output is ‘1 of Diamonds’. Test_deckprint (__main__.DeckTest) also fail because of this kind of bug.
The second bug is in test_sortcard (__main__.DeckTest). If some card is been posed off, sort function should sort the remaining deck. However, it returns a deck with 52 cards which is contradict to what the description say.
The third bug is in test_deal_hand (__main__.DeckTest). When asked to deal 52 cards, it shows error. 
The 4th bug is in test_show_song (__main__.Test_function_show_song). When we input ‘Winner’, it returns I'M YOUNG but not a string contains ‘Winner’.

# Rummy
Rummy Game using pygame library in Python3

## Rules:

### 2Players:
* 1st User
* 2nd Computer

### 10 cards for each player

#### A run:

* 3 or more cards of the same suit in consecutive order
* valid order A-2-3-4-5-6-7-8-9-10-J-Q-K-A
(you cannot form K-A-2)

#### A set:

* 3 or 4 cards of same rank but of different suit
* like 9heart-9spade-9-diamond

### To Begin:

Top card of the stock pile is placed face up in the dicard pile

### Objective:

* To be the first player to place all his cards into melds(a run or a set) by forming one quad and 2 triplets.
* Each player turn by turn deals the cards.
* You need to form runs(or sequences) and sets
* When a player has required runs and sets he declares his turn.
* The player picks either top face up card of discard pile or the top face down card of stock pile.
and discards the least important card in the discard pile
* Game ends when player melds all cards or discards last card

#### Description of GUI:

* A new screen opens and rummy sound plays in the beginning with title, icon and background
* The bottom cards belong to the user while the top cards belong to the computer.
* Left cards which are reverse belong to the pile and the card in the middle belong to the discarded cards which are again moved back to the the pile. The user can either pick the stock card or the discarded card by clicking on it.
* Once the user forms a quad or a triplet ,it moves to right .The user can form 2 triplets and 1 quad and can end the game by discarding the last card

#### Variation: Pool Rummy: 

from random import shuffle
values = {"duggi" : 2,"tiggi":3,"chowki" : 4,"panji" : 5,"chakki" : 6,"satti":7,"athi" : 8,"nhela" : 9,"dhela" : 10, "gulam" : 11,"begam" : 12,"badshah" : 13,"ikka" : 14}
ranks=("duggi","tiggi","chowki","panji","chakki","satti","athi","nhela","dhela", "gulam","begam","badshah","ikka")
suits = ["eeth","chidi","paan","hukum"]


class Card():
    #Card class which will create all card
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value = values[rank]
    def __str__(self) :
        if(self.rank=="ikka"):
            return self.suit + " ka "+self.rank
        else:
            return self.suit + " ki "+self.rank
    def printcard(self):
        if(self.rank=="ikka"):
            return self.suit + " ka "+self.rank
        else:
            return self.suit + " ki "+self.rank
    def printcard(self):
            print("{} ki {}".format(self.suit,self.rank))

class Deck():
    # This class will create deck from all cards
    def __init__(self):
        self.all_cards=[]
        #this for loop will create all cards
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
        self.shuffle()
    def shuffle(self):
        shuffle(self.all_cards)
        #this will shuffle all card randomly
    def pick_one(self):
        return self.all_cards.pop()

class Player():
    # This class whill define player and no of cards
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        return self.all_cards.pop(0)# this will remove top card 
    def add_cards(self,new_cards):
        #this will insert card or cards  at the bottom if user give list of cards then it will extend the all card list if user give single card then it will add that in last
        if(type(new_cards)==type([])):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)}'


def intro():
# This function introduces the rules of the game Tic Tac Toe
    print("Hello! Welcome to Sam's Card war Game !")
    print("\n")
    print("Rules: Player 1 and player 2, have equal number of cards . \n  Both the person will draw one one card  "
          "Person with bigger card value will take both his and oppenat card and put them in his deck \n"
          "Person with all 52 cards win the Game .\n"
          "TRY YOR LUCK !!!! ")
    print("\n")
    input("Press enter to continue.")
    print("\n")

def Player_info(new_deck):
    player1_name=input("Enter player 1 name: ")
    player2_name=input("Enter player 2 name: ")
    input("Press enter to continue.")
    player1=Player(player1_name)
    player2=Player(player2_name)
    #shuffling and distributing card to both 
    input("Press enter to distribute card .")
    for card_object in range(0,26):
        player1.add_cards(new_deck.pick_one())
        player2.add_cards(new_deck.pick_one())
    
    input("Cards are distibuted press enter to start a game.")
    

    return player1,player2


def startgame(player1,player2):
    round_num = 0
    game_on=True
    card_on_table=[]
    while game_on: 
        round_num += 1
        print(f"Round {round_num}")
        # Check to see if a player is out of cards:
        if len(player1.all_cards) == 0:
            print("Player One out of cards! Game Over")
            print("Player Two Wins!")
            game_on = False
            break
            
        if len(player2.all_cards) == 0:
            print("Player Two out of cards! Game Over")
            print("Player One Wins!")
            game_on = False
            break
        card_on_table.append(player1.remove_one())
        card_on_table.append(player2.remove_one())
        if card_on_table[-2].value > card_on_table[-1].value:
            print(f"{card_on_table[-2]} > {card_on_table[-1]} Player 1 won")
            player1.add_cards(card_on_table)
            card_on_table=[]
        elif card_on_table[-2].value < card_on_table[-1].value:
            print(f"{card_on_table[-1]} > {card_on_table[-2]} Player 2 won")
            player2.add_cards(card_on_table)
            card_on_table=[]
        elif card_on_table[-2].value == card_on_table[-1].value:
            print(f"{card_on_table[-1]} == {card_on_table[-2]} Tie")
            if(len(player1.all_cards)<5):
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break
            elif(len(player2.all_cards)<5):
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            else:
                for num in range(5):
                    card_on_table.append(player1.remove_one())
                    card_on_table.append(player2.remove_one())
   

if __name__ == "__main__":
# The main function
    intro()
    new_deck=Deck()#created a new deck
    player1,player2=Player_info(new_deck)
    startgame(player1,player2) # The function that starts the game.





#----------------------------------------------------------
#extra
# for card_object in new_deck.all_cards:
#     print(card_object)
# print(new_deck.pick_one())
# print(len(new_deck.all_cards))
# player1.add_cards(new_deck.all_cards)
# print(player1)

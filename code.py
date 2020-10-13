import pygame
import random
import time

#initialize pygame
pygame.init()

#creating screen
screen = pygame.display.set_mode((1200,650))

#Title and icon
pygame.display.set_caption('Rummy')
icon = pygame.image.load('images/rum1.jpg')
pygame.display.set_icon(icon)

#Background
Background = pygame.image.load('images/im1.jpg')

#sound
pygame.mixer.music.load('Intro.mp3')
pygame.mixer.music.play(0)

#Reverse card
cardBack = pygame.image.load('images/back.png')
cardBackX = 75
cardBackY = 225
cardBackX_change = 0
cardBackY_change = 0

#win
win=pygame.image.load('images/win1.jpg')

#lose
lose=pygame.image.load('images/lose.png')

#Clubs
club=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
club[1]= pygame.image.load('images/club ace.png')
club[2] = pygame.image.load('images/club 2.png')
club[3] = pygame.image.load('images/club 3.png')
club[4] = pygame.image.load('images/club 4.png')
club[5] = pygame.image.load('images/club 5.png')
club[6] = pygame.image.load('images/club 6.png')
club[7] = pygame.image.load('images/club 7.png')
club[8] = pygame.image.load('images/club 8.png')
club[9] = pygame.image.load('images/club 9.png')
club[10] = pygame.image.load('images/club 10.png')
club[11] = pygame.image.load('images/club J.png')
club[12]= pygame.image.load('images/club Q.png')
club[13] = pygame.image.load('images/club K.png')

#Diamonds
diamond=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
diamond[1] = pygame.image.load('images/diamond ace.png')
diamond[2] = pygame.image.load('images/diamond 2.png')
diamond[3] = pygame.image.load('images/diamond 3.png')
diamond[4] = pygame.image.load('images/diamond 4.png')
diamond[5] = pygame.image.load('images/diamond 5.png')
diamond[6] = pygame.image.load('images/diamond 6.png')
diamond[7] = pygame.image.load('images/diamond 7.png')
diamond[8] = pygame.image.load('images/diamond 8.png')
diamond[9] = pygame.image.load('images/diamond 9.png')
diamond[10] = pygame.image.load('images/diamond 10.png')
diamond[11] = pygame.image.load('images/diamond J.png')
diamond[12] = pygame.image.load('images/diamond Q.png')
diamond[13] = pygame.image.load('images/diamond K.png')

#Hearts
heart =[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
heart[1] = pygame.image.load('images/heart ace.png')
heart[2] = pygame.image.load('images/heart 2.png')
heart[3] = pygame.image.load('images/heart 3.png')
heart[4] = pygame.image.load('images/heart 4.png')
heart[5] = pygame.image.load('images/heart 5.png')
heart[6] = pygame.image.load('images/heart 6.png')
heart[7] = pygame.image.load('images/heart 7.png')
heart[8] = pygame.image.load('images/heart 8.png')
heart[9] = pygame.image.load('images/heart 9.png')
heart[10] = pygame.image.load('images/heart 10.png')
heart[11] = pygame.image.load('images/heart J.png')
heart[12] = pygame.image.load('images/heart Q.png')
heart[13] = pygame.image.load('images/heart K.png')

#Spades
spade = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
spade[1] = pygame.image.load('images/spade ace.png')
spade[2] = pygame.image.load('images/spade 2.png')
spade[3] = pygame.image.load('images/spade 3.png')
spade[4] = pygame.image.load('images/spade 4.png')
spade[5] = pygame.image.load('images/spade 5.png')
spade[6] = pygame.image.load('images/spade 6.png')
spade[7] = pygame.image.load('images/spade 7.png')
spade[8] = pygame.image.load('images/spade 8.png')
spade[9] = pygame.image.load('images/spade 9.png')
spade[10] = pygame.image.load('images/spade 10.png')
spade[11] = pygame.image.load('images/spade J.png')
spade[12] = pygame.image.load('images/spade Q.png')
spade[13] = pygame.image.load('images/spade K.png')

card=[club,diamond,heart,spade] #array of 52 cards

def card1(card,x,y):        #for displaying cards on the screen at x,y top left coordinates
    screen.blit(card,(x,y)) #blit means draw

startCards=[] #card array at the bottom
startCards1=[] #card array at the top
requiredPairs=[] #for forming quads and triplets

#for forming possible quads and tripplets
for j in range(1,14):
    requiredPairs.append([[0,j],[1,j],[2,j],[3,j]])
    requiredPairs.append([[0,j],[1,j],[2,j]])
    requiredPairs.append([[0,j],[1,j],[3,j]])
    requiredPairs.append([[0,j],[2,j],[3,j]])
    requiredPairs.append([[1,j],[2,j],[3,j]])
for i in range(4):
    for j in range(1,12):
        requiredPairs.append([[i,j],[i,j+1],[i,j+2]])
for i in range(4):
    requiredPairs.append([[i,0],[i,12],[i,13]])
for i in range(4):
    for j in range(1,11):
        requiredPairs.append([[i,j],[i,j+1],[i,j+2],[i,j+3]])
for i in range(4):
    requiredPairs.append([[i,0],[i,11],[i,12],[i,13]])

#to check if arr2 is a subset of arr1
def isSubset(arr1,arr2):
    if(len(arr2)<3):
        return False
    for i in arr2:
        if(i not in arr1):
            return False
    return True

flag=False
var=0
#for discarding cards
def addCards(x5,x6,y5,y6,m):
    global flag
    global var
    if x5<=pygame.mouse.get_pos()[0]<=x6 and y5<=pygame.mouse.get_pos()[1]<=y6: #to get mouse positions
        if len(startCards)==l+1: #to delete card only when extra card is present(card removed only after picking a card from the pile)
            x10=startCards[m][0] 
            y10=startCards[m][1]
            startCards.pop(m)   #deletes the card from startCards
            flag=True           #for displaying discarded card
            var=1               #computer's turn
            return x10,y10      #returning index of the removed card in card array
    return -1,-1


def check(arr,point):
    for i in arr:
        for j in i:
            if point==j:
                return False
    return True

#initializing
x2,y2=1,1
x3,y3=1,1
#initially 10 cards for both players
l=10
l2=10
p=0
p2=0
prev=0
#counting quads and triplets in startCards
four =0
three=0
#counting quads and triplets in startCards1
four1 =0
three1=0
#array of formed quads and triplets
arr=[]

#Game loop
run = True
while run:
    #RGB color
    screen.fill((0,128,0))
    #background
    screen.blit(Background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:    #so that screen doesn't close
            run = False

    if var==0: #user's turn 
        while len(startCards)<l: #for adding 10 cards
            while p<l: 
                x=random.randint(0,3)
                y=random.randint(1,13)
                if [x,y] not in startCards and check(arr,[x,y])==True:
                    startCards.append([x,y]) #for adding random cards in the begining
                    p+=1

        if event.type == pygame.MOUSEBUTTONDOWN: #on clicking
            if 75<=pygame.mouse.get_pos()[0]<=175 and 225<=pygame.mouse.get_pos()[1]<=375: #if position of mouse is between these coordinates
                x2=random.randint(0,3)  #for left pile
                y2=random.randint(1,13)
            elif 200<=pygame.mouse.get_pos()[0]<=300 and 200<=pygame.mouse.get_pos()[1]<=350:
                x2=x3                   #for discarded pile in the middle
                y2=y3
                x3=prev[0]              #if a card is picked from dicarded pile the card
                y3=prev[1]              # which was discarded just before by the player should be visible
            if [x2,y2] not in startCards+startCards1 and check(arr,[x2,y2])==True and len(startCards)<l+1:
                startCards.append([x2,y2]) #for adding random cards by clicking on the deck(to pick a card)
            mouseX=pygame.mouse.get_pos()[0] #x coordinate of mouse
            c=(mouseX-100)//30 #for chosing the card to be discarded
            if c<=l:
                a,b=addCards(100+(30*c),130+(30*c),425,575,c) #for discarding a card from the player's cards
                if a*b!=1: #for invalid click -1,-1 is returned(-1*-1=1)
                    prev=[x3,y3] #value of x3,y3 stored in prev before it is changed in the next line
                    x3=a #index of deleted cards (from startCards) in card array 
                    y3=b
        startCards.sort() #for sorting in the order club-diamond-heart-spade
        sorted(startCards,key=lambda k: [k[1], k[0]]) #for sorting in order ace-1-2-3-4-5-6-7-8-9-10-J-Q-K
        for i in range(l2):                 #l2 is length of computer's cards array
            card1(cardBack,200+(30*i),25)  #for displaying top cards in the beginning               
        card1(cardBack,cardBackX,cardBackY) #for dispalying the deck(left)
        if flag:
            card1(card[x3][y3],200,200) #in first run flag is False,set to True in addCards function
                                        #deleted card displayed in the middle discarded pile
        for i in range(len(startCards)):
            x1=startCards[i][0]
            y1=startCards[i][1]
            card1(card[x1][y1],100+(30*i),425) #for displaying the bottom cards 
    #---------------------------------------------------------------------------------------------------------    
    elif var==1:                        #computer's turn 
        var=0                           #resets value for next run  
        while(len(startCards1)<l2):                     #initialises array for each run
            x=random.randint(0,3)
            y=random.randint(1,13)
            if([x,y] not in startCards+startCards1 and check(arr,[x,y])):
                startCards1.append([x,y])               #array of computer's cards
        time.sleep(0.5)                                 #for adding delay of 0.5 seconds
        x,y=random.randint(0,3),random.randint(1,13)            
        if([x,y]) not in startCards+startCards1 and check(arr,[x,y]):            
            startCards1.append([x,y])                   #picking card from deck for computer
        startCards1.sort()                              #for sorting in the order club-diamond-heart-spade
        sorted(startCards1,key=lambda k: [k[1],k[0]])   #for sorting in order ace-1-2-3-4-5-6-7-8-9-10-J-Q-K
        time.sleep(0.5)                                 #adds delay of 0.5s
        index=random.randint(0,l2-1)                    #selecting the card to be removed
        card10=startCards1.pop(index)                   #removing the selected card
        x3=card10[0]                                    #index of 
        y3=card10[1]                                    #removed card
        for i in range(l2):                             #l2 is length of computer's cards array
            card1(cardBack,200+(30*i),25)               #printing the opponent's cards  
        card1(card[x3][y3],200,200)                     #sending card to discarded deck
    #------------------------------------------------------------------------------------------------------
    tr1=0
    for i in arr:
        flag1=0
        for j in i:
            card1(j,600+(30*flag1),50+(155*tr1)) #for displaying top right cards(quads and triplets formed)
            flag1+=1                             #for increasing the x coordinate
        tr1+=1                                   #for increasing y for the next quad/triplet formed
    for i in requiredPairs: 
            a=isSubset(startCards,i) #to check if a quad/triplet is present in startCards
            if a:
                if len(i)==4:
                    if four<1:       #only 1 quad can be formed(see rules)
                        l-=4         #decreasing the length by 4(as quad formed)
                        four+=1      #after 1 quad formed
                        ar=[]        #array of the 4 cards 
                        for j in i:
                            x4=j[0] 
                            y4=j[1]
                            ar.append(card[x4][y4])
                            startCards.remove(j) #removed from startCards
                        arr.append(ar) #array of all quads and triplets formed
                elif(len(i)==3):
                    if(three<2):    #can form only 2 triplets
                        l-=len(i) #reduces the length of startCards by 3
                        three+=1  #to count triplets formed
                        ar=[]      #array of 3 cards
                        for j in i:
                            x4=j[0] 
                            y4=j[1]
                            ar.append(card[x4][y4])
                            startCards.remove(j) #removed from startCards
                        arr.append(ar)
    #---------------------same loop for computer-----------------------------------------------------
    for i in requiredPairs: 
            a=isSubset(startCards1,i) #to check if a quad/triplet is present in startCards1
            if a:
                if len(i)==4:
                    if four1<1:
                        l2-=4
                        four1+=1
                        ar=[]
                        for j in i:
                            x4=j[0] 
                            y4=j[1]
                            ar.append(card[x4][y4])
                            startCards1.remove(j) 
                        arr.append(ar)
                elif(len(i)==3):
                    if(three1<2):
                        l2-=len(i)
                        three1+=1
                        ar=[]
                        for j in i:
                            x4=j[0] 
                            y4=j[1]
                            ar.append(card[x4][y4])
                            startCards1.remove(j) 
                        arr.append(ar)

    #when length of user's cards is one the card is discarded and user wins      
    if len(startCards)==1:
        screen.blit(win,(0,0))  #displays 'YOU WIN' image on the screen
    elif len(startCards1)==1:
        screen.blit(lose,(0,0)) #displays 'YOU LOSE' image on the screen
    #updates the screen
    pygame.display.update()   
#!/usr/bin/env python
# coding: utf-8

# In[29]:


board = ["1","2","3",
         "4","5","6",
         "7","8","9"]


# In[30]:


currentPlayer = "X"


# In[31]:


winner = None


# In[32]:


gameRunning = True


# In[33]:


# printing the game board
def printBoard(board):
    print(f"Game Board \n{board[0]}   {board[1]}   {board[2]}")
    print(f"{board[3]}   {board[4]}   {board[5]}")
    print(f"{board[6]}   {board[7]}   {board[8]}")
    


# In[34]:


numLst = ["1","2","3","4","5","6","7","8","9"]


# In[35]:


# define pkayer input
def playerInput(board):
    inp = input("please choose a number of spot to play....")
    while True:
        if inp in numLst and board[int(inp) -1] in numLst :
            board[int(inp) -1] = currentPlayer
            break

        else :    
            inp = input("wrong input, please choose a number of spot to play....")
            
        


# In[36]:


# define check win or tie
def checkHorizonatle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] not in numLst:
        return True
    elif board[3] == board[4] == board[5] and board[3] not in numLst:
        return True
    elif board[6] == board[7] == board[8] and board[6] not in numLst:
        return True
def checkVirticale(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] not in numLst:
        return True
    elif board[1] == board[4] == board[7] and board[1] not in numLst:
        return True
    elif board[2] == board[5] == board[8] and board[2] not in numLst:
        return True
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] not in numLst:
        return True
    elif board[2] == board[4] == board[6] and board[2] not in numLst:
        return True
def checkTie(board):
    global gameRunning
    if board[0] and board[1] and board[2]and board[3]and board[4]and board[5]and board[6]and board[7]and board[8] not in numLst :
        printBoard(board)
        print("the game is tie")
        gameRunning = False


# In[37]:


def checkWin():
    global gameRunning
    if checkHorizonatle(board) or checkVirticale(board) or checkDiagonal(board) :
        printBoard(board)
        winner = currentPlayer
        print (f"congratulations, the winner is {winner}")
        gameRunning = False
        


# In[38]:


def switchPlayer(board):
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else :
        currentPlayer = "X"
    


# In[39]:


# while loop to run the game
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer(board)


# In[ ]:





# In[ ]:





# In[ ]:





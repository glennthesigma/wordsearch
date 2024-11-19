#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

#WORD RETRIEVAL
wordfile = open("TWL06.txt", "r")
wordlist = []
wordlist = wordfile.readlines()
wordfile.close()

#BOARD
def display(board_arr, filename):
    if filename == None:
        print("    A B C D E F G H I J K L M N O P Q R S T\n")
    else:
        cwfile = open(filename, "w")
        
    rownum = 1
    for row in board_arr:
        
        if filename != None:
            if rownum == 1:
                rownum = 0
            else:
                cwfile.write("")

            
            for char in row:
                cwfile.write(char)
                
        else:
                
            if rownum < 10:
                print(end = "\n" + str(rownum) + "   ")
                rownum += 1

            else:
                print(end = "\n" + str(rownum) + "  ")       
                rownum += 1
                            
            for char in row:
                print(char, end = " ")
                
    if filename != None:
        cwfile.close()
        
def pos_to_index(tuple_pos): #RETURNS INT
    return tuple_pos[0] + 20 * tuple_pos[1]
            
    
board = [[" " for x in range(20)] for y in range(20)]
ans_board = [[" " for x in range(20)] for y in range(20)]

board_empty = True

#HORIZONTAL
class horizontal:
    def __init__(self, word):
        self.word = word
        self.start_pos = None #tuple (x,y,0/1), 1 = reverse
        self.end_pos = None #tuple (x,y)
        self.added = False

    def addword(self):
        global board_empty
            
        if board_empty:
            x_pos = random.randint(0, 19 - len(self.word))
            y_pos = random.randint(0, 19)
            
            if random.randint(0, 1) == 1:
                self.start_pos = (x_pos, y_pos, 1)
                word = self.word[::-1]
                
            else:
                self.start_pos = (x_pos, y_pos, 0)
                word = self.word
            
            for char in word:
                board[y_pos][x_pos] = char
                ans_board[y_pos][x_pos] = char
                x_pos += 1
                
            self.end_pos = (x_pos - 1, y_pos)
            board_empty = False
            self.added = True
                
        else:
            list_of_start_pos = []
            
            for y_pos in range(20):
                for x_pos in range(20 - len(self.word)):
                    xtemp = x_pos
                    valid0 = False
                    valid1 = False
                    
                    for char in self.word:
                        if board[y_pos][xtemp] == " " or board[y_pos][xtemp] == char:
                            if xtemp - x_pos + 1 == len(self.word):
                                valid0 = True
                            else:
                                xtemp += 1
                        
                        else:
                            break
                            
                    word = self.word[::-1]
                    xtemp = x_pos
                    
                    for char in word:
                        if board[y_pos][xtemp] == " " or board[y_pos][xtemp] == char:
                            if xtemp - x_pos + 1 == len(self.word):
                                valid1 = True
                            else:
                                xtemp += 1
                
                        else:
                            break
                    
                    if valid0:
                        list_of_start_pos.append((x_pos, y_pos, 0))
                        
                    if valid1:
                        list_of_start_pos.append((x_pos, y_pos, 1))
                        
            if list_of_start_pos == []:
                pass
            
            else:
                self.start_pos = list_of_start_pos[random.randint(0, len(list_of_start_pos) - 1)]

                x_pos = self.start_pos[0]
                y_pos = self.start_pos[1]

                if self.start_pos[2] == 0:
                    for char in self.word:
                        board[y_pos][x_pos] = char
                        ans_board[y_pos][x_pos] = char
                        x_pos += 1

                else:
                    for char in word:
                        board[y_pos][x_pos] = char
                        ans_board[y_pos][x_pos] = char
                        x_pos += 1
                
                self.end_pos = (x_pos - 1, y_pos)
                self.added = True
                
            
#VERTICAL
class vertical:
    def __init__(self, word):
        self.word = word
        self.start_pos = None #tuple (x,y,0/1), 1 = reverse
        self.end_pos = None #tuple (x,y)
        self.added = False
        
    def addword(self):
        global board_empty
        
        if board_empty:
            x_pos = random.randint(0, 19)
            y_pos = random.randint(0, 20 - len(self.word))
            
            if random.randint(0, 1) == 1:
                self.start_pos = (x_pos, y_pos, 1)
                word = self.word[::-1]
                
            else:
                self.start_pos = (x_pos, y_pos, 0)
                word = self.word
            
            for char in word:
                board[y_pos][x_pos] = char
                ans_board[y_pos][x_pos] = char
                y_pos += 1
             
            self.end_pos = (x_pos, y_pos - 1)
            board_empty = False
            self.added = True
            
        else:
            list_of_start_pos = []
            
            for x_pos in range(20):
                for y_pos in range(20 - len(self.word)):
                    ytemp = y_pos
                    valid0 = False
                    valid1 = False
                    
                    for char in self.word:
                        if board[ytemp][x_pos] == " " or board[ytemp][x_pos] == char:
                            if ytemp - y_pos + 1 == len(self.word):
                                valid0 = True
                            else:
                                ytemp += 1
                        
                        else:
                            break
                            
                    word = self.word[::-1]
                    ytemp = y_pos
                    
                    for char in word:
                        if board[ytemp][x_pos] == " " or board[ytemp][x_pos] == char:
                            if ytemp - y_pos + 1 == len(self.word):
                                valid1 = True
                            else:
                                ytemp += 1
                        
                        else:
                            break
                    
                    if valid0:
                        list_of_start_pos.append((x_pos, y_pos, 0))
                        
                    if valid1:
                        list_of_start_pos.append((x_pos, y_pos, 1))
                        
            if list_of_start_pos == []:
                pass
            
            else:
                self.start_pos = list_of_start_pos[random.randint(0, len(list_of_start_pos) - 1)]

                x_pos = self.start_pos[0]
                y_pos = self.start_pos[1]

                if self.start_pos[2] == 0:
                    for char in self.word:
                        board[y_pos][x_pos] = char
                        ans_board[y_pos][x_pos] = char
                        y_pos += 1

                else:
                    for char in word:
                        board[y_pos][x_pos] = char
                        ans_board[y_pos][x_pos] = char
                        y_pos += 1
                        
                self.end_pos = (x_pos, y_pos - 1)
                self.added = True

                
#DIAGONALS
class positive:
    def __init__(self, word):
        self.word = word
        self.start_pos = None #tuple (x,y,0/1), 1 = reverse
        self.end_pos = None #tuple (x,y)
        self.added = False
        
    def addword(self):
        global board_empty
            
        if board_empty:
            x_pos = random.randint(0, 19 - len(self.word))
            y_pos = random.randint(len(self.word), 19)
            
            if random.randint(0, 1) == 1:
                self.start_pos = (x_pos, y_pos, 1)
                word = self.word[::-1]
                
            else:
                self.start_pos = (x_pos, y_pos, 0)
                word = self.word
            
            for char in word:
                board[y_pos][x_pos] = char
                ans_board[y_pos][x_pos] = char
                x_pos += 1
                y_pos -= 1
                
            self.end_pos = (x_pos - 1, y_pos + 1)
            board_empty = False
            self.added = True
            
        else:
            list_of_start_pos = []
            
            for x_pos in range(20 - len(self.word)):
                for y_pos in range(len(self.word), 20):
                    xtemp = x_pos
                    ytemp = y_pos
                    valid0 = False
                    valid1 = False
                    
                    for char in self.word:
                        if board[ytemp][xtemp] == " " or board[ytemp][xtemp] == char:
                            if xtemp - x_pos + 1 == len(self.word):
                                valid0 = True
                            else:
                                xtemp += 1
                                ytemp -= 1
                        
                        else:
                            break
                            
                    word = self.word[::-1]
                    xtemp = x_pos
                    ytemp = y_pos
                    
                    for char in word:
                        if board[ytemp][xtemp] == " " or board[ytemp][xtemp] == char:
                            if xtemp - x_pos + 1 == len(self.word):
                                valid1 = True
                            else:
                                xtemp += 1
                                ytemp -= 1
                        
                        else:
                            break
                    
                    if valid0:
                        list_of_start_pos.append((x_pos, y_pos, 0))
                        
                    if valid1:
                        list_of_start_pos.append((x_pos, y_pos, 1))
                        
            if list_of_start_pos == []:
                pass
            
            else:
                self.start_pos = list_of_start_pos[random.randint(0, len(list_of_start_pos) - 1)]

                x_pos = self.start_pos[0]
                y_pos = self.start_pos[1]

                if self.start_pos[2] == 0:
                    for char in self.word:
                        board[y_pos][x_pos] = char
                        ans_board[y_pos][x_pos] = char
                        x_pos += 1
                        y_pos -= 1

                else:
                    for char in self.word[::-1]:
                        board[y_pos][x_pos] = char
                        ans_board[y_pos][x_pos] = char
                        x_pos += 1
                        y_pos -= 1
                
                self.end_pos = (x_pos - 1, y_pos + 1)
                self.added = True
                
class negative:
    def __init__(self, word):
        self.word = word
        self.start_pos = None #tuple (x,y,0/1), 1 = reverse
        self.end_pos = None #tuple (x,y)
        self.added = False
    
    def addword(self):
        global board_empty
        
        if board_empty:
            x_pos = random.randint(0, 19 - len(self.word))
            y_pos = random.randint(0, 19 - len(self.word))
            
            if random.randint(0, 1) == 1:
                self.start_pos = (x_pos, y_pos, 1)
                word = self.word[::-1]
                
            else:
                self.start_pos = (x_pos, y_pos, 0)
                word = self.word
            
            for char in word:
                board[y_pos][x_pos] = char
                ans_board[y_pos][x_pos] = char
                x_pos += 1
                y_pos += 1
                
            self.end_pos = (x_pos - 1, y_pos - 1)
            board_empty = False
            self.added = True
            
        else:
            list_of_start_pos = []
            
            for x_pos in range(20 - len(self.word)):
                for y_pos in range(20 - len(self.word)):
                    xtemp = x_pos
                    ytemp = y_pos
                    valid0 = False
                    valid1 = False
                    
                    for char in self.word:
                        if board[ytemp][xtemp] == " " or board[ytemp][xtemp] == char:
                            if xtemp - x_pos + 1 == len(self.word):
                                valid0 = True
                            else:
                                xtemp += 1
                                ytemp += 1
                        
                        else:
                            break
                            
                    word = self.word[::-1]
                    xtemp = x_pos
                    ytemp = y_pos
                    
                    for char in word:
                        if board[ytemp][xtemp] == " " or board[ytemp][xtemp] == char:
                            if xtemp - x_pos + 1 == len(self.word):
                                valid1 = True
                            else:
                                xtemp += 1
                                ytemp += 1
                        
                        else:
                            break
                    
                    if valid0:
                        list_of_start_pos.append((x_pos, y_pos, 0))
                        
                    if valid1:
                        list_of_start_pos.append((x_pos, y_pos, 1))
                        
            if list_of_start_pos == []:
                pass
            
            else:
                self.start_pos = list_of_start_pos[random.randint(0, len(list_of_start_pos) - 1)]

                x_pos = self.start_pos[0]
                y_pos = self.start_pos[1]

                if self.start_pos[2] == 0:
                    for char in self.word:
                        board[y_pos][x_pos] = char
                        ans_board[y_pos][x_pos] = char
                        x_pos += 1
                        y_pos += 1

                else:
                    for char in self.word[::-1]:
                        board[y_pos][x_pos] = char
                        ans_board[y_pos][x_pos] = char
                        x_pos += 1
                        y_pos += 1
                                         
                self.end_pos = (x_pos - 1, y_pos - 1)
                self.added = True
        
#POSITION
def gridpos(xy):
    xaxis = "ABCDEFGHIJKLMNOPQRST"
    
    return xaxis[xy[0]] + str(xy[1] + 1)
        
#GAME
words = []
number = int(input("Select number of words (1-30): "))

while len(words) < number * 2:
    word = wordlist[random.randint(0, 178691)]
    if 5 < len(word) < 20 and word not in words:
        words.append(word.strip())

count = 0
i = 0
pos_list = [["", "", ""] for a in range(number)]
wordfile = open("words.txt", "w")

print("WORDS: ")
        
while True:
    i += 1
    num = random.randint(1, 4)
    
    if num == 1:
        wordobj = horizontal(words[i])
        orientation = "HORIZONTAL"
        
    elif num == 2:
        wordobj = vertical(words[i])
        orientation = "VERTICAL"
        
    elif num == 3:
        wordobj = positive(words[i])
        orientation = "DIAGONAL"
        
    else:
        wordobj = negative(words[i])
        orientation = "DIAGONAL"
        
    wordobj.addword()
    
    if wordobj.added:
        if wordobj.start_pos[2] == 0:
            pos_string = gridpos(wordobj.start_pos[:2])
            wordfile.write(wordobj.word + "," + str(pos_to_index(wordobj.start_pos)) + "," + str(pos_to_index(wordobj.end_pos)) + ";")
        else:
            pos_string = gridpos(wordobj.end_pos)
            wordfile.write(wordobj.word + "," + str(pos_to_index(wordobj.end_pos)) + "," + str(pos_to_index(wordobj.start_pos)) + ";")
            
        pos_list[count] = [wordobj.word, pos_string, orientation]
        
        count += 1
        if count < 10:
            print(str(count) + "   " + wordobj.word)
        else:
            print(str(count) + "  " + wordobj.word)
            
        
            
        
    if count == number:
        wordfile.close()
        break
        
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
y_pos = -1

for row in board:
    y_pos += 1
    x_pos = -1
    for char in row:
        x_pos += 1
        if char == " ":
            board[y_pos][x_pos] = alphabets[random.randint(0, 25)]

#DISPLAY
print()
display(board, None)
display(board, "grid.txt")


# In[ ]:


choice = input("Enter 'Y' to reveal answer: ")

if choice.lower() == "y":
    print()
    print("\n======================================================\nANSWER\n\n")
    display(ans_board, None)
    print(end = "\n\n")

    count = -1
    print("NO. WORD".ljust(24) + "POSITION".ljust(15) + "ORIENTATION")

    
    for sublist in pos_list:
        count += 1
        
        if count < 9:
            print(str(count + 1) + "   " + sublist[0].ljust(20) + sublist[1].ljust(15) + sublist[2])
        else:
            print(str(count + 1) + "  " + sublist[0].ljust(20) + sublist[1].ljust(15) + sublist[2])
            


# In[ ]:





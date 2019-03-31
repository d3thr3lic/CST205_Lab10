#CST 205 - Lab 10
#Nicholas Saunders
#Mitchell Saunders
import random

def warmUp():
  name = requestString("What is your name?")
  printNow(name)
  
def goUntilStop():
  name = ""
  while name != "stop":
    name = requestString("input a string")
    printNow(name)

        
                
                        
###############################################################      
def hangman():
  instructions = "To play Hangman, guess letters to try to "+ \
                 "come up with an unknown word with less than six guesses"
  printNow(instructions)
  
  #add/change words in all lower case here
  wordList = ['jazz', 'garbage', 'brick', 'manufacturing', 'cool cat', 'lets go home']
  
  
  
  
  incorrectLetters = ""
  score = 0
  
  #use rng to select word(s) from word list
  randomNum = random.randint(0, len(wordList)-1)
  word = wordList[randomNum]
  
  textDisplayed = initChosenWord(word)
  printNow(textDisplayed)
  
  #this loop is for the entire game
  while True:  
    #this loop is just for the input, making sure that the input is valid 
    while True:
      chosenLetter = requestString("Input a letter").lower()
      printNow("=========================")
      #calls function to verify validity of input
      if checkUsed(chosenLetter, textDisplayed, incorrectLetters):
        printNow("Letter previously entered. Please try again.")
      elif not(acceptableInput(chosenLetter)):
        printNow("Input a single letter only please!")
      else:
        break
    
    #if the chacter is in the word, it will be added to the dashed output for the user
      #otherwise, tell them they are wrong and increment score
    correctBool = False
    if(word.find(chosenLetter) != -1):
      #stores displayed dashed word from user function
      textDisplayed = (buildChosenWord(word, textDisplayed, chosenLetter))
      correctBool = True
      printNow("Correct!")
    else:
      correctBool = False
      printNow("Incorrect!")
      score += 1
    
    #builds list of characters that are not valid
    if (incorrectLetters.find(chosenLetter) == -1) and correctBool == False:
      incorrectLetters += chosenLetter
    
    #count number of letters left in word to find
    lettersLeft = countChar(textDisplayed,'_')
       
    printNow("Word so far:")
    printNow(textDisplayed)    
    printNow("Incorrect guesses:")
    printNow(incorrectLetters)
    printNow("You have used " + str(score) + " of six guesses")
    
    #determine if the game has ended, either win or loose. if it has, break out of loop and end game
    if lettersLeft == 0:
      printNow("Congratulations you win!!")
      printNow("The game is now quitting.")
      break
    elif lettersLeft > 0 and score > 5:
      printNow("Sorry, you lose.  Better luck next time!")
      printNow("The game is now quitting.")
      break

#make sure input is a single character and it is alphebeitc   
def acceptableInput(str):
  if len(str) == 1:
    if str.isalpha():
      return True
    else:
      return False
  else:
    return False

#count the instances of a character in a string    
def countChar(str,char):
  count = 0
  for i in range(len(str) - 1):
    if str[i:i+1] == char:
      count = count + 1
  return count

#returns the formatted and updated string to display to player with dashes and letters
def buildChosenWord(word, textDisplayed, chosenLetter):
  index = 0
  numOfInstances = countChar(word,chosenLetter)
  for i in range(0, numOfInstances + 1):
    index = word.find(chosenLetter, index)
    if index != -1:
      textDisplayed = textDisplayed[:index*2] + chosenLetter + textDisplayed[index*2+1:]
    index += 1
  return textDisplayed

#converts word from list (with or without spaces) into a dashed string for the player to see 
def initChosenWord(word):
  textDisplayed = "_ "*len(word)
  index = 0    
  numOfSpaces = countChar(word," ")
  for i in range(0, numOfSpaces):
    index = word.find(" ", index+1)
    if index != -1:
      textDisplayed = textDisplayed[:index*2] + " " + textDisplayed[index*2+1:]
    
  return textDisplayed
  
#compares user input to all previous inputs, valid or invalid  
def checkUsed(chosenLetter, word, incorrectStr):
  #if the chosen letter is not in the word, or if it is found in the list of incorrect letters
  if word.find(chosenLetter) != -1:
    return True
  elif incorrectStr.find(chosenLetter) != -1:
    return True
  else:
    return False
  
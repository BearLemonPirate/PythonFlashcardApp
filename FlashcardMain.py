#Python revision flashcard app
"""
Idea is to have a GUI that enables you to pick a selection of flashcards from a database, and runs through those cards
randomly.  On seeing a card, you can either type the answer and check, or just show the answer, depending on if the flashcard
is an answerable type or not.  When finished, you can back out to the main menu loop.
"""

#### Import librarys here ####
#import maths
import xlrd
#import pandas

#### Object classes defined here ####

#### Useful functions defined here ####

#### Gameplay Loops defined here ####

def MainGamePlayLoop ():
    #This loop will play constantly and will reset any varialbes ready for a different deck to be loaded after 1 is played
    print("MainGamePlayLoop starting")
    """
    select deck (follows dropbox of specified location)
    pass to IndividualDeckLoop
    Should reset to start on end of deck loop providing new selection as function will be endless
    """

    #### testing ####
    IndividualDeckLoop("E:\GitHub Repos\PythonFlashcardApp\TestExcelSheet.xls")

def IndividualDeckLoop (ChosenDeck):
    #This loop will cover the 'round' played with a single deck, keeping track of scores, which cards have been played, etc
    print("IndividualDeckLoop starting")
    """
    Find deck
    read into array of card objects
    randomly select card from array
    pass to FlashcardLogic
    leave if wrong, remove from array if correct
    repeat until cards are depleated
    present score (attempts-card total / card total * 100)
    Ask if you want to save results (date, score, total question answered, total attempts, etc)
    """

    #### testing ####
    deckSpreadSheet = xlrd.open_workbook(ChosenDeck, ragged_rows=True)
    deckDataSheet = deckSpreadSheet.sheet_by_index(0)
    rowcount = deckDataSheet.nrows
    print(rowcount)

    """
    stopCounter = 0
    indexCounter = 1
    while stopCounter != 1:
        if 
        indexCounter = indexCounter + 1
    """





def FlashcardLogic ():
    #this is the generic function called to read any individual card, process, present accordingly, and check results
    print("FlashcardLogic starting")
    """
    read card
    check card type
    present card
    check user input (if applic)
    present result (offer force correct)
    return true/false for right/wrong
    """





while True:
    MainGamePlayLoop ()
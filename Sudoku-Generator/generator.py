# ==================================================================== #
#  File name:      generator.py                 #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           13-Oct-2023                  #    *= #        =*    #
#  Description:    File providing generation    #   #/  #         \#   #
#                  tools.                       #  |#   #   $      #|  #
#                                               #  |#   #   #      #|  #
#  Rev:            0.1                          #   #\  #   #     /#   #
#                                               #    *= #   #    =+    #
#                                               #     *++######++*     #
#                                               #        *-==-*        #
# ==================================================================== #
#  Revision history:                                                   #
#  Date        Description                                             #
#  13-Oct-2023 File created                                            #
# ==================================================================== #
#  To-Do: !=Priority, ~=Bug, ?=Idea/nice to have                       #
#                                                                      #
# ==================================================================== #

# =========== #
#   Imports   #
# =========== #
import subprocess
from log import print_pretty_sudoku
import logging as log
from copy import deepcopy
from sudoku import Sudoku
import definitions as const 

# =============== #
#   Definitions   #
# =============== #
L_FLAGS = [
    "qqwing",
    "--generate",
    "1",
    "--one-line", 
    "--csv", 
    "--solution"
]

L_UNWANTED_CHAR = [
    "'",
    " ",
    "Puzzle,",
    "Solution,",
    "\\",
    "n",
    "b"
]
EMPTY_CHAR = " "

# =========== #
#   Methods   #
# =========== #
def get_multiple_sudokus(amount:int, difficulty:str):
    """Create a list of unique sudokus

    :param amount: Number of sudokus in the lsit
    :type amount: integer
    :param difficulty: Difficulty levels of sudokus
    :type difficulty: string
    :return: List of uniques sudokus
    :rtype: list[Sudoku]
    """
    # Initialize the list
    lSudokus = list()
    
    # Keep going until the correct amount of sudokus is created
    while(len(lSudokus) < amount):
        # Create a sudoku
        newSudoku = generate_sudoku(difficulty)
        
        # Check if it is not found already
        if not any([oldSudoku.is_equal(newSudoku.llSolution) for oldSudoku in lSudokus]):
            newSudoku.number = len(lSudokus)+1
            log.debug(f"Found sudoku {newSudoku.number}/{amount} ")
            lSudokus.append(newSudoku)
            
    return lSudokus
    
def get_sudoku_matrix(csvFormat:str):
    """Convert a CSV format sudoku into a matrix

    :param csvFormat: Sudoku in csv format
    :type csvFormat: string
    :return: matrix which represents the original csv formate
    :rtype: list[list[string]]
    """
    # log.debug(f"Converting CSV variant of {csvFormat}.")
    llNewSudoku = deepcopy(const.LL_EMPTY_SUDOKU)
    
    for index, char in enumerate(csvFormat):
        # Calculate the current row and column
        row = int(index / 9) 
        col = index % 9
        
        if const.is_number(char):
            llNewSudoku[row][col] = char
        else:
            llNewSudoku[row][col] = EMPTY_CHAR
    
    # log.debug(f"Converted: \n {print_pretty_sudoku(llNewSudoku)}.")
    return llNewSudoku
        
def generate_sudoku(difficulty:str=const.DIFF_ANY):
    """Create a sudoku object

    :param difficulty: Level of difficulty for the sudoku, defaults to const.DIFF_ANY
    :type difficulty: string, optional
    :rtype: Sudoku
    """    
    # Create the command
    lCommand = L_FLAGS + [f"--difficulty", difficulty]
    # log.debug(f"Running command \"{lCommand}\"")
    
    # Run QQwing
    commandOut = str(subprocess.run(lCommand, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout)
    # log.debug(f"Retrieved command output: {commandOut}")
    
    # Prepare output for form conversion
    for remove in L_UNWANTED_CHAR:
        commandOut = commandOut.replace(remove, "") 
    
    # log.debug(f"Cleared string: {commandOut}")
    separator = commandOut.find(",")
    
    sudokuRaw = commandOut[:separator]
    if len(sudokuRaw) != 81:
        log.error(f"The raw sudoku has incorrect amount of characters: {len(sudokuRaw)}")
    
    solutionRaw = commandOut[separator+1:-1]
    if len(solutionRaw) != 81:
        log.error(f"The raw solution has incorrect amount of characters: {len(solutionRaw)}")
    
    # Create the object
    return Sudoku(
        get_sudoku_matrix(sudokuRaw),
        get_sudoku_matrix(solutionRaw)
    ) 
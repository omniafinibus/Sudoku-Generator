# ==================================================================== #
#  File name:      latex_builder.py             #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           29-Oct-2023                  #    *= #        =*    #
#  Description:    Functions to create the      #   #/  #         \#   #
#                  "tex" file                   #  |#   #   $      #|  #
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

import os
from sudoku import Sudoku
from generator import EMPTY_CHAR
from definitions import DIFF_EASY, DIFF_SIMP, DIFF_XPER, DIFF_MEDI

# =============== #
#   Definitions   #
# =============== #
VALUE_NUMBER_LABEL = "$V_SUDOKU_NUMBER$"
VALUE_R_NUMBER_LABEL = "$VR_SUDOKU_NUMBER$"
VALUE_L_NUMBER_LABEL = "$VL_SUDOKU_NUMBER$"
SOLUTION_NUMBER_LABEL = "$S_SUDOKU_NUMBER$"
SOLUTION_L_NUMBER_LABEL = "$SL_SUDOKU_NUMBER$"
SOLUTION_R_NUMBER_LABEL = "$SR_SUDOKU_NUMBER$"

COVER_LABEL = "$DIFFICULTY_COLOR$"
COLOR_LABEL = "$TEXT_COLOR$"
DIFF_LABEL = "$DIFFICULTY_HERE$"

DIFF_BEGINNER_BACK = "beginner_background"
DIFF_BEGINNER_TEXT = "beginner_text"
DIFF_BEGINNER_LABEL = "Beginner"

DIFF_EASY_BACK = "easy_background"
DIFF_EASY_TEXT = "easy_text"
DIFF_EASY_LABEL = "Easy"

DIFF_HARD_BACK = "hard_background"
DIFF_HARD_TEXT = "hard_text"
DIFF_HARD_LABEL = "Hard"

DIFF_EXPERT_BACK = "expert_background"
DIFF_EXPERT_TEXT = "expert_text"
DIFF_EXPERT_LABEL = "Expert"



TEMPLATE_PATH = os.path.join(os.path.abspath("."), "assets")
LEFT = "left"
RIGHT = "right"


# =========== #
#   Methods   #
# =========== #
def latex_start_old(difficulty:str):
    """Create the first page and LaTeX setup for the final PDF

    :param difficulty: Difficulty level of sudokus
    :type difficulty: string
    :return: Latex code to be placed in a tex file
    :rtype: string
    """    
    # Select the correct cover image
    if difficulty == DIFF_SIMP:
        coverColor = DIFF_BEGINNER_BACK
        textColor = DIFF_BEGINNER_TEXT
        coverText = DIFF_BEGINNER_LABEL
    elif difficulty == DIFF_EASY:
        coverColor = DIFF_EASY_BACK
        textColor = DIFF_EASY_TEXT
        coverText = DIFF_EASY_LABEL
    elif difficulty == DIFF_MEDI:
        coverColor = DIFF_HARD_BACK
        textColor = DIFF_HARD_TEXT
        coverText = DIFF_HARD_LABEL
    elif difficulty == DIFF_XPER:
        coverColor = DIFF_EXPERT_BACK
        textColor = DIFF_EXPERT_TEXT
        coverText = DIFF_EXPERT_LABEL
        
    # Read template
    startTemplate = open( os.path.join(TEMPLATE_PATH, "start.txt"), "r").read()
    
    # Set the correct cover image
    startTemplate = startTemplate.replace(COVER_LABEL, coverColor)
    startTemplate = startTemplate.replace(DIFF_LABEL, coverText)
    startTemplate = startTemplate.replace(COLOR_LABEL,textColor)
    
    return startTemplate

def latex_page_old(sudoku:Sudoku, leftOrRight:str, solution:Sudoku = None):
    """Create a page with a sudoku and a possible solution

    :param sudoku: _description_
    :type sudoku: Sudoku
    :param leftOrRight: Orientation of the page when the book is open
    :type leftOrRight: string
    :param solution: The solution to show on the page, if None, only the sudoku is shown, defaults to None
    :type solution: Sudoku, optional
    :return: LaTeX code for a page with sudoku
    :rtype: string
    """    
    # Get correct page
    PageTemplate = open(os.path.join(TEMPLATE_PATH, f"page_{leftOrRight.lower()}.txt")).read()
    PageTemplate = PageTemplate.replace(NUMBER_LABEL, str(sudoku.number))
    for row in range(9):
        for col in range(9):
            PageTemplate = PageTemplate.replace(f"${row+1}{col+1}$", str(sudoku.llValues[row][col]))
            
    # Insert or clear the solution
    if solution:
        SolutionTemplate = open(os.path.join(TEMPLATE_PATH, f"solution_{leftOrRight.lower()}.txt")).read()
        SolutionTemplate = SolutionTemplate.replace(NUMBER_LABEL, str(solution.number))
        for row in range(9):
            for col in range(9):
                if solution.llValues[row][col] != EMPTY_CHAR:
                    SolutionTemplate = SolutionTemplate.replace(f"${row+1}{col+1}$", str(solution.llSolution[row][col]))
                else:
                    SolutionTemplate = SolutionTemplate.replace(f"${row+1}{col+1}$", "\\textcolor{blue}{" + str(solution.llSolution[row][col]) + "}" )
                    
                
        PageTemplate = PageTemplate.replace(SOLUTION_LABEL, SolutionTemplate)
    else:
        PageTemplate = PageTemplate.replace(SOLUTION_LABEL, "")
    
    return PageTemplate

def latex_last_page_old(solution1:Sudoku, solution2:Sudoku, difficulty:str):
    """Prepare the last pages and end of the latex document
    :param solution1: The first solution to show on the page
    :type solution1: Sudoku
    :param solution2: The second solution to show on the page
    :type solution2: Sudoku
    :param difficulty: Difficulty level of sudokus
    :type difficulty: string
    :return: Last LaTeX code
    :rtype: string
    """    
    lastPage = open(os.path.join(TEMPLATE_PATH, "final_page.txt")).read()
    
    # Add correct sudoku numbers
    lastPage = lastPage.replace(NUMBER_LABEL, str(solution1.number), 1)
    lastPage = lastPage.replace(NUMBER_LABEL, str(solution2.number))
    
    for row in range(9):
        for col in range(9):
            if solution1.llValues[row][col] != EMPTY_CHAR:
                lastPage = lastPage.replace(f"${row+1}{col+1}$", str(solution1.llSolution[row][col]), 1)
            else:
                lastPage = lastPage.replace(f"${row+1}{col+1}$", "\\textcolor{gray}{" + str(solution1.llSolution[row][col]) + "}" , 1)
            
            if solution2.llValues[row][col] != EMPTY_CHAR:
                lastPage = lastPage.replace(f"${row+1}{col+1}$", str(solution2.llSolution[row][col]), 1)
            else:
                lastPage = lastPage.replace(f"${row+1}{col+1}$", "\\textcolor{gray}{" + str(solution2.llSolution[row][col]) + "}" , 1)
    
    
    # Select the correct cover image
    if difficulty == DIFF_SIMP:
        coverColor = DIFF_BEGINNER_BACK
        textColor = DIFF_BEGINNER_TEXT
        coverText = DIFF_BEGINNER_LABEL
    elif difficulty == DIFF_EASY:
        coverColor = DIFF_EASY_BACK
        textColor = DIFF_EASY_TEXT
        coverText = DIFF_EASY_LABEL
    elif difficulty == DIFF_MEDI:
        coverColor = DIFF_HARD_BACK
        textColor = DIFF_HARD_TEXT
        coverText = DIFF_HARD_LABEL
    elif difficulty == DIFF_XPER:
        coverColor = DIFF_EXPERT_BACK
        textColor = DIFF_EXPERT_TEXT
        coverText = DIFF_EXPERT_LABEL
        
    # Set the correct cover image
    lastPage = lastPage.replace(COVER_LABEL, coverColor)
    
    return lastPage

def new_page():
    return "\n  \\clearpage\n\n"

def latex_start():
    return open( os.path.join(TEMPLATE_PATH, "first_pages.txt"), "r").read()

def latex_solutionless(sudokuL:Sudoku, sudokuR:Sudoku):
    PageTemplate = open(os.path.join(TEMPLATE_PATH, f"solutionless_sudoku.txt")).read()
    PageTemplate = PageTemplate.replace(VALUE_L_NUMBER_LABEL, str(sudokuL.number))
    PageTemplate = PageTemplate.replace(VALUE_R_NUMBER_LABEL, str(sudokuR.number))
    
    PageTemplate = replace_matrix_values(sudokuL, "VL", PageTemplate)
    PageTemplate = replace_matrix_values(sudokuR, "VR", PageTemplate)
    
    return PageTemplate

def latex_left_block(sudoku:Sudoku, sudokuS:Sudoku):
    PageTemplate = open(os.path.join(TEMPLATE_PATH, f"sudoku_and_solution_left.txt")).read()
    PageTemplate = PageTemplate.replace(VALUE_NUMBER_LABEL, str(sudoku.number))
    PageTemplate = PageTemplate.replace(SOLUTION_NUMBER_LABEL, str(sudokuS.number))
    
    PageTemplate = replace_matrix_values(sudoku, "V", PageTemplate)
    PageTemplate = replace_matrix_solutions(sudokuS, "S", PageTemplate)
    
    return PageTemplate

def latex_right_block(sudoku:Sudoku, sudokuS:Sudoku):
    PageTemplate = open(os.path.join(TEMPLATE_PATH, f"sudoku_and_solution_right.txt")).read()
    PageTemplate = PageTemplate.replace(VALUE_NUMBER_LABEL, str(sudoku.number))
    PageTemplate = PageTemplate.replace(SOLUTION_NUMBER_LABEL, str(sudokuS.number))
    
    PageTemplate = replace_matrix_values(sudoku, "V", PageTemplate)
    PageTemplate = replace_matrix_solutions(sudokuS, "S", PageTemplate)
    
    return PageTemplate

def latex_solution_block(sudokuL:Sudoku, sudokuR:Sudoku):
    PageTemplate = open(os.path.join(TEMPLATE_PATH, f"solution_block.txt")).read()
    PageTemplate = PageTemplate.replace(SOLUTION_L_NUMBER_LABEL, str(sudokuL.number))
    PageTemplate = PageTemplate.replace(SOLUTION_R_NUMBER_LABEL, str(sudokuR.number))
    
    PageTemplate = replace_matrix_solutions(sudokuL, "SL", PageTemplate)
    PageTemplate = replace_matrix_solutions(sudokuR, "SR", PageTemplate)
    
    return PageTemplate

def latex_end():
    return open( os.path.join(TEMPLATE_PATH, "last_pages.txt"), "r").read()

def replace_matrix_solutions(sudoku:Sudoku, prefix:str, pageData:str):
    for row in range(9):
        for col in range(9):
            if sudoku.llValues[row][col] != EMPTY_CHAR:
                pageData = pageData.replace(f"{prefix}{row+1}{col+1}", str(sudoku.llSolution[row][col]), 1)
            else:
                pageData = pageData.replace(f"{prefix}{row+1}{col+1}", "\\textcolor{gray}{" + str(sudoku.llSolution[row][col]) + "}" , 1)
                
    return pageData

def replace_matrix_values(sudoku:Sudoku, prefix:str, pageData:str):
    for row in range(9):
        for col in range(9):
            if sudoku.llValues[row][col] != EMPTY_CHAR:
                pageData = pageData.replace(f"{prefix}{row+1}{col+1}", str(sudoku.llSolution[row][col]), 1)
            else:
                pageData = pageData.replace(f"{prefix}{row+1}{col+1}", " " , 1)
    
    return pageData
# ==================================================================== #
#  File name:      main.py                      #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           13-Oct-2023                  #    *= #        =*    #
#  Description:    Generates sudoku's in a      #   #/  #         \#   #
#                  in latex form.               #  |#   #   $      #|  #
#                                               #  |#   #   #      #|  #
#  Rev:            0.1                          #   #\  #   #     /#   #
#                                               #    *= #   #    =+    #
#                                               #     *++######++*     #
#                                               #        *-==-*        #
# ==================================================================== #
#  Revision history:                                                   #
#  Date        Description                                             #
#  13-oct-2023 File created                                            #
# ==================================================================== #
#  To-Do: !=Priority, ~=Bug, ?=Idea/nice to have                       #
# ==================================================================== #
import os
import log
import datetime
import definitions as const
from generator import get_multiple_sudokus
import latex_builder as builder

logger = log.setup_custom_logger(
    name="root",
    directory=const.OUT_DIR,
    makeFolder=True,
    loggingLevel=log.logging.DEBUG
)

def create_sudoku_book(difficulty):
    amount = 777
    # difficulty = const.DIFF_EASY
    date = str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().year)
    time = datetime.datetime.now()
    time = str(time.hour) + "-" + str(time.minute) + "-" + str(time.second)
    OUTPUT_FOLDER = "/" + os.path.join("home", "arjan", "Nextcloud", "Programming", "Full_Projects", "SudokuGenerator", "generated_books", f"{date}_{time}_{difficulty}_{amount}")

    # Create enough sudokus
    lSudokus = get_multiple_sudokus(amount, difficulty)
    
    # Create a new tex file
    os.mkdir(OUTPUT_FOLDER)

    # Copy all sudokus to a text file
    newTxtFile = open(os.path.join(OUTPUT_FOLDER, "used_sudokus.txt"), "w")
    for sudoku in lSudokus:
        line = f"[{sudoku.number}]\t" + "|" + " ".join(sudoku.get_solution_list()) + "|" + " ".join([i.replace(' ', '_') for i in sudoku.get_values_list()]) + "\n"
        newTxtFile.write(line)
    newTxtFile.close()
    
    newTexFile = open(os.path.join(OUTPUT_FOLDER, "sudoku_book.tex"), "w")

    #Add the first page and Tex setup
    logger.debug(f"Creating TEX file")
    newTexFile.write(builder.latex_start())

    # Add all sudokus (without solution)
    newTexFile.write(builder.new_page())
    newTexFile.write(builder.latex_solutionless(lSudokus[0], lSudokus[1]))
    logger.debug(f"Added sudoku 1/{amount}")
    logger.debug(f"Added sudoku 2/{amount}")

    newTexFile.write(builder.latex_solutionless(lSudokus[2], lSudokus[3]))
    logger.debug(f"Added sudoku 3/{amount}")
    logger.debug(f"Added sudoku 4/{amount}")

    # Add the remaining sudokus with solutions
    pageOrient = builder.RIGHT
    
    i = offset = 4 
    dontMakeLast = False
    while i < len(lSudokus):
        newTexFile.write(builder.new_page())
        if pageOrient == builder.RIGHT:
            newTexFile.write(builder.latex_right_block(lSudokus[i], lSudokus[i-offset]))
            i += 1
            logger.debug(f"Added sudoku {i}/{amount}")
            try:
                newTexFile.write(builder.latex_right_block(lSudokus[i], lSudokus[i-offset]))
                i += 1
                logger.debug(f"Added sudoku {i}/{amount}")
            except:
                dontMakeLast = True
                newTexFile.write(builder.latex_solution_block(lSudokus[-4], lSudokus[-3]))
                newTexFile.write(builder.new_page())
                newTexFile.write(builder.latex_solution_block(lSudokus[-2], lSudokus[-1]))
                
            pageOrient = builder.LEFT
            
        elif pageOrient == builder.LEFT:
            newTexFile.write(builder.latex_left_block(lSudokus[i], lSudokus[i-offset]))
            i += 1
            logger.debug(f"Added sudoku {i}/{amount}")
            try:
                newTexFile.write(builder.latex_left_block(lSudokus[i], lSudokus[i-offset]))
                i += 1
                logger.debug(f"Added sudoku {i}/{amount}")
            except:
                dontMakeLast = True
                newTexFile.write(builder.latex_solution_block(lSudokus[-4], lSudokus[-3]))
                newTexFile.write(builder.new_page())
                newTexFile.write(builder.latex_solution_block(lSudokus[-2], lSudokus[-1]))
            pageOrient = builder.RIGHT
                       
    try:
        if not dontMakeLast:
            newTexFile.write(builder.new_page())
            newTexFile.write(builder.latex_solution_block(lSudokus[-4], lSudokus[-3]))
            newTexFile.write(builder.latex_solution_block(lSudokus[-2], lSudokus[-1]))
    except:
        pass
    
    
    # Add the final page
    newTexFile.write(builder.latex_end())
    newTexFile.close()

    print("done")

create_sudoku_book(const.DIFF_SIMP) 
# create_sudoku_book(const.DIFF_EASY) 
# create_sudoku_book(const.DIFF_MEDI) 
# create_sudoku_book(const.DIFF_XPER)
# 
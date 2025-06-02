# ==================================================================== #
#  File name:      definitions.py               #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           13-Oct-2023                  #    *= #        =*    #
#  Description:    definitions used through     #   #/  #         \#   #
#                  the project                  #  |#   #   $      #|  #
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
from math import isnan, isinf

# =============== #
#   Definitions   #
# =============== #
OUT_DIR = "/" + os.path.join("home", "arjan", "Nextcloud", "Documents", "sudoku")
LL_EMPTY_SUDOKU = [
    ["", "", "", "", "", "","", "", ""],
    ["", "", "", "", "", "","", "", ""],
    ["", "", "", "", "", "","", "", ""],
    ["", "", "", "", "", "","", "", ""],
    ["", "", "", "", "", "","", "", ""],
    ["", "", "", "", "", "","", "", ""],
    ["", "", "", "", "", "","", "", ""],
    ["", "", "", "", "", "","", "", ""],
    ["", "", "", "", "", "","", "", ""],
]

DIFF_ANY = "any"
DIFF_SIMP = "simple"
DIFF_EASY = "easy"
DIFF_MEDI = "intermediate"
DIFF_XPER = "expert"

# =========== #
#   Methods   #
# =========== #
def is_number(value:str):
    """
    Check if a string is a number, either a float or integer.
    float('nan') and float('inf') will return a false

    :param value: String to check
    :type value: string
    :return: Boolean if it is a number or not
    :rtype: boolean
    """    
    try:
        return all([not isnan(float(str(value))), not isinf(float(str(value)))])
    except ValueError:
        return False
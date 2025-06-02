# ==================================================================== #
#  File name:      sudoku.py                    #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           13-Oct-2023                  #    *= #        =*    #
#  Description:    File defining the sudoku     #   #/  #         \#   #
#                  object.                      #  |#   #   $      #|  #
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

class Sudoku:
    def __init__(self, llValues, llSolution, number:int=0):
        self.llValues = llValues
        self.llSolution = llSolution
        self.number = number
    
    def is_equal(self, llSolutionCompare):
        return self.llSolution == llSolutionCompare
    
    def get_solution_list(self):
        lSolution = list()
        for row in self.llSolution:
            lSolution += row
        return lSolution
        
    def get_values_list(self):
        lValues = list()
        for row in self.llValues:
            lValues += row
        return lValues
        
    def __repr__(self):
        return f"value: {self.llValues}\n\r" + f"solution: {self.llSolution}"
    
    
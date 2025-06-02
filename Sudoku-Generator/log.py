# ==================================================================== #
#  File name:      log.py                       #        _.==._        #
#  Author:         Arjan Lemmens                #     .+=##**##=+.     #
#  Date:           18-Jul-2023                  #    *= #        =*    #
# ============================================= #   #/  #         \#   #
#  Description:    Method used to initialize    #  |#   #   $      #|  #
#                  the global logger.           #  |#   #   #      #|  #
#  Rev:            3.2                          #   #\  #   #     /#   #
#                                               #    *= #   #    =+    #
#                                               #     *++######++*     #
#                                               #        *-==-*        #
# ==================================================================== #
#  Revision history:                                                   #
#  Date        Description                                             #
#  18-Jul-2023 File created                                            #
# ==================================================================== #
#  To-Do: !=Priority, ~=Bug, ?=Idea/nice to have                       #
#                                                                      #
# ==================================================================== #

# =========== #
#   Imports   #
# =========== #
import os
import logging
import logging.handlers
    
# =========== #
#   Methods   #
# =========== #
def setup_custom_logger(name:str, directory:str="./", makeFolder:bool=False, loggingLevel:int=logging.DEBUG):
    """
    Initialize a logger

    :param name: Name of the logger to setup, use root for the global logger
    :type name: string
    :param directory: Directory to write the log file too, defaults to "./"
    :type directory: string, optional
    :param makeFolder: Create the directory if it is missing, defaults to False
    :type makeFolder: boolean, optional
    :param loggingLevel: Logging level to log at (use logging constants), defaults to logging.DEBUG
    :type loggingLevel: integer, optional
    :return: The created logger
    :rtype: Logger
    """    
    # logger settings
    log_file = f"{directory}script_generation.log"
    log_file_max_size = 1024 * 1024 * 20 # megabytes
    log_num_backups = 3
    log_format = "[%(levelname)s] %(message)s"
    log_filemode = "w" # w: overwrite; a: append
    
    # Create the folder if missing
    if not os.path.isdir(f"{directory}") and makeFolder:
        os.makedirs(f"{directory}")
    
    # setup logger
    logging.basicConfig(filename=log_file, format=log_format,
                        filemode=log_filemode, level=loggingLevel)
    rotate_file = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=log_file_max_size, backupCount=log_num_backups
    )
    logger = logging.getLogger(name)
    logger.addHandler(rotate_file)

    # print log messages to console
    consoleHandler = logging.StreamHandler()
    logFormatter = logging.Formatter(log_format)
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)
    return logger

def change_log_file(loggerName:str, newDir:str, makeFolder:bool=False):
    """
    Change the directory where the logger writes the log file

    :param name: Name of the logger to setup, use root for the global logger
    :type name: string
    :param newDir: Directory to write the log file too
    :type newDir: string
    :param makeFolder: Create the directory if it is missing, defaults to False
    :type makeFolder: boolean, optional
    """    
    # Create the folder if it is missing
    if not os.path.isdir(newDir) and makeFolder:
        os.makedirs(newDir)
    else: return
    
    # Prepare a new file    
    log_file_max_size = 1024 * 1024 * 20 # megabytes
    log_num_backups = 3
    rotate_file = logging.handlers.RotatingFileHandler(
            f"{newDir}scripts.log", maxBytes=log_file_max_size, backupCount=log_num_backups
        )
    logger = logging.getLogger(loggerName)
    logger.addHandler(rotate_file)
    
def print_pretty_sudoku(llMatrix):
    string = "___________________\n"
    for row in range(9):
        string += "|" + "|".join(llMatrix[row]) + "|\n"
        string += "|-+-+-+-+-+-+-+-+-|\n"
        
    print(string)

#import pathlib and time
from pathlib import Path
import time

#initialize file_path and file_exists
file_path = Path("~", "Documents", "questions.txt").expanduser()
file_exists: bool = None

#program checks if questions.txt exists, if so, set file_exists to True. Otherwise, False
if file_path.exists():
    file_exists = True

else:
    print("Error: questions.txt does not exist")
    time.sleep(1)
    print("Create a question file first, then run this program")
    file_exists = False

#define count_questions(file_path: str)
def count_questions():
    global file_path

    with open(file_path, "r") as file:
        content = file.read()
        return content.count("<question>")
#define get_question()
#define get_choices()
#define get_correct()
#define check_ans()
#define change_dir(new_file: str)
#initiate infinite while-loop
#create a menu with different options and features:
#show in the menu which file is currently opened
#show in the menu how many questions are contained in the file
#option: Ask random question; program asks a random question
#option: Ask all questions; still random, but asks all questions
#option: Quit program; breaks the loop and closes the program
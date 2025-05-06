#import pathlib and time
from pathlib import Path
import time
import random

#initialize file_path and file_exists
file_path = Path("~", "Documents", "questions_2.txt").expanduser()
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
    with open(file_path, "r") as file:
        content = file.read()
        return content.count("<question>")
    
#define get_question()
def get_question(code: int) -> str:
    with open(file_path, "r") as file:
        content = file.read()
        ques_index = content.find(f"<{code:b}> <question>")
        spec_ques = content[ques_index].replace(f"<{code:b}> <question>:", "")
        return spec_ques

#define get_choices()
def get_choices(code: int) -> list:
    choice_list = list()

    with open(file_path, "r") as file:
        content = file.read()
        choice_index = content.find(f"<{code:b}> <choice>")
        for i in range(4):
            choice_list.append(content[choice_index + i])
            choice_list[i].replace(f"<{code:b}> <choice>", "")
        
        return choice_list

            
#define get_correct()
def get_correct(code: int) -> str:
    with open(file_path, "r") as file:
        content = file.read()
        corr_index = content.find(f"<{code:b}> <correct>")
        return content[corr_index].replace(f"<{code:b}> <correct>", "")
    
#define check_ans()
def check_ans(user_input: str, correct: str) -> bool: 
    if user_input == correct:
        return True
    
    elif correct.startswith(user_input):
        return True
    
    else:
        return False

#define change_dir(new_file: str)
def change_dir(new_file: str):
    global file_path

    file_path = Path("~", "Documents", new_file + ".txt").expanduser()
    if file_path.exists():
        print(f"Moved to new file: {new_file + ".txt"}")
    
    else: 
        print(f"{new_file + ".txt"} does not exist, moving back to default directory...")
        file_path = Path("~", "Documents", "questions.txt").expanduser()

#define current_dir()
def current_dir() -> str:
    with open(file_path, "r") as file:
        return Path(file.name)

#initiate infinite while-loop
while file_exists: 
    local_count = count_questions()
    local_path = current_dir()
    ques_range = range(local_count)

    #Create the main menu:
    print(f"""
Welcome to the Quizzler!

File currently opened: {local_path}
There are {local_count} questions in this file.
Main Menu:

[1] Ask Random Question
[2] Ask All Questions
[3] Change Directory
[4] Quit Program
""")
    #Create prompt to choose among the given options
    while True:
        user_select = input("Select from the menu above!")
        if user_select.isnumeric and int(user_select) < 5:
            break
        else:
            continue
    
    user_select = int(user_select)

    #option: Ask random question; program asks a random question
    if user_select == 1:
        rand_ques_indx = random.choice(ques_range)
        print("Okay! Giving you a random question now: ")
        print(get_question(rand_ques_indx))

        for i in get_choices(rand_ques_indx):
            print(i)

        correct_ans = get_correct(rand_ques_indx)

        time.sleep(3)
        user_ans = input("Answer: ")

        if check_ans(user_ans, correct_ans):
            print("Very good! You answered correctly!")
        else:
            print(f"Sorry, your answer is wrong! The answer was: {correct_ans}")

    #option: Ask all questions; still random, but asks all questions
    #option: Change directory; change which file the program will access
    #option: Quit program; breaks the loop and closes the program
#import pathlib and time
from pathlib import Path
import time
import random

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
    with open(file_path, "r") as file:
        content = file.read()
        return content.count("<question>")
    
#define get_question()
def get_question(code: int) -> str:
    break_flag = False

    with open(file_path, "r") as file:
        content = file.readlines()

        for i in content:
            if i.startswith(f"<{code:b}> <question>"):
                spec_ques = i
                break_flag = True

            elif break_flag:
                break

            else:
                continue

        return spec_ques.replace(f"<{code:b}> <question>:", "")

#define get_choices()
def get_choices(code: int) -> list:
    choice_list = list()
    break_flag = False

    with open(file_path, "r") as file:
        content = file.readlines()
        
        for i in content: 
            if i.startswith(f"<{code:b}> <choice>"):
                choice_list.append(i.replace(f"<{code:b}> <choice>:", ""))
                break_flag = True
            
            elif break_flag:
                break

            else:
                continue
        
        return choice_list

            
#define get_correct()
def get_correct(code: int) -> str:
    break_flag = False

    with open(file_path, "r") as file:
        content = file.readlines()

        for i in content:
            if i.startswith(f"<{code:b}> <correct>"):
                correct_ans = i.replace(f"<{code:b}> <correct>:", "")
                break_flag = False
            
            elif break_flag:
                break

            else:
                continue
        
        return correct_ans
    
#define check_ans()
def check_ans(user_input: str, correct: str) -> bool: 
    if user_input == correct:
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
    local_ques_count = count_questions()
    local_path = current_dir()
    ques_range = range(1, local_ques_count + 1)

    #Create the main menu:
    print(f"""
Welcome to the Quizzler!

File currently opened: {local_path}
There are {local_ques_count} questions in this file.
Main Menu:

[1] Ask Random Question
[2] Ask All Questions
[3] Change Directory
[4] Quit Program
""")
    #Create prompt to choose among the given options
    while True:
        user_select = input("Select from the menu above!: ")
        if user_select.isnumeric() and int(user_select) < 5:
            break
        else:
            continue
    
    user_select = int(user_select)

    #option: Ask random question; program asks a random question
    if user_select == 1:
        rand_ques_code = random.choice(ques_range)
        print("Okay! Giving you a random question now: ")
        print(get_question(rand_ques_code))

        for i in get_choices(rand_ques_code):
            print(i)

        correct_ans = get_correct(rand_ques_code)

        time.sleep(3)
        user_ans = input("Choose your answer: ")

        if check_ans(user_ans, correct_ans):
            print("Very good! You answered correctly!")
        else:
            print(f"Sorry, your answer is wrong! The answer was: {correct_ans}")

    #option: Ask all questions; still random, but asks all questions
    elif user_select == 2:
        print("The program will now ask you all the questions in this file")
        time.sleep(1)
        print("There will be no particular flow in the asking of questions, all questions will be given at random.")
        time.sleep(1)
        print("Once all questions are asked, the session will end")
        time.sleep(1)
        print("Session begins now...")

        questions_asked = 0
        asked_codes = list()

        while questions_asked != local_ques_count:
            break_flag = False
            rand_ques_code = random.choice(ques_range)
            
            if rand_ques_code in asked_codes:
                continue

            else:
                print(get_question(rand_ques_code))
                for i in get_choices(rand_ques_code):
                    print(i)

                correct_ans = get_correct(rand_ques_code)
                asked_codes.append(rand_ques_code)
                questions_asked += 1

                time.sleep(3)
                user_input = input("Input your answer: ")

                if check_ans(user_input, correct_ans):
                    time.sleep(1)
                    print("Very good! Onto the next question!")

                else:
                    print(f"Your answer is wrong! The answer was {correct_ans}")
                    time.sleep(2)

                    while True: 
                        user_select = input("Continue session? (y/n): ")
                        if user_select.isalpha() and user_select == "y":
                            break

                        elif user_select.isalpha() and user_select == "n":
                            break_flag = True
                            print("Ending session...")
                            time.sleep(1)
                            break

                        else: 
                            continue
                
                if break_flag:
                    break


    #option: Change directory; change which file the program will access
    elif user_select == 3:
        print("If you want to change the file to access, it is recommended that you first create a text file with the quiz creator.")
        time.sleep(1)
        print("Input the name of the file you want to access (without the file extension or \".txt\")")
        time.sleep(1)
        file_change = input("File name: ")
        
        change_dir(file_change)
        print(f"Done! Moved to {current_dir()}")

    #option: Quit program; breaks the loop and closes the program
    elif user_select == 4:
        break

# A Python program acting as a Mock Test using OOP and functions 
# to access a .txt file with questions for the AWS Cloud Practitioner Test. 


import random as rd
from time import sleep

'''import sys, os
os.chdir(sys._MEIPASS)'''
# Uncomment this only when using pyinstaller to create .exe file

class Question():
    def __init__(self, question_text, answer1, answer2, answer3, answer4):
        self.question_text = question_text
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
    
    def get_question_text(self):
        return self.question_text
    
    def get_correct_answer(self):
        correct = self.answer1
        return correct
    
    def get_answer1(self):
        return self.answer1
    
    def get_answer2(self):
        return self.answer2
    
    def get_answer3(self):
        return self.answer3
    
    def get_answer4(self):
        return self.answer4
    
    def __str__(self):
        output = f"{GREEN}{self.question_text}\n"
        output += f"{BLUE}A: {PINK}{self.answer1}\n"
        output += f"{BLUE}B: {PINK}{self.answer2}\n"
        output += f"{BLUE}C: {PINK}{self.answer3}\n"
        output += f"{BLUE}D: {PINK}{self.answer4}{ENDC}"
        return output 



def random_qs_generator(num_q, max_value):
    """ Function returns a list with randomly generated unique numbers.
    Parameters: num_q (int), max_value (int).
    Returns: unique_nr (list) """
    
    unique_nr = []
    temp = rd.randint(1, max_value)
    
    for index in range(num_q):
        
        while temp in unique_nr:
            temp = rd.randint(1, max_value)
            
        unique_nr.append(temp)
    
    return unique_nr


def quiz():
    """ Function prints out the questions and calculates the score.
    Parameters: None
    Returns: None """
    
    while True:
        try:
            number_Qs = int(input(f"{ENDC}Enter how many questions you would like (max {total_nr_questions}): {CYAN}"))
            if number_Qs < 1 or number_Qs > total_nr_questions:
                raise Exception(f"{RED}Sorry, not valid. Please enter number between 1 and {total_nr_questions}.")
            else:
                break
        except Exception as error:
            print(f"{EM} {error} Let's try again.")
    
    print(f"\n{ENDC}I will ask you {PURPLE}{number_Qs} questions {ENDC}on {LIGHTCYAN}AWS Cloud Practitioner{ENDC}. Let's proceed...\n")
    sleep(2)

    questions_to_display = random_qs_generator(number_Qs, total_nr_questions)
    
    score = 0
    question_nr = 0
    
    while True:
        question_nr += 1
        number = str(question_nr)
        if question_nr < 10:
            number = " " + number
        title = f'''
            {BLUE}╔{'═' * 19}╗
            ║{PURPLE}**{GREEN}  QUESTION {number}  {PURPLE}**{BLUE}║
            ╚{'═' * 19}╝{ENDC}\n'''
        print(title)
        
        current_q = quest_list[questions_to_display[question_nr-1]-1]
        answers_order = [current_q.get_answer1(), 
                        current_q.get_answer2(), 
                        current_q.get_answer3(), 
                        current_q.get_answer4()]
        rd.shuffle(answers_order)
        
        output = f'''{CYAN}{current_q.get_question_text()}
            {YELLOW}A: {PINK}{answers_order[0]}
            {YELLOW}B: {PINK}{answers_order[1]}
            {YELLOW}C: {PINK}{answers_order[2]}
            {YELLOW}D: {PINK}{answers_order[3]}{ENDC}'''
        print(output) 
        
        while True:
            try:
                letter = input(f"Your answer: {LIGHTCYAN}").upper()
                if letter == "A" or letter == "B" or letter == "C" or letter == "D":
                    break
                else:
                    raise Exception("Sorry, not valid. Please enter 'A', 'B', 'C' or 'D'.")
            except Exception as error:
                print(f"{EM} {error} Let's try again.")
        
        if letter == 'A':
            answer = answers_order[0]
        elif letter == 'B':
            answer = answers_order[1]
        elif letter == 'C':
            answer = answers_order[2]
        elif letter == 'D':
            answer = answers_order[3]
        
        if answer == current_q.get_correct_answer():
            print(f"{LIGHTGREEN}That was correct, {username}!")
            score += 1
        else:
            print(f"{LIGHTRED}Sorry {username}, wrong answer.{ENDC}")
        
        if question_nr == number_Qs:
            print(f"{LIGHTBLUE}\nLet's see how you've done, {username}... {ENDC}")
            print(f"You answered correctly {GREEN}{score}{ENDC} out of {BLUE}{number_Qs}{ENDC} questions.")
            final = round(score/number_Qs*100)
            if final < 70:
                print(f"Your score is: {RED}{final}% \nYou failed. :({ENDC}")
            else:
                print(f"Your score is: {LIGHTGREEN}{final}% \nYou passed!{ENDC}")
            break


def read_questions_data():
    """ Function reads the questions file and saves the contents as objects.
    Parameters: None
    Returns: None """
    
    try:
        with open('questions.txt', 'r', encoding='utf-8') as questions:
            for line in questions:                
                q_data = line.strip().split(";")
                quest = Question(q_data[0], q_data[1], q_data[2], 
                                q_data[3], q_data[4])
                quest_list.append(quest)
                # Saving each question 1 by 1 from file as objects 
                # and adding them all to the 'quest_list'.
    except FileNotFoundError:
        print(f"\n{EM} Questions file not found.")
    except IndexError:
        print(f"{EM} Questions file has been {RED}corrupted{ENDC}.",
            f"Please check file contents and try again.")



# Some formatting shortcuts:
RED = '\033[31m'
LIGHTRED = '\033[91m'
GREEN = '\033[32m'
LIGHTGREEN = '\033[92m'
YELLOW = '\033[33m'
LIGHTYELLOW = '\033[93m'
BLUE = '\033[34m'
LIGHTBLUE = '\033[94m'
PURPLE = '\033[35m'
PINK = '\033[95m'
CYAN = '\033[36m'
LIGHTCYAN = '\033[96m'
ENDC = '\033[0m'  # Removes all formatting applied.
EM = f"{RED}‼{ENDC}"  # 'Exclamation Mark' shorthand


title = f'''
    {PINK}╔{'═'*34}╗
    ║{PURPLE}**{CYAN} Cloud Practitioner Mock Test {PURPLE}**{PINK}║
    ╚{'═'*34}╝{ENDC}
    '''
print(title)
# This will print out the title.

print(f'''Welcome to your {PURPLE}Mock Test{ENDC}. 
        Let's test your {GREEN}knowledge!{ENDC}''')
username = input(f"\nFirst, enter your name: {CYAN}").capitalize()
# Getting the user's name and starting the test. 

print(f"{ENDC}\nGreat stuff, {PINK}{username}{ENDC}. {LIGHTYELLOW}Now let's get started.{ENDC}\n")

quest_list = []
# This list will contain all the questions for the quiz as objects.
user_choice = 'yes'

read_questions_data()
# This will read the 'questions.txt' file and save the questions.

total_nr_questions = len(quest_list)

while user_choice == 'yes':
    quiz()
    while True:
        try:
            user_choice = input(f"\nTake the test again? yes/no: {LIGHTCYAN}").lower()
            if user_choice != "yes" and user_choice != "no":
                raise Exception("Sorry, not valid. Please enter 'yes' or 'no'.")
            else:
                break
        except Exception as error:
            print(f"{EM} {error} Let's try again.")
    if user_choice == 'no':
        print(f"\n {ENDC}Okay, {LIGHTRED}goodbye{ENDC}.\n")
        break
    else:
        print(f"{GREEN}\nLet's start the Quiz again! {ENDC}\n")

sleep(2)
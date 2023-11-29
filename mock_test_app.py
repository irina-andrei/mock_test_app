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
        # The for loop will keep running until it fills 'unique_nr' 
        # with random unique numbers.
        while temp in unique_nr:
            temp = rd.randint(1, max_value)
        unique_nr.append(temp)
    
    return unique_nr


def quiz():
    """ Function prints out the questions and calculates the score.
    Parameters: None
    Returns: None """
    
    print(f"There are {LIGHTRED}{total_nr_questions} different questions available{ENDC}.")
    while True:
        try:
            number_Qs = int(input(f"{ENDC}Enter how many questions you would like to answer: {CYAN}"))
            if number_Qs < 1 or number_Qs > total_nr_questions:
                raise Exception(f"{RED}Sorry, not valid. Please enter number between 1 and {total_nr_questions}.")
            else:
                break
        except Exception as error:
            print(f"{EM} {error} Let's try again.")
        # The try/except will catch any wrong inputs from user.
        # The while loop will keep running until the user enters an acceptable number.
    
    print(f"\n{ENDC}I will ask you {PURPLE}{number_Qs} questions {ENDC}on {LIGHTCYAN}AWS Cloud Practitioner{ENDC}. Let's proceed...\n")
    sleep(2)
    
    questions_to_display = random_qs_generator(number_Qs, total_nr_questions)
    # This will be the list containing the order in which the questions are displayed.
    
    score = 0
    # The total score for the user.
    question_nr = 0
    # The tally for the questions while it goes through the while loop.
    
    while True:
        question_nr += 1
        number = str(question_nr)
        
        if question_nr < 10:
            number = " " + number + " "
        elif question_nr < 100:
            number = number + " "
        # By having this string and adding a space to it, it makes
        # sure that the number will be displayed correctly inside title. 

        title = f'''
            {BLUE}╔{'═' * 19}╗
            ║{PURPLE}**{GREEN}  QUESTION {number} {PURPLE}**{BLUE}║
            ╚{'═' * 19}╝{ENDC}\n'''
        print(title)
        
        current_q = quest_list[questions_to_display[question_nr-1]-1]
        # This will contain the current question as an Object.
        
        answers_order = [current_q.get_answer1(), 
                        current_q.get_answer2(), 
                        current_q.get_answer3(), 
                        current_q.get_answer4()]
        # A list that will contain the 4 answers to the question.
        rd.shuffle(answers_order)
        # This will shuffle the list of answers, making sure they will always
        # be displayed in a random order and not as before.
        
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
            # The try/except will catch any wrong inputs from user.
            # The while loop will keep running until the user enters an acceptable answer.
        
        if letter == 'A':
            answer = answers_order[0]
        elif letter == 'B':
            answer = answers_order[1]
        elif letter == 'C':
            answer = answers_order[2]
        elif letter == 'D':
            answer = answers_order[3]
        # Associating the user's answer with the correct position in the list.
        
        if answer == current_q.get_correct_answer():
            # Getting the correct answer from the Object and comparing 
            # it to the user's answer.
            print(f"{LIGHTGREEN}That was correct, {username}!")
            score += 1
            sleep(2)
        else:
            print(f"{LIGHTRED}Sorry {username}, wrong answer.{ENDC}")
            sleep(2)
        
        if question_nr == number_Qs:
            # If this condition is True, it means it has reached the last 
            # question and we can print the results.
            print(f"{PURPLE}\n\nThat was the last question!{ENDC}")
            print(f"{LIGHTBLUE}Let's see how you've done, {username}... {ENDC}")
            print(f"You answered correctly {GREEN}{score}{ENDC} out of {PINK}{number_Qs}{ENDC} questions.")
            
            final = round(score/number_Qs*100)
            print(f"Your score is...")
            
            final_score = str(final)
            if final < 10:
                final_score = "  " + final_score
            elif final <100:
                final_score = " " + final_score
            # By having this string and adding a space to it, it makes
            # sure that the number will be displayed correctly inside title.  
            
            if final < 70:
                final_text = f"\t{LIGHTRED}Sorry, you failed. :({ENDC}"
                COLOUR1 = RED
                COLOUR2 = LIGHTRED
            else:
                #{LIGHTGREEN}{final}% \n
                final_text = f"\t{LIGHTGREEN}Congrats, you passed! :){ENDC}"
                COLOUR1 = GREEN
                COLOUR2 = LIGHTGREEN
            
            score_title = f'''
            {COLOUR1}╔{'═' * 9}╗
            ║  {COLOUR2}{final_score}% {COLOUR1}  ║
            ╚{'═' * 9}╝{ENDC}\n'''
            print(score_title)
            print(final_text)
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
    # The try/except will make sure the program still runs even if it 
    # encounters an error. In that case, instead of the program crashing, it 
    # will print the specific error on the screen for the user.



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
# This will be the total number of questions found in 'questions.txt' and 
# saved as Objects inside the 'quest_list'.

while user_choice == 'yes':
    quiz()
    # Running the quiz.
    
    while True:
        try:
            user_choice = input(f"\nDo you want to take the test again? yes/no: {LIGHTCYAN}").lower()
            if user_choice != "yes" and user_choice != "no":
                raise Exception("Sorry, not valid. Please enter 'yes' or 'no'.")
            else:
                break
        except Exception as error:
            print(f"{EM} {error} Let's try again.")
        # The try/except will catch any wrong inputs from user.
        # The while loop will keep running until the user enters 'yes' or 'no'.
    
    if user_choice == 'no':
        print(f"\n {ENDC}Okay, {LIGHTRED}goodbye{ENDC}.\n")
        break
    else:
        print(f"{GREEN}\nLet's start the Quiz again! {ENDC}\n")

sleep(2)

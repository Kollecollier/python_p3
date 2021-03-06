import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_project_sheet')

score_sheet = SHEET.worksheet('store_correct1')


questions = [
    {
        "question": "What is RAM short for?",
        "options": [
            "a) Random Memory",
            "b) Random Access",
            "c) Random Access Memory",
            "d) Access Memory"
        ],
        "correct_answer": "c"
    },
    {
        "question": "What is GPU short for?",
        "options": [
            "a) Graphical Processing Unit",
            "b) Random Access",
            "c) Random Access Memory",
            "d) Access Memory"
            ],
        "correct_answer": "a"
    },
    {
        "question": "What is SSD short for?",
        "options": [
            "a) Random Memory",
            "b) Solid State Drive",
            "c) Random Access Memory",
            "d) Access Memory"
            ],
        "correct_answer": "b"
    },
    {
        "question": "What is PSU short for?",
        "options": [
            "a) Random Memory",
            "b) Random Access",
            "c) Random Access Memory",
            "d) Power Supply Unit"
            ],
        "correct_answer": "d"
    }
]


def ask_to_play():
    """
    This function defines the start of the game
    """
    print('Welcome to my computer quiz!\n')
    play = input('Do you want to play? Yes or No ?\n').lower()
    if play == "yes":
        start_game()
    else:
        print("To bad maybe next time?")


def start_game():
    """
    Giving the user a feedback comment and also engageing the quiz
    """
    user_name = input("Please enter your name:")
    print("-----------------\nOkej! Let's play 😊!\n-----------------")
    start_quiz(user_name)


def update_score_to_sheet(score, user_name):
    """
    This funtion is coded to provide scores to the googlesheet
    """
    no_of_rows = len(score_sheet.col_values(1))
    score_sheet.update_cell(no_of_rows+1, 1, user_name)
    score_sheet.update_cell(no_of_rows+1, 2, score)


def start_quiz(user_name):
    """
    Here the quiz begins after all the correct user inputs
    """
    score = 0

    for question in questions:
        print(question["question"])
        question_options = question["options"]
        for option in question_options:
            print(option)
        user_choice = input('Enter either a/b/c/d:\n').lower()
        if user_choice == question["correct_answer"]:
            score += 1
            print("-----------------\nCorrect! Well done😊!!\n----------------")
            end_game()
        else:
            print("Sorry its wrong!!\n")
            user_choice = input('Try again?\n').lower()
            if user_choice == ('yes'):
                start_quiz(user_name)
            if user_choice != ('yes'):
                end_game()

    update_score_to_sheet(score, user_name)


def end_game():
    """
    This ends the game and provides user a thank you and some information
    """
    print("Thank you for playing my first python quiz game\n")
    print("Your score has been added to the scoreboard\n")
    print("You can find the scoreboard in the README.md file! 😊")


ask_to_play()

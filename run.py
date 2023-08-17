# Percy Jackson's Quiz - Conception:
# Ask user's name
# - Avoid user from put non-alphabetical characters and a name of any length
# - Ask for user to start the game by him/herserlf
# Load questions
# Receive answers and value them
# - Refrain user from put anything as answer; Accpecting A, B, C or D as answer
# Finish the quiz informing the score and asking about restart

import time


def get_valid_name():
    while True:
        name = input("First of all, what's your name? ")
        if name.isalpha() and 2 <= len(name) <= 10:
            return name
        else:
            print("Hey, it's an invalid name! Only alphabetic characters.")


def get_user_answer():
    while True:
        user_input = input("Choose between (A, B, C, or D): ").upper()
        if user_input in ['A', 'B', 'C', 'D']:
            return user_input
        else:
            print("Hey! It's an invalid option! It may be A, B, C, or D.")


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}.\n")
        return 0


def run_quiz(questions, alternatives, correct_answers, user_name):
    score = 0
    for i in range(len(questions)):
        print(f"\nQuestion {i+1}: {questions[i]}")
        for option in alternatives[i]:
            print(option)

        user_input = get_user_answer()
        score += check_answer(user_input, correct_answers[i])
    
    time.sleep(1)
    print("Bravo!! We're now counting your score\n")

    time.sleep(2)

    if score == 5:
        print(f"Well done, {user_name}! You nailed it! Scored 5/5")
    else:
        print(f"""Thank you for participating, {user_name}!
You can improve next time... Your score was {score}/5""")


def main():
    print(
        """
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                  @@#((#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((@@
                  @@(((*(((((@@@@@@@@@@@@@@@@@@@(((((,((,@
                  @@(((.....(((((@@@@@@@@@@@#(((/.....((@@
                  @@@((........*(((((((((((((,.......(((@@
                  @@@(((.../(((((((((((((((((((((,..*((@@@
                  @@@@(((((((/....(((((((((....(((((((&@@@
                  @@@@@(((((...&&*..(((((..#&#...(((((@@@@
                  @@@#(((((...*&&&..((((/..&&&...*(((((@@@
                  @@@@(((((,........(((((......../((((&@@@
                  @@@(*............(((((((............/(@@
                  @@(((............(((((((............(((@
                  @@@@((((@((((....&&&&&&&....(((@@((((@@@
                  @@@@@@@@@@@@((.....&&&.....(#@@@@@@@@@@@
                  @@@@@@@@@@@@@@(((((((((((((@@@@@@@@@@@@@
                  @@@@@@@@@@@@@@@@@@(((((@@@@@@@@@@@@@@@@@
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        """
    )
    print("""Test your knowledge about the three first books of Percy Jackson
with the next 5 questions!\n""")
    user_name = get_valid_name()
    print(f"Welcome, {user_name}! Let's start? (press Y for yes)")
    answer_user = input("Any other key will cancel the quiz ").upper()

    if answer_user != "Y":
        print(f"Ok, {user_name} I hope to see you again")
        quit()
    else:
        print("Starting...")
        time.sleep(1)
    
    questions = [
        "Why is Percy declared 'undetermined' when he first gets to camp?",
        "In 'the Lightning Thief', why is Percy wanted in the mortal world?",
        """What is the name for the monsters that attacked Percy in the
beginning of the book 'Sea of Monsters'?""",
        """When Percy asked what they meant about the 'location he seeks', what
did the gray sisters say?""",
        "Why didn't Phoebe get to go on the mission with the other demi-gods?"
    ]

    alternatives = [
        ["A: He is new to the camp",
            "B: They do not know which sport he will be good at",
            "C: They do not know which God is his father",
            "D: They can't tell if he is good or evil"],
        ["A: He is thought to be a runaway",
            "B: For the disappearance of his mother",
            "C: For the disappearance of Mr. Brunner",
            "D: For the disappearance of Mrs. Dodds"],
        ["A: Cyclops", "B: Minotaur",
            "C: Laistrygonians", "D: Hydra"],
        ["A: Miami Florida", "B: Bermuda Triangle",
            "C: Sea of Monsters", "D: 30, 31, 75, 12"],
        ["A: She got pranked when she was given a T-Shirt, it made her sick",
            "B: She did go on the mission", "C: She lost her shoes",
            "D: She got food poisoning"]
    ]

    correct_answers = ['C', 'B', 'C', 'D', 'A']

    while True:
        run_quiz(questions, alternatives, correct_answers, user_name)

        play_again = input("Do you want to retry? (press Y for yes): ").upper()
        if play_again != "Y":
            print(f"Thank you, {user_name}! Keep listening us in Spotify")
            break


if __name__ == "__main__":
    main()

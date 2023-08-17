# Percy Jackson's Quiz - Conception:
# Ask user's name
# - Avoid user from put non-alphabetical characters and a name of any length
# - Ask for user to start the game by him/herserlf
# Load questions
# Receive answers and value them
# - Refrain user from put anything as answer; Accpecting A, B, C or D as answer
# Finish the quiz informing the score and asking about restart

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

        """
    )
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

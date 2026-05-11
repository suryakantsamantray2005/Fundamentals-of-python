import random

class Flashcard:

    def __init__(self):
        self.score = 0

    def frontpage(self):
        print("WELCOME TO MINDQUIZ !!")

    def quiz(self):

        self.score = 0

        levels = {

            "easy": {

                "fruits": {

                    "banana": "yellow",
                    "apple": "red",
                    "watermelon": "green",
                    "orange": "orange",
                    "blueberry": "blue",
                    "mango": "yellow",
                    "strawberry": "red",
                    "pineapple": "yellow",
                    "grapes": "green",
                    "papaya": "orange",
                    "guava": "green",
                    "cherry": "red",
                    "kiwi": "green",
                    "lemon": "yellow",
                    "peach": "pink",
                    "pear": "green",
                    "plum": "purple",
                    "pomegranate": "red",
                    "coconut": "brown",
                    "dragonfruit": "pink"

                },

                "animals": {

                    "lion": "wild",
                    "cow": "domestic",
                    "dog": "domestic",
                    "tiger": "wild",
                    "cat": "domestic",
                    "elephant": "wild",
                    "goat": "domestic",
                    "horse": "domestic",
                    "zebra": "wild",
                    "camel": "domestic",
                    "fox": "wild",
                    "rabbit": "domestic",
                    "wolf": "wild",
                    "deer": "wild",
                    "buffalo": "domestic",
                    "monkey": "wild",
                    "pig": "domestic",
                    "bear": "wild",
                    "donkey": "domestic",
                    "giraffe": "wild"

                }

            },

            "medium": {

                "science": {

                    "H2O": "water",
                    "NaCl": "salt",
                    "CO2": "carbon dioxide",
                    "O2": "oxygen",
                    "Sun": "star",
                    "Earth": "planet",
                    "Moon": "satellite",
                    "plants": "oxygen",
                    "Fe": "iron",
                    "Au": "gold",
                    "Ag": "silver",
                    "Cu": "copper",
                    "He": "helium",
                    "N": "nitrogen",
                    "Mg": "magnesium",
                    "K": "potassium",
                    "Ca": "calcium",
                    "Zn": "zinc",
                    "Pb": "lead",
                    "Sn": "tin"

                },

                "maths": {

                    "2+2": "4",
                    "5x5": "25",
                    "10/2": "5",
                    "9-3": "6",
                    "12+8": "20",
                    "7x6": "42",
                    "15-5": "10",
                    "18/3": "6",
                    "9x9": "81",
                    "100/10": "10",
                    "11+11": "22",
                    "8x7": "56",
                    "14+6": "20",
                    "20-8": "12",
                    "6x6": "36",
                    "81/9": "9",
                    "13+7": "20",
                    "16-4": "12",
                    "3x9": "27",
                    "49/7": "7"

                }

            },

            "hard": {

                "capitals": {

                    "India": "delhi",
                    "Japan": "tokyo",
                    "France": "paris",
                    "China": "beijing",
                    "USA": "washington",
                    "Russia": "moscow",
                    "Germany": "berlin",
                    "Italy": "rome",
                    "Nepal": "kathmandu",
                    "Australia": "canberra",
                    "Canada": "ottawa",
                    "Brazil": "brasilia",
                    "Spain": "madrid",
                    "Egypt": "cairo",
                    "Thailand": "bangkok",
                    "Argentina": "buenos aires",
                    "Mexico": "mexico city",
                    "South Korea": "seoul",
                    "Turkey": "ankara",
                    "Indonesia": "jakarta"

                },

                "chemistry": {

                    "Na": "sodium",
                    "Au": "gold",
                    "Fe": "iron",
                    "H": "hydrogen",
                    "O": "oxygen",
                    "K": "potassium",
                    "Ca": "calcium",
                    "Mg": "magnesium",
                    "Ag": "silver",
                    "Cu": "copper",
                    "Zn": "zinc",
                    "Pb": "lead",
                    "Sn": "tin",
                    "Hg": "mercury",
                    "Cl": "chlorine",
                    "Br": "bromine",
                    "I": "iodine",
                    "Al": "aluminium",
                    "Ni": "nickel",
                    "Co": "cobalt"

                }

            }

        }

        print("\nSELECT LEVEL")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        level_choice = int(input("Enter your choice: "))

        if level_choice == 1:

            selected_level = levels["easy"]

            print("\nSELECT CATEGORY")
            print("1. Fruits")
            print("2. Animals")

            category_choice = int(input("Enter your choice: "))

            if category_choice == 1:

                selected_questions = selected_level["fruits"]
                question_type = "What is the colour of"

            elif category_choice == 2:

                selected_questions = selected_level["animals"]
                question_type = "Is this animal domestic or wild ->"

            else:
                print("Invalid choice")
                return

        elif level_choice == 2:

            selected_level = levels["medium"]

            print("\nSELECT CATEGORY")
            print("1. Science")
            print("2. Maths")

            category_choice = int(input("Enter your choice: "))

            if category_choice == 1:

                selected_questions = selected_level["science"]
                question_type = "What is the chemical/common name of"

            elif category_choice == 2:

                selected_questions = selected_level["maths"]
                question_type = "What is the value of"

            else:
                print("Invalid choice")
                return

        elif level_choice == 3:

            selected_level = levels["hard"]

            print("\nSELECT CATEGORY")
            print("1. Capitals")
            print("2. Chemistry")

            category_choice = int(input("Enter your choice: "))

            if category_choice == 1:

                selected_questions = selected_level["capitals"]
                question_type = "What is the capital of"

            elif category_choice == 2:

                selected_questions = selected_level["chemistry"]
                question_type = "What element is represented by"

            else:
                print("Invalid choice")
                return

        else:
            print("Invalid level")
            return

        question_list = random.sample(list(selected_questions.keys()), 5)

        for i in range(5):

            key = question_list[i]

            print("\nQuestion", i + 1)
            print(question_type, key, "?")

            ans = input("Enter answer: ").lower()

            if ans == selected_questions[key]:

                print("Correct answer")
                self.score += 1

            else:

                print("Wrong answer")
                print(selected_questions[key], "is the correct answer")

        print("\nQuiz Finished")
        print("Final Score =", self.score, "/5")

        print("\nWant to play again? PRESS 0")

        user_input = int(input())

        if user_input == 0:
            self.quiz()


f1 = Flashcard()

f1.frontpage()

f1.quiz()
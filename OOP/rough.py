class FlashCard:

    def __init__(self):
        self.score = 0

    def frontpage(self):
        print("Welcome to FlashMind Quiz!!")

    def quiz(self):

        levels = {

            "easy": {

                "fruits": {
                    "banana":"yellow",
                    "apple":"red"
                },

                "animals": {
                    "dog":"pet",
                    "lion":"wild"
                },

                "colors": {
                    "sky":"blue",
                    "grass":"green"
                }
            },

            "medium": {

                "countries": {
                    "india":"delhi",
                    "japan":"tokyo"
                },

                "science": {
                    "h2o":"water",
                    "co2":"carbon dioxide"
                },

                "sports": {
                    "cricket":"bat",
                    "football":"goal"
                }
            },

            "hard": {

                "programming": {
                    "python":"language",
                    "html":"markup"
                },

                "chemistry": {
                    "na":"sodium",
                    "au":"gold"
                },

                "mathematics": {
                    "pi":"3.14",
                    "square root of 16":"4"
                }
            }
        }

        print("\nChoose Level:")
        print("easy")
        print("medium")
        print("hard")

        level_choice = input("Enter level: ").lower()

        if level_choice not in levels:
            print("Invalid level")
            return

        print("\nChoose Category:")

        for category in levels[level_choice]:
            print(category)

        category_choice = input("Enter category: ").lower()

        if category_choice not in levels[level_choice]:
            print("Invalid category")
            return

        selected_questions = levels[level_choice][category_choice]

        import random

        for i in range(5):

            key = random.choice(list(selected_questions.keys()))

            print("\nQuestion", i + 1)
            print("What is related to", key, "?")

            ans = input("Enter answer: ").lower()

            if ans == selected_questions[key]:

                print("Correct answer")
                self.score += 1

            else:

                print("Wrong answer")
                print(selected_questions[key], "is correct")

        print("\nQuiz Finished")
        print("Final Score =", self.score, "/5")


f1 = FlashCard()

f1.frontpage()

f1.quiz()
import random

# Random Joke Generator with No Repetition
def joke_generator():
    jokes = [
        "Why did the Nigerian student bring a ladder to school? Because he heard it was high school!",
        "What did the suya seller say to the bank? 'I’m here to pepper my account balance!'",
        "Why did the yam refuse to get cooked? Because it didn’t want to be pounded!",
        "What did the Nigerian traffic light say to the car? 'Stop looking at me like I’m NEPA, I won’t go off!'",
        "Why don’t Nigerians tell secrets in a party? Because even the wall has ears and might start gisting!"
    ]

    random.shuffle(jokes)
    for joke in jokes:
        print(joke)
        input("\nPress Enter for the next joke...")

    print("That's all the jokes for now! 😄")

joke_generator()

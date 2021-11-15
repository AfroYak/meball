import random
from termcolor import COLORS, colored


RESPONSES = {
    "msgs": [
        ("It is certain.", 0),
        ("It is decidedly so.", 0),
        ("Without a doubt.", 0),
        ("Yes – definitely.", 0),
        ("You may rely on it.", 0),
        ("As I see it, yes.", 0),
        ("Most likely.", 0),
        ("Outlook good.", 0),
        ("Yes.", 0),
        ("Signs point to yes.", 0),
        ("Reply hazy, try again.", 1),
        ("Ask again later.", 1),
        ("Better not tell you now.", 1),
        ("Cannot predict now.", 1),
        ("Concentrate and ask again.", 1),
        ("Don’t count on it.", 2),
        ("My reply is no.", 2),
        ("My sources say no.", 2),
        ("Outlook not so good.", 2),
        ("Very doubtful.", 2),
    ],
    "colors": ["green", "yellow", "red"],
}


def get_response():
    """Generates and Returns a Random Response based on the Magic 8 Ball game."""

    (response, idx_color) = random.choice(RESPONSES["msgs"])
    return colored(response, RESPONSES["colors"][idx_color], attrs=["bold"])


def print_response():
    """Prints a Random Response based on the Magic 8 Ball RESPONSES"""
    print(get_response())
    return None


def try_me():
    """Plays one round"""
    wise_bold = colored("WISE", attrs=["bold"])
    user_input = input(
        f"\nWhat would you like to ask the great {wise_bold} magic ball?\n"
    )
    print_response()
    return user_input


if __name__ == "__main__":
    print(get_response())

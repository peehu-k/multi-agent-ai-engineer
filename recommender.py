import random
import os

def suggest_next():
    ideas = [
        "build log analyzer",
        "build ai file organizer",
        "build password strength checker",
        "build system monitor tool",
        "build automation script generator",
        "build data cleaner toolkit",
        "build code profiler",
        "build terminal productivity suite"
    ]

    return random.choice(ideas)

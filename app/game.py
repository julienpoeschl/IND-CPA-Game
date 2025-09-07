import parser
import cryptography

import random


def start_game() -> None:
    """Starts game loop"""


    print("")
    score = 0
    rounds_played = 0
    while True:
        
        print(f"Round {rounds_played + 1}")
        print("--------------------------")

        m1 = ""
        m2 = ""
        while m1 == m2:
            m1 = input("Input M_1: ")
            m2 = input("Inpu M_2: ")
            if m1 == m2:
                print("M_1 and M_2 must be distinct.")

        m1_length = len(m1)
        m2_length = len(m2)

        m_length_diff = abs(m1_length - m2_length)
        
        if m1_length > m2_length:
            print("Padding M_2 with zeros.")
            for _ in range(m_length_diff):
                m2 += "0"
        elif m2_length > m1_length:
            print("Padding M_1 with zeros.")
            for _ in range(m_length_diff):
                m1 += "0"

        m1 = parser.to_bytes(m1)
        m2 = parser.to_bytes(m2)

        m1 = cryptography.encrypt(m1)
        m2 = cryptography.encrypt(m2)

        rand = random.randint(1, 2)

        if rand == 1:
            print(f"M_x: {str(m1)}")
        else:
            print(f"M_x: {str(m2)}")

        guess = ""
        while guess not in (1, 2):
            guess = int(input("Guess: "))
            if guess not in (1, 2):
                print("Guess must be 1 or 2.")
        
        if guess == rand:
            print("You have guessed correctly!")
            score += 1
        else:
            print("You have guessed incorrectly!")
        
        rounds_played += 1
        
        print("--------------------------")
        print(f"Score: {score}")
        print(f"Rounds: {rounds_played}")
        print(f"Probability: {float(score)/float(rounds_played)}")
        print("--------------------------")
        print("")

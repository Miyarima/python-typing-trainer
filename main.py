#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is the main program.
"""

import type_tester as tt
import present_score as ss
import random_character as rc

def main():
    """
    The main loop of the program.
    """

    while True:
        
        tt.meny()
        choice = input(">>> ")

        if choice == "q":
            print("Bye!")
            break
        elif choice == "1":
            tt.train("easy.txt", "easy")
        elif choice == "2":
            tt.train("medium.txt", "medium")
        elif choice == "3":
            tt.train("hard.txt", "hard")
        elif choice == "4":
            ss.print_scores()
        elif choice == "5":
            rc.random_training()
        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()

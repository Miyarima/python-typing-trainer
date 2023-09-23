#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains a function
that gives you are character you
need to type.
"""

import random as rand
import time
import type_tester as tt

def random_training():
    """
    This function contains a while
    loop which presents a random character
    the player has to type, and later prints
    the result. 
    """
    tt.clear_terminal()
    wrong_chars = {}
    total_amount_of_chars = []
    try:
        traing_dur = input("How long would you like to train for(sec)?: ")
        traing_dur = int(traing_dur) + time.time()

        tt.clear_terminal()
        start = time.time()
        while time.time() < traing_dur:
            char = rand.randint(43,122)
            print(f"Durration left: {traing_dur - time.time()}")
            print(f"{chr(char)}")
            user_input = input(">>> ")
            if user_input != chr(char):
                if user_input in wrong_chars:
                    wrong_chars[user_input] += 1
                else:
                    wrong_chars[user_input] = 1
            total_amount_of_chars.append(user_input)
            tt.clear_terminal()
        stop = time.time()

        total_time_sec = stop - start
        amount_of_wrong_chars = tt.return_amount_of_wrong_chars(wrong_chars)
        wrong_char_tuple_lst = tt.dict_to_list_tuple_pair(wrong_chars)

        tpm = round(len(total_amount_of_chars) / (total_time_sec / 60), 1)
        percent_wrong = round((amount_of_wrong_chars / len(total_amount_of_chars)) * 100, 2)

        print("Well done! Your practice is over.")
        print(wrong_char_tuple_lst)
        print(f"procent fel: {percent_wrong}%")
        print(f"TPM: {tpm}")

    except ValueError:
        print("Please enter the time correctly.")

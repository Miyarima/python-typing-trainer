#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a module which cotains a few
function that together creates a simple
type tester program by giving it a file
and how hard the file is.
"""

import os
import time

def meny():
    """
    Displays all available commands.
    """
    meny_text = r"""
[Task]           [Command]

Train easy       | 1
Train medium     | 2
Train hard       | 3
See high score   | 4
Train            | 5
Quit             | q
    """
    print(meny_text)

def clear_terminal():
    """
    Clears the terminal when called.
    """
    os.system('cls' if os.name=='nt' else 'clear')

def get_content(filename):
    """
    Opens the file, and puts each
    line into a variable, and returns
    it.
    """
    with open(filename) as f:
        file_content = f.readlines()
    return file_content

def get_words(content):
    """
    Takes the words from the input and
    retuns a list with every word as
    an element of the list.
    """
    words = []
    word = ""
    for row in content:
        for char in row:
            if char in [" "]:
                words.append(word)
                word = ""
            if char not in ["\n", " "]:
                word += char
        words.append(word)
        word = ""
    return words

def remove_new_lines(content):
    """
    Takes in a list and removes
    new-lines on the elements.
    """
    added_new_lines = []
    for row in content:
        if "\n" in row:
            row = row[:-1]
            added_new_lines.append(row)
        else:
            added_new_lines.append(row)
    return added_new_lines

def compare_strings(file_sentences, user_sentences):
    """
    Takes in two arguments and compares
    each character. eg. first character in
    the first argument, compared to the first
    character in the second argument.
    """
    wrong_chars = {}
    # for i in range(len(file_sentences)):
    for i, _ in enumerate(file_sentences):
        len_file = len(file_sentences[i])
        len_user = len(user_sentences[i])
        lst_lenght = len_file if len_file > len_user else len_user
        for char in range(lst_lenght):
            try:
                if file_sentences[i][char] != user_sentences[i][char]:
                    letter = file_sentences[i][char]
                    if letter in wrong_chars:
                        wrong_chars[letter] += 1
                    else:
                        wrong_chars[letter] = 1
            except IndexError:
                if len_file > len_user:
                    letter = file_sentences[i][char]
                    if letter in wrong_chars:
                        wrong_chars[letter] += 1
                    else:
                        wrong_chars[letter] = 1
                else:
                    letter = user_sentences[i][char]
                    if letter in wrong_chars:
                        wrong_chars[letter] += 1
                    else:
                        wrong_chars[letter] = 1

    return wrong_chars

def dict_to_list_tuple_pair(dict_to_convert):
    """
    Takes in a dictinary and adds the
    key and value as a tuple into a list
    """
    sorted_dict = {}
    sorted_lst = sorted(((value, key) for (key, value) in dict_to_convert.items()), reverse=True)
    for value, key in sorted_lst:
        sorted_dict[key] = value

    tuple_pair = []
    for key, value in sorted_dict.items():
        tuple_pair.append((key,value))
    return tuple_pair

def return_amount_of_wrong_chars(chars_to_check):
    """
    Takes in a dictionary and sums
    all the values, and returns the sum.
    """
    amount_of_wrong_chars = 0
    for value in chars_to_check.values():
        amount_of_wrong_chars += value
    return amount_of_wrong_chars

def get_amount_of_letters(sentences):
    """
    Counts all characters in the
    given argument.
    """
    letters = 0
    for sentence in sentences:
        letters += len(sentence)
    return letters

def words_per_minut(start, stop, words):
    """
    Calculates the words per minut.
    """
    return len(words) / ((stop - start) / 60)

def save_score(user, score, difficulty):
    """
    Writes the user, score and difficulty
    to the score.txt file.
    """
    with open("score.txt", "a") as f:
        f.write(f"{user} {score} {difficulty}\n")

def train(name_of_file, difficulty):
    """
    Takes in the name of the file,
    and what difficulty the file is.
    Lastly it prints the result from the
    training done.
    """
    i = 0
    inputs_lst = []

    content = get_content(name_of_file)
    file_sentences = remove_new_lines(content)
    file_len = len(content)

    start = time.time()
    while i < file_len:
        clear_terminal()
        typed = input(f"{file_sentences[i]}\n")
        inputs_lst.append(typed)
        i += 1
    stop = time.time()

    all_words = get_words(inputs_lst)
    total_time_seconds = round(stop - start, 1)
    wps = words_per_minut(start, stop, all_words)
    
    wrong_chars = compare_strings(file_sentences, inputs_lst)
    wrong_char_lst = dict_to_list_tuple_pair(wrong_chars)

    amount_of_wrong_chars = return_amount_of_wrong_chars(wrong_chars)
    chars_in_org_file = get_amount_of_letters(file_sentences)

    percent_wrong = round((amount_of_wrong_chars / chars_in_org_file) * 100, 2)
    score = (chars_in_org_file * (100 - percent_wrong)) / total_time_seconds

    clear_terminal()
    input("Congrats! You finished the training.\nPress enter to see statistics...")
    print("Feltecken:")
    print(wrong_char_lst)
    print(f"procentuellt fel {percent_wrong}%")
    print(f"total tid: {total_time_seconds}s")
    print(f"poäng: {score} ")
    print(f"WPM: {wps}")
    user = input("Enter username to add to highscore: ")

    save_score(user, score, difficulty)

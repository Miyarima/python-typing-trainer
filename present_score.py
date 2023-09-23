#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a module which will present
the score saved by the type_tester module
in descending order by score and difficulty.
"""

def get_user_score_diff(score_lst):
    """
    Takes in the rows from the file
    and returns the players and scores.
    """
    players_and_scores = []
    all_players_and_scores = []
    word = ""
    for playerscore in score_lst:
        for char in playerscore:
            if char in ["\n", " "]:
                players_and_scores.append(word)
                word = ""
            else:
                word += char
        if len(players_and_scores) > 2:
            all_players_and_scores.append(players_and_scores)
            players_and_scores = []
    return all_players_and_scores

def longest_element(lst, position):
    """
    Saves the longest string av 
    characters on the given position
    in a list and returns it plus 2.
    """
    longest = 0
    # for i in range(len(lst)):
    for i, _ in enumerate(lst):
        lenght = len(lst[i][position])
        if lenght > longest:
            longest = lenght
    return longest + 2

def create_print(elements, longest):
    """
    This functions takes in the finished
    list and makes it prettier by making
    every column even.
    """
    str_to_print = "\n"
    for lst in elements:
        for i in range(2):
            str_to_print += lst[i]
            for _ in range(longest[i] - len(lst[i])):
                str_to_print += " "
        str_to_print += lst[2] + "\n"
    return str_to_print

def merge_lst(lst1, lst2):
    """
    This function takes in the lists
    and merges them.
    """
    for diff in lst2:
        lst1.append(diff)
    return lst1

def sort_score(score_to_sort):
    """
    This function sorets list by
    the second element in every
    nestled list.
    """
    tmp_lst = []
    sorted_score = []
    for score in score_to_sort:
        tmp_lst.append([score[1], score[0], score[2]])
    tmp_lst = sorted(tmp_lst, reverse=True)
    for score in tmp_lst:
        sorted_score.append([score[1], score[0], score[2]])
    return sorted_score


def sort_difficulty(diff_to_sort):
    """
    This function takes in a list
    and distributes them into three
    different once depending on the
    difficulty.
    """
    easy_lst = []
    medium_lst = []
    hard_lst = []
    diff_sorted = []
    for diffifulty in diff_to_sort:
        if diffifulty[2] == "easy":
            easy_lst.append(diffifulty)
        elif diffifulty[2] == "medium":
            medium_lst.append(diffifulty)
        else:
            hard_lst.append(diffifulty)
    diff_sorted = merge_lst(diff_sorted, sort_score(hard_lst))
    diff_sorted = merge_lst(diff_sorted, sort_score(medium_lst))
    diff_sorted = merge_lst(diff_sorted, sort_score(easy_lst))
    return diff_sorted
    
    
def print_scores():
    """
    This function opens the score
    file and prints the return from
    the last function.
    """
    with open("score.txt") as f:
        all_scores = f.readlines()
    
    all_scores_words = get_user_score_diff(all_scores)

    longest_name = longest_element(all_scores_words, 0)
    longest_score = longest_element(all_scores_words, 1)
    diff_sorted = sort_difficulty(all_scores_words)
    print(create_print(diff_sorted, [longest_name, longest_score]))

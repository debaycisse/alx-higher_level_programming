#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    h_k = ""
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > score:
                score = v
                h_k = k
    if score == 0:
        return None
    return h_k

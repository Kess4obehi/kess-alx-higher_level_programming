#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best_scores = 0
    for key, scores in a_dictionary.items():
        if scores > best_scores:
            best_scores = scores
            best_key = key
    return best_key

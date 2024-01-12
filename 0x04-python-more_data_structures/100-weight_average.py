#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_scores = []
    weighted_sums = 0
    scored_sum = 0
    if my_list[:]:
        for i in range(len(my_list)):
            weighted_scores.append(my_list[i][0] * my_list[i][1])
            weighted_sums += my_list[i][1]

        for x in weighted_scores:
            scored_sum += x
        return (scored_sum / weighted_sums)
    return (0)

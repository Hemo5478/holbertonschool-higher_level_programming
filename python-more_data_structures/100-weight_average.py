#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (0)
    tot_type_1 = 0
    tot_type_2 = 0
    for score, weight in my_list:
        tot_type_1 += score * weight
        tot_type_2 += weight
    avg = tot_type_1 / tot_type_2
    return (avg)

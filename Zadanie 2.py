from main import *
import numpy as np
import math as mth
import random as rand
import csv

three_states = ['r', 'z', 'n']
character_array = np.random.choice(three_states, [20, 20])
another_character_array = np.random.choice(three_states, [20, 20])

s = [i/400 for i in range(0, 400)]
rand.shuffle(s)
p = [(1 - i/400) for i in range(0, 400)]
rand.shuffle(p)

s_sum = []
p_sum = []
p_sum_another = []


sum_index_czerwone = []
distance_czerwone = []
d_czerwone_indexes = []

sum_index_niebieskie = []
distance_niebieskie = []
d_niebieskie_indexes = []

sum_index_zielone = []
distance_zielone = []
d_zielone_indexes = []

t = 0
alpha = 2


def for_same_opinion(distance, some_index):
    l = 0
    while l < len(some_index):
        s_obj = (s[some_index[l]]/(1+(distance[l]**alpha)))
        s_sum.append(s_obj)
        l = l+1
    return s_sum


def for_different_opinion(distance, some_index, some_sum):
    l = 0
    while l < len(some_index):
        p_obj = (p[some_index[l]]/(1+(distance[l]**alpha)))
        some_sum.append(p_obj)
        l = l+1
    return some_sum


def sum_of_index(array_index, some_array, sum_index):
    for i in range(0, len(array_index)):
        sum_index.append(((len(some_array) * array_index[i][0]) + array_index[i][1]))
    return sum_index


def distances_in_array(c, d, some_array):
    for x in range(len(some_array)):
        for y in range(len(some_array)):
            if some_array[x][y] == "r":
                distance_czerwone.append(mth.sqrt((c - x) ** 2 + (d - y) ** 2))
                to_add = [x, y]
                d_czerwone_indexes.append(to_add)
            elif some_array[x][y] == "z":
                distance_zielone.append(mth.sqrt((c - x) ** 2 + (d - y) ** 2))
                to_add = [x, y]
                d_zielone_indexes.append(to_add)
            else:
                distance_niebieskie.append(mth.sqrt((c - x) ** 2 + (d - y) ** 2))
                to_add = [x, y]
                d_niebieskie_indexes.append(to_add)

    return distance_czerwone, distance_zielone, distance_niebieskie


with open("Zadanie 2 wyniki.txt", "w") as f:
    f.write("\nStarting array for t = {0} ".format(t))
    csv.writer(f).writerows(character_array)
    for t in range(10):
        f.write("\n")
        for i in range(0, len(character_array)):
            for j in range(0, len(character_array)):

                sum_index_czerwone = []
                distance_czerwone = []
                d_czerwone_indexes = []

                sum_index_niebieskie = []
                distance_niebieskie = []
                d_niebieskie_indexes = []

                sum_index_zielone = []
                distance_zielone = []
                d_zielone_indexes = []

                distances_in_array(i, j, character_array)

                if character_array[i][j] == "n":

                    # print("\nThe chosen element was blue")
                    sum_of_index(d_czerwone_indexes, character_array, sum_index_czerwone)
                    sum_of_index(d_zielone_indexes, character_array, sum_index_zielone)
                    sum_of_index(d_niebieskie_indexes, character_array, sum_index_niebieskie)

                    for_same_opinion(distance_niebieskie, sum_index_niebieskie)
                    result_same = 4 * sum(s_sum)

                    for_different_opinion(distance_zielone, sum_index_zielone, p_sum)
                    result_different_one = 4 * sum(p_sum)

                    for_different_opinion(distance_czerwone, sum_index_czerwone, p_sum_another)
                    result_different_two = 4 * sum(p_sum_another)

                    # print(
                    #    "The result for blue was: {0}, the result for green was: {1} and the result for red was: {2}".format(
                    #        result_same, result_different_one, result_different_two))
                    #print("The max result was :", max(result_same, result_different_one, result_different_two))
                    max_resuls = max(result_same, result_different_one, result_different_two)
                    if max_resuls == result_same:
                        another_character_array[i][j] = "n"
                    elif max_resuls == result_different_one:
                        another_character_array[i][j] = "z"
                    else:
                        another_character_array[i][j] = "r"

                    s_sum.clear()
                    p_sum.clear()
                    p_sum_another.clear()
                    max_resuls = 0

                elif character_array[i][j] == "z":
                    #print("\nThe chosen element was green")
                    sum_of_index(d_czerwone_indexes, character_array, sum_index_czerwone)
                    sum_of_index(d_zielone_indexes, character_array, sum_index_zielone)
                    sum_of_index(d_niebieskie_indexes, character_array, sum_index_niebieskie)

                    for_same_opinion(distance_zielone, sum_index_zielone)
                    result_same = 4 * sum(s_sum)

                    for_different_opinion(distance_niebieskie, sum_index_niebieskie, p_sum)
                    result_different_one = 4 * sum(p_sum)

                    for_different_opinion(distance_czerwone, sum_index_czerwone, p_sum_another)
                    result_different_two = 4 * sum(p_sum_another)

                    #print(
                    #    "The result for green was: {0}, the result for blue was: {1} and the result for red was: {2}".format(
                    #        result_same, result_different_one, result_different_two))
                    #print("The max result was :", max(result_same, result_different_one, result_different_two))
                    max_resuls = max(result_same, result_different_one, result_different_two)

                    if max_resuls == result_same:
                        another_character_array[i][j] = "z"
                    elif max_resuls == result_different_one:
                        another_character_array[i][j] = "n"
                    else:
                        another_character_array[i][j] = "r"

                    s_sum.clear()
                    p_sum.clear()
                    p_sum_another.clear()
                    max_resuls = 0

                elif character_array[i][j] == "r":

                    #print("\nThe chosen element was red")
                    sum_of_index(d_czerwone_indexes, character_array, sum_index_czerwone)
                    sum_of_index(d_zielone_indexes, character_array, sum_index_zielone)
                    sum_of_index(d_niebieskie_indexes, character_array, sum_index_niebieskie)

                    for_same_opinion(distance_czerwone, sum_index_czerwone)
                    result_same = 4 * sum(s_sum)

                    for_different_opinion(distance_niebieskie, sum_index_niebieskie, p_sum)
                    result_different_one = 4 * sum(p_sum)

                    for_different_opinion(distance_zielone, sum_index_zielone, p_sum_another)
                    result_different_two = 4 * sum(p_sum_another)

                    #print(
                    #    "The result for red was: {0}, the result for blue was: {1} and the result for green was: {2}".format(
                    #        result_same, result_different_one, result_different_two))
                    #print("The max result was :", max(result_same, result_different_one, result_different_two))
                    max_resuls = max(result_same, result_different_one, result_different_two)

                    if max_resuls == result_same:
                        another_character_array[i][j] = "r"
                    elif max_resuls == result_different_one:
                        another_character_array[i][j] = "n"
                    else:
                        another_character_array[i][j] = "z"

                    s_sum.clear()
                    p_sum.clear()
                    p_sum_another.clear()
                    max_resuls = 0

        f.write("\nArray in next time t = {0}".format(t + 1))
        f.write("\n")
        csv.writer(f).writerows(another_character_array)
        for i in range(len(character_array)):
            for j in range(len(character_array)):
                character_array[i][j] = another_character_array[i][j]


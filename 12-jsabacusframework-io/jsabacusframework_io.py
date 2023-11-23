"""
Advent of Code - Day 12: JSAbacusFramework.io
"""
import json
import pprint

# load text file
with open('input.txt', 'r') as input:
    json_document = input.read()

json_data = json.loads(json_document)
#pprint.pprint(json_data)

###########
# Part One
###########
def integer_sum(input):
    sum = 0
    if type(input) is dict:
        for value in input.values():
            if type(value) is int:
                sum += value
            elif type(value) is dict or type(value) is list:
                sum += integer_sum(value)

    elif type(input) is list:
        for element in input:
            if type(element) is int:
                sum += element
            elif type(element) is dict or type(element) is list:
                sum += integer_sum(element)

    elif type(input) is int:
        sum += input

    return sum

print(integer_sum(json_data))


###########
# Part Two
###########
def integer_sum_excluding_red(input):
    sum = 0
    if type(input) is dict:
        if 'red' in input.values():
            pass
        else:
            for value in input.values():
                if type(value) is int:
                    sum += value
                elif type(value) is dict:
                    if 'red' in value.values():
                        pass
                    else:
                        sum += integer_sum_excluding_red(value)
                elif type(value) is list:
                    sum += integer_sum_excluding_red(value)

    elif type(input) is list:
        for element in input:
            if type(element) is int:
                sum += element
            elif type(element) is dict:
                if 'red' in element.values():
                    pass
                else:
                    sum += integer_sum_excluding_red(element)

            elif type(element) is list:
                sum += integer_sum_excluding_red(element)

    elif type(input) is int:
        sum += input

    return sum

print(integer_sum_excluding_red(json_data))

import ipdb

numbers_list = []

numbers_tuple = ()

# if only one value in a tuple it must be followed by a comma

# spread_operator = [* seq1, seq2] uses asterisk instead of ...

# {*foods[0]} returns a 'set' class

# single asterisk can also be used for a tuple

# { **foods[0]} returns a dictionary

#{**foods[0], 'age' : 1} returns a new dictionary with the updated data, either added or mutated

# [4,5,4].index(5) searches for 5, returns index of 1

# [4,5,4].count(4) counts 4's, returns 2


# a set that removes duplicates from apple string, unordered

# set_of_chars = set("apple")

#taking characters from a set, and creating a new string, no duplicates

# new_string = ""

# for char in set_of_chars:
#     new_string += char

#food['name'] = "hot Dog" w/ new variable of food being the first set in the dictionary

# key_value_pairs = {'name': "onion rings", 'age': 5}
# foods.update(key_value_pairs) adds key value pairs, or update existing key with new value. is destructive.

# a set that removes duplicate items from a list
#numbers_set = set([2,2,3,3,4,4]) returns {2,3,4}
#numbers_list_without_duplicates = list(numbers_set) returns [2,3,4]


def combine_sequences(seq1, seq2):
    new_sequence = seq1 + seq2
    return new_sequence

def sequence_n_times(seq, n):
    new_sequence = seq * n
    return new_sequence

def average(seq):
    new_sequence = sum(seq)/len(seq)
    return new_sequence

def append_n_times(input_list, element, n):
    return [*input_list] + [element] * n
    

foods = [
    {
        "name": "Flatburger",
        "price": 9.50
    },
    {
        "name": "French Fries",
        "price": 1.25
    },
    {
        "name": "Burrito",
        "price": 7.25
    }
]

animals = [
    {
        "name": "Fido",
        "animal_type": "Dog"
    },
    {
        "name": "Kitty",
        "animal_type": "Cat"
    },
    {
        "name": "Fluffy",
        "animal_type": "Guinea Pig"
    }
]

food_names = [food['name'] for food in foods]

food_price = [food['price'] for food in foods]
average_price = sum(food_price)/len(food_price)

animal_descriptions = [f"{animal['name']} is a {animal['animal_type']}" for animal in animals]
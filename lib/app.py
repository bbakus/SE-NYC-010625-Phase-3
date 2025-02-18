import ipdb

# # write your code here


# # def whatever_name_we_want(param1, param2):
# #     # new_var = f'Hello {param1} {param2}'
# #     new_var = "hello" + " " + param1 + " " + param2
# #     return new_var


# # result = whatever_name_we_want("John", "Krazinski")

# # print(result)

# def is_it_true(item):
#     if item:
#         return "yes"
#     else:
#         return "no"
    
# solve = is_it_true(None)

# print(solve)

# my_list = [1,2,3,4,5]

# my_tuple = (1,2,3,4,5)

# # tuple is immutable, unlike lists. it also takes up less memory

# greetings = ["hello", "howdy", "buttstuff"]
# result = [ item.title() for item in greetings]
# print(result)

# result = "pizza"
# result = "not pizza"
# RESULT = "I am a constant"
# # RESULT is still changeable, it's just more of a signal to devs to avoid changing it


# # DICTIONARIES (kind of like a JS object)

# my_dictionary = {
#     "key" : "value",
#     "key_two": "value_two"
# }

# #dictionary keys have to be strings, like json, unless you're using numbers

# my_dictionary["key"]

# my_dictionary['new_thing'] = 'hello' #new key, and new value

# my_dictionary['new_thing'] = 'goodbye' # reassigns the value


# def make_error():
#     try:
#         return 100/0
#         # raise Exception("I AM AN ERROR")
#     except:
#         print("You shall not pass!!")

# make_error()


#Deliverable 1

print("Hello Flatiron! Class is in session!")

#Deliverable 2

def add(num1, num2):
    if type(num1) != int and type(num1) != float:
        raise TypeError
    if type(num2) != int and type(num2) != float:
        raise TypeError
    return num1 + num2
    
        

#Deliverable 3

def subtract(num1,num2):
    try:
        result = num1 - num2
        return result
    except TypeError:
        print("Error: num1 and num2 must both be integers or floats!")


#Deliverable 4

def multiply(num1,num2):
    if type(num1) != int and type(num1) != float:
        raise TypeError
    if type(num2) != int and type(num2) != float:
        raise TypeError
    return num1 * num2

#Deliverable 5

def divide(num1, num2):
    try:
        result = num1/num2
        return result
    except TypeError:
        print("Error: num1 and num2 must both be integers or floats!")
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0!")
              

#Deliverable 6

def calculator(operator, num1, num2):
    
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        if operator == "+":
            return num1 + num2
        if operator == "-":
            return num1 - num2
        if operator == "*":
            return num1 * num2
        if operator == "/":
            return num1 / num2
    else:
        raise Exception
    

#Deliverable 7

def create_user(username):
    if type(username) != str:
        raise TypeError
    elif len(username) < 2:
        raise ValueError
    else:
        print(f"User successfully created! Welcome {username}!")
    

#Deliverable 8

def print_greeting_loop(greeting):
    if type(greeting) == str:
        for letter in greeting:
            print(letter)
    
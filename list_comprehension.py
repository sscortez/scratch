
"""
Examples of list comprehensions:

1. Definitions
2. For loop, syntax
3. List comprehension examples:
    a. List comprehension. Ex. 1
    b. Dictionary comprehension. Ex. 7
    c. Combination of both. Ex. 6
4. Q&A
"""

"""
* Iteration: Executing the same block of code over and over
* Loop:      A programming structure that implements iteration; collection-based iteration
* For loop:  A programming structure that loops over a collection of objects (eg. list, tuple, dict)
* Iterable:  Collection of objects
* List:      An object that stores a collection of objects; bookended by square brackets (eg. [1]); objects are
             separated by commas
"""

# For loop syntax:
#
# for <variable> in <collection>:
#    <statement>



# For loop syntax:
#
# for <variable: placeholder for/representative of each object in a collection> in <collection: collection of objects>:
#    <statement: block of code to be repeated over and over for each object in a collection>



# For loop syntax
for i in [1, 2, 3, 4, 5]:
    print(i)



# ~~~~~~~~~~~~~~~~ EXAMPLE 1: Compute each object in a list ~~~~~~~~~~~~~~~~ #
items = [1, 2, 3, 4, 5]
empty_lista = []
for x in items:
    new_val = x * 2
    empty_lista.append(new_val)
print(empty_lista)



# List comprehension syntax
#
# [<statement> for <variable> in <collection>]



# List comprehension syntax
#
# [<statement: block of code to be repeated over and over for each object in a collection>
#  for <variable: placeholder for/representative of each object in a collection>
#  in <collection: collection of objects>]



list_compa = [x * 2 for x in items]
print(list_compa)


# ~~~~~~~~~~~~~~~~ EXAMPLE 2: Flatten a nested list inside a list ~~~~~~~~~~~~~~~~ #
items = [['seat1', 'seat2'],
         ['seat3', 'seat4'],
         ['seat5', 'seat6'],
         ['seat7', 'seat8'],
         ['seat9', 'seat10']]
empty_listb = []
for x in items:
    for y in x:
        empty_listb.append(y)
print(empty_listb)

list_compb = [y for x in items for y in x]
print(list_compb)

# new_list = [<variable2>                             Get the selected item and add it to the list
#             for <variable1> in <iterable object>    Get each item in the iterable object
#             for <variable2> in <variable1>]         Get each item in the nested object





# ~~~~~~~~~~~~~~~~ EXAMPLE 3: Check if a string pattern exists in each string in a list ~~~~~~~~~~~~~~~~ #
items = ['Alds', 'Abii', 'A-Jay', 'Joyce', '__Dunderrrr__', '__Agentx']
empty_listc = []
for x in items:
    if '__' not in x:
        empty_listc.append(x)
print(empty_listc)

list_compc = [x for x in items if '__' not in x]
print(list_compc)

# new_list = [<variable>                       Get the selected item and add it to the list
#              for <variable> in <iterable>    Get each item in the iterable object
#              if <object> in <variable>]      Check if a string pattern is in the selected item





# ~~~~~~~~~~~~~~~~ EXAMPLE 4: Check if each item in a list is in another list ~~~~~~~~~~~~~~~~ #
their_states = ['Alaska', 'Hawaii', 'Georgia', 'Montana', 'New York',
                'California', 'Indiana', 'Oregon', 'Florida', 'Iowa']
my_states = ['Montana', 'California', 'Florida', 'Missouri', 'New York', 'New Jersey']
empty_listd = []
for x in their_states:
    if x in my_states:
        empty_listd.append(x)
print(empty_listd)

list_compd = [x for x in their_states if x in my_states]
print(list_compd)

# new_list = [<variable>                      Get the selected item and add it to the list
#             for <variable> in <iterable>    Get each item in the iterable object
#             if <variable> in <object>]      Check if the selected item is inside an iterable object





# ~~~~~~~~~~~~~~~~ EXAMPLE 5: Using Enumerator() in a list comprehension ~~~~~~~~~~~~~~~~ #
item = range(1, 11)
empty_liste = []
for ind, x in enumerate(item):
    if ind % 2 == 0:
        empty_liste.append(x)
print(empty_liste)

list_compe = [x for ind, x in enumerate(range(1, 11)) if ind % 2 == 0]
print(list_compe)

# new_list = [<variable2>                                              Get item 2 and add it to the list
#             for <variable1>, <variable2> in enumerate(<iterable>)    Get each items in the enumerate operator
#             (if condition: <variable1> is even)]                     Check if item 1 is even





# ~~~~~~~~~~~~~~~~ EXAMPLE 6: Greetings ~~~~~~~~~~~~~~~~ #
string_object = "Hi there {name}. How are you doing today? Your nickname is {nickname} correct? " \
                "Your pronouns are {pronouns} correct? Thanks for confirming!"

place_holders = ['name', 'nickname', 'pronouns']
print(place_holders)

alds = {
    'name': 'Aldrin',
    'competiton': 'badminton',
    'nickname': 'Alds',
    'pronouns': 'he/him'}
benjie = {
    'name': 'Benjamin',
    'competition': 'RPG video games',
    'nickname': 'Benjie',
    'pronouns': 'they/them'}
abii = {
    'name': 'Abigail',
    'competition': 'singing',
    'nickname': 'Abii',
    'pronouns': 'she/her'}
ate_lea = {
    'name': 'Leafar',
    'competition':'pageantry',
    'nickname': 'Ate Lea',
    'pronouns': 'she/her'}

mi_gente = [alds, benjie, abii, ate_lea]

for person in mi_gente:
    pertinent_info = {key: value for key, value in person.items() if key in place_holders}
    print(f'{string_object.format(**pertinent_info)}')





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Dictionary Comprehension ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

"""
* dictionary: object that stores a collection of objects in key-value pairs; bookended by curly brackets (eg. {'a': 1})
"""

# ~~~~~~~~~~~~~~~~ EXAMPLE 7: Multiply each value value by 2 ~~~~~~~~~~~~~~~~ #
dict_item = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
empty_dicta = {}
for key, val in dict_item.items():
    empty_dicta[key] = val * 2
print(empty_dicta)

dict_compa = {k: v * 2 for k, v in dict_item.items()}
print(dict_compa)

# empty_dict = [<variable1>: <variable2> * 2                        Get the key and multiply the value of that key by 2
#               for <variable1>, <variable2> in <iterable>.items()  Get key-value pair in dictionary using items()





# ~~~~~~~~~~~~~~~~ EXAMPLE 8: Add functions into a dictionary. key: name of function, value: function ~~~~~~~~~~~~~~~~ #

def func1():
    return 1


def func2():
    return 2


def func3():
    return 3

func_list = [func1, func2, func3]
empty_dictb = {}
for func in func_list:
    empty_dictb[func.__name__] = func
print(empty_dictb)

dict_compb = {func.__name__: func for func in func_list}
print(dict_compb)

# empty_dictb = {<variable>.__name__: <variable>          Get the name and the item and add them as pairs to dict
#                for <variable> in <iterator>}             Get each item in the dictionary





# ~~~~~~~~~~~~~~~~ EXAMPLE 9: Get instance variables in a class and loop into a dict comprehension ~~~~~~~~~~~~~~~~ #
class MyMilkTeas:
    def __init__(self):
        self.item1 = 'oolong milk tea'
        self.item2 = 'regular kung fu milk tea'
        self.item3 = 'brown sugar milk tea'
        self.item4 = 'taro milk tea - no boba'
        self.item5 = 'winter melon milk tea'

my_milk_teas = MyMilkTeas()
my_bobas = {key: value for key, value in my_milk_teas.__dict__.items() if 'no boba' not in value}
print(my_bobas)

# my_bobas = {<variable1>: <variable2>                                     Get key and value pair and add to dictionary
#             for <variable1>: <variable2> in <class_obj.__dict__>.items() Get instance variables of a class via items()
#             (if condition)                                               Get key-val pair only if they meet condition




# ~~~~~~~~~~~~~~~~ EXAMPLE 10: Putting it together; Implemented in RPC reporting ~~~~~~~~~~~~~~~~ #
# * For documentation on Format().parse():
#       https://docs.python.org/3.7/library/string.html#string.Formatter.parse
# * Format().parse() is a lazy operator
# * Returns an iterable of tuples (literal_text, field_name, format_spec, conversion)
from string import Formatter

query1 = "SELECT id, customer_id" \
         "FROM avant.{dw_table}.loans" \
         "WHERE origination_date > DATE('{trgt_date1}')"

query2 = "SELECT email, person_id " \
         "FROM avant.{dw_table}.customers " \
         "WHERE email_domain in ({email_domains}) " \
         "AND bad_email is False"

query3 = "SELECT first_name, last_name " \
         "FROM avant.{basic_table}.people " \
         "WHERE date_of_birth > DATE('{trgt_date2}')"

queries = {'query1': query1, 'query2': query2, 'query3': query3}


class MyClass1:
    def __init__(self):
        self.dw_table = 'dw'
        self.trgt_date1 = '2019-01-01'
        self.email_domains = "'gmail', 'aol', 'outlook'"
        self.basic_table = 'avant_basic'
        self.trgt_date2 = '1960-03-05'

class MyClass2:
    def __init__(self):
        self.dw_table = 'dw_eloan'
        self.trgt_date1 = '2019-03-01'
        self.email_domains = "'gmail', 'outlook'"
        self.basic_table = 'avant_basic_eloan'
        self.trgt_date2 = '1965-01-05'

my_classes = [MyClass1(), MyClass2()]

for name, query in queries.items():
    place_holders = [fname for _, fname, _, _ in Formatter().parse(query) if fname]
    for cls in my_classes:
        pairing = {i: cls.__dict__.get(i) for i in place_holders}
        print(f'For class {cls.__class__.__name__}, query {name} says:'
               f'       {query.format(**pairing)}')

"""
Cons:
    1. Cannot handle exceptions
    2. Becomes difficult to read for more complex expressions
    3.
"""

"""
For loops = definite iteration
Python for loop:
    Collection-Based or Iterator-Based Loop
List comprehension is a great tool to use because it allows you to condense multiple lines of code into one line
while still maintaining clarity of execution
"""

"""
Sources:
1. For loop: https://realpython.com/python-for-loop/
2. List comprehension: https://realpython.com/list-comprehension-python/
"""

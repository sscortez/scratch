import time

# A decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f'Finished in {end:0.2f} seconds')
        return result
    return wrapper

# For loop syntax
# for <item> in <iterable>:
#     <statement>

# Simple for loop
for i in [1, 2, 3, 4, 5]:
    print(i)

# __iter__() and __next__()
items = [1, 2, 3, 4, 5]
iter_obj = iter(items)
next(iter_obj)

# Simple generator function
def generator_func():
    for x in range(0, 10):
        yield x

# Simple generator expression
gen_obj = (x for x in range(0, 10))


############################### Example 1 ###############################

# Function with for loop
@timer
def large_calculation(max=10000):
    lst = []
    for x in range(0, max):
        result = x ** 15
        lst.append(result)
    return lst

# Generator function
@timer
def large_calculation_gen(max=10000):
    for x in range(0, max):
        result = x ** 15
        yield result


############################### Example 2 ###############################

import os

import pandas as pd


file_name = 'icd10cm_codes_2019.txt'
file_path = os.path.expanduser(os.path.join('~/Downloads', file_name))
df_columns = ['code', 'definition']

@timer
def to_dataframe(file_path):
    df = pd.read_csv(file_path, header=None, sep='|')
    df = df[0].str.split(' ', 1, expand=True)
    df.columns = ['code', 'definition']
    return df

@timer
def to_df_with_gen(file_path):
    with open(file_path) as data:
        line = (lines.replace('\n', '').split(' ', 1) for lines in data)
        formatted = ([l[0], l[1].lower()] for l in line)
        df = pd.DataFrame(formatted)
        df.columns = ['code', 'definition']
        return df


############################### Example 3 ###############################
# File can be found at https://realpython.com/introduction-to-python-generators/
import os
from guppy import hpy; h = hpy()  # installed guppy3 for Python3

file_path = os.path.expanduser('~/Downloads/techcrunch.csv')


@timer
def compute_with_df(file_path):
    df = pd.read_csv(file_path)
    print(f'Size of df: {h.iso(df)}')
    total_series_a = df.loc[df['round'] == 'a', 'raisedAmt'].sum()
    print(f'Total funding for round A is ${total_series_a}')


@timer
def compute_with_gen1(file_path):
    with open(file_path) as f:
        # Get lines; result: generator > str
        lines = (line for line in f)
        print(f'Size of lines: {h.iso(lines)}')
        # Split each line to a list; result: generator > list
        list_lines = (s.strip().split(',') for s in lines)
        print(f'Size of list_lines: {h.iso(list_lines)}')
        # Get columns; result: list
        cols = next(list_lines)
        # Zip column with every line; result: generator > dict
        company_dicts = (dict(zip(cols, data)) for data in list_lines)
        # Get collection of raised amount
        funding = (int(company_dict['raisedAmt'])
                   for company_dict in company_dicts
                   if company_dict['round'] == 'a')
        print(f'Size of funding: {h.iso(funding)}')
        # Consume by adding using `sum()`
        total_series_a = sum(funding)

        print(f'Total funding for round A is ${total_series_a}')

 
############################### Example 3 ###############################
# This is an actual use case in our team's repo. We ingest an API output
# that is one large bytes object and convert it into a pd.DataFrame object
def output_to_df(output):
    # Converts bytes object to string
    if isinstance(output, bytes):
        output = output.decode('utf-8')

    # Split string on "\n"; split() returns a list of strings
    lines = (output.split('\n'))

    # Removes last item in the list that contains an empty string
    data_lines = (line for line in lines if line != '')

    # Split string on ","; returns a list of strings
    items = (dl.split(',') for dl in data_lines)

    # Get first item in generator object (it is a list of string objects)
    headers = next(items)

    # Format each string as lower case in the list object `headers`
    headers = [h.lower() for h in headers]

    # Create a pd.DataFrame object out of object items
    df = pd.DataFrame(items, columns=headers)

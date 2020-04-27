# Convert Number into tuple of words using list comprehension
"""
input- Numbers (int)
Output- integer with corresponding word as string

"""

NUM = int(input('Enter number'))
STR_NUM = str(NUM)

TUP_VALUE = {'1':(1, 'One'), '2':(2, 'Two'), '3':(3, 'Three'), '4':(4, 'Four'), '5':(5, 'Five'),
             '6':(6, 'Six'), '7':(7, 'Seven'), '8':(8, 'Eight'), '9':(9, 'Nine'), '0':(0, 'Zero')}


TUPLE_OUTPUT = [TUP_VALUE[i] for i in STR_NUM if i in TUP_VALUE]


print(TUPLE_OUTPUT)

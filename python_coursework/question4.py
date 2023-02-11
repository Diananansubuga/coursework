#With illustrations, give the difference between lists and tuples

"""lists: a list stores dynamic characters therefore they can be modified.
lists are denoted with square brackets and the implications of iterations are time consuming. they take up alot of memory and 
its easy for errors to occur.

#illustration of  lists:"""
num_list=[1,2,3,5,6]#a list of integers
print(num_list)

letter_list['a','b','c','d']# a list with letters
print(letter_list)

mixed_list['a',1,'c','d',4]# a list wit mixed data types
print(mixed_list)

nested_lists[1,2,3['a','b','c']4,5,6]#nested lists
print(nested_loops)



"""#tuples: tuples store static characters therefore they cannot be modified.
tuples are denoted with parenthesis and they are faster than lists. they take up less memory and its hard for errors to occur."""
num_tuple=(1,2,3,5,6)#a tuple of integers
print(num_tuple)

letter_tuple('a','b','c','d')# a tuple with letters
print(letter_tuple)

mixed_tuple('a',1,'c','d',4)# a tuple wit mixed data types
print(mixed_tuple)

nested_tuple(1,2,3('a','b','c')4,5,6)#nested tuples
print(nested_tuple)

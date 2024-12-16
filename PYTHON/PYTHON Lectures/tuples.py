# TUPLES


#Tuples are faster.
#Tuples cannot be modified.
#Tuples can be changed to tuples


products = ['pen', 'pencil', 'book']
colors = ('red', 'green', 'pink')

# Qn. Add rubber to the products list, ( Hint use append)

products.append('rubber') # This puts rubber in at the end.
print(products)

# Qn. Add ruler at the second position to the productis list. (Hint use insert)

products.insert(1,'ruler') # Here use, the order of the indexing and the rubber comes in the second position
print(products)

# Qn. Display the length of the list products.

length = len(products)
print(length)

# Qn. Add purple to the tuple color.
# This will give an error because you cannot modify a tuple.

 #  *********The tuple can only be modified after changing it to a alist like this'

new_colors =list(colors)
print(type(new_colors)) # This prints a list.


new_colors.append('purple')
print(new_colors)

# Then convert back that list to a tuple again.
colors = tuple(new_colors)
print(colors) # This will print back your tuple.



#Qn.  Print the tuple with one item

fruits = ('Apple',) # You add a comma whenever the tuple has only one item. Because if you dont add a comma, it prints out a list.
print(type(fruits))
print(fruits)

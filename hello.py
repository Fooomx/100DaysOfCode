print('Hello')
print('Hello World')
fruit = "orange"
print(fruit)
print("orange")
print(fruit[2])
print('{0:8} | {1:8}' .format('Fruit', 'Quantity'))
print('{1:8} | {0:8}' .format('Apple', 3))
print('{0:8} | {1:8}' .format('Orange',5))
print(len(fruit))
print('{0:8} | {1:<8}' .format('Fruit', 'Quantity'))
print('{1:8} | {0:^8}' .format('Apple', 3))
print('{0:8} | {1:>8}' .format('Orange',5))
print('{0:8} | {1:>8.2f}' .format('Orange',3.1416354))
# Example Exercise
#Get Input from the user
text = input('What would you like the cat to say?')

#Determine the length of the input
text_length = len (text)

#Make the border the same size as the input
print('          {}'.format('_' * text_length))
print('        < {} >'.format(text))
print('          {}'.format('-' * text_length))





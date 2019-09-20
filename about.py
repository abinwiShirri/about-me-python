#!/bin/python3


print('Hi, I can code in Python!')

live = input('Where do you live?')

fav_anim = input('What is your favourite animal?')

fav_color = input('what is your favourite colour?')

fav_quote = input('what is your favourite quote?')

dislike_nature = input('do you dislike nature?')

like_books = input('do you like books?')


print('''
My favourite animals are sheep

 o-###-
   | |   #

I live in Glasgow

   _|_
  |   |
  |#  |____
  |   |    |
  |  #|  # |
 _|___|_#__|_

''')

born = input('What year were you born?')
born = int(born)
age = 2025 - born
print('Your favourite animal is ', fav_anim )
print('You live in', live, ' And in the year 2025 you\'ll be', age, 'years old!')
print('your favourite animal is ', fav_color )
print('your favourite quote is ', fav_quote)
print('do you dislike nature', dislike_nature)
print('do you like books', like_books)
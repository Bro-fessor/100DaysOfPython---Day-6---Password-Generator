#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
basic_password=""
for number_of_letters in range(0,nr_letters):
  random_letter_index=random.randint(0,len(letters)-1)
  basic_password=basic_password+letters[random_letter_index]
for number_of_symbols in range(0,nr_symbols):
  random_symbol_index=random.randint(0,len(symbols)-1)
  basic_password=basic_password+symbols[random_symbol_index]
for number_of_numbers in range(0,nr_numbers):
  random_number_index=random.randint(0,len(numbers)-1)
  basic_password=basic_password+numbers[random_number_index]
scrambled_password=''.join(random.sample(basic_password,len(basic_password)))
print(f"Basic password is {basic_password}")
print(f"shuffled password is {scrambled_password}")
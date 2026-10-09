# numbers = []
# for i in range(0, 5):
#     numbers.append(int(input("Number: ")))
#
# first_number = numbers[0]
# last_number = numbers[-1]
# smallest_number = min(numbers)
# largest_number = max(numbers)
# average_of_numbers = sum(numbers)/len(numbers)
#
# print(f"The first number is {first_number}")
# print(f"The last number is {last_number}")
# print(f"The smallest number is {smallest_number}")
# print(f"The largest number is {largest_number}")
# print(f"The average number is {average_of_numbers}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

current_username = input('Please enter your username: ')
if current_username in usernames:
    print("Access granted.")
else:
    print("Access denied.")

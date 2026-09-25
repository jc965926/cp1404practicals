# GST_RATE = 0.1
#
# item_price = float(input("Item price: "))
# has_gst = input("Any GST? (y/n): ").lower()
# if has_gst == "y":
#     item_price *= (1 + GST_RATE)
# print(f"Final price: ${item_price:.2f}")

# user_number = int(input("Enter a number: "))
# for i in range(0, user_number):
#     print(i)

SECRET_NUMBER = 1

guess_number = int(input("Guess the number between 1 and 10: "))
while guess_number != SECRET_NUMBER:
    print("Wrong number! Please try again.")
    guess_number = int(input("Guess the number between 1 and 10: "))

print(f"You got it! The secret number is {SECRET_NUMBER}")
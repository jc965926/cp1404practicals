from prac_06.guitar import Guitar

# test get_age() function

test_guitar = Guitar("Telecaster", 1999, 799)
print(test_guitar)

age = test_guitar.get_age() # should be 27

print(f"{test_guitar.name} get age(): Expected 27. Got {age}")
# Gibson L-5 CES get_age() - Expected 100. Got 100
# Another Guitar get_age() - Expected 9. Got 9
# Gibson L-5 CES is_vintage() - Expected True. Got True
# Another Guitar is_vintage() - Expected False. Got False
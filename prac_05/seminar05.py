name_to_score = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}

name_width = max(len(name) for name in name_to_score)
number_width = max(len(name_to_score) for name in name_to_score)

print(name_width)
print(number_width)

for name, score in name_to_score.items():
    print(f"{name:<{name_width}} = {score:>{number_width}}")
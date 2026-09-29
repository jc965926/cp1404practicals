# filename = "text.txt"
filename = input("filename: ")
try:
    in_file = open(f"{filename}", "r")
    for line in in_file:
        line_stripped = line.strip()
        if line_stripped.startswith("#"):
            print(line_stripped)
    in_file.close()
except FileNotFoundError:
    print("File not found")


# guitars = open("guitars.txt", "r")
# for line in guitars:
#     parts = line.strip().split(",")
#     model = parts[0]
#     year = parts[1]
#     price = float(parts[2])
#     print(f"{model} ({year}): ${price}")
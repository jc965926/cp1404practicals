COLOUR_TO_HEX = {"amaranth": "#e52b50", "apricot": "#fbceb1",
                 "aquamarine2": "#76eec6", "baker-miller pink": "#ff91af",
                 "banana yellow": "#ffe135", "barn red": "#7c0a02",
                 "boysenberry": "#873260", "bright green": "#66ff00",
                 "byzantium": "#702963", "cadmium orange": "#ed872d"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
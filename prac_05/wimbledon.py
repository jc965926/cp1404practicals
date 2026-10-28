"""
Word Occurrences
Estimate: 60 minutes
Actual:   60 minutes
"""

FILENAME = "wimbledon.csv"

def main():
    """Display Wimbledon champions and their wins, along with winning countries"""
    wimbledon_data = read_file(FILENAME)
    champions_to_wins = get_champions(wimbledon_data)
    winning_countries = get_winning_countries(wimbledon_data)

    print("Wimbledon Champions:")
    for champion in champions_to_wins:
        print(f"{champion} {champions_to_wins[champion]}")

    print(f"\nThese {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(winning_countries))


def read_file(filename):
    """Read entire contents of file"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline() # skip header
        data = in_file.readlines()
        return data

def get_champions(data):
    """Add champions and their wins to a dictionary"""
    champion_to_wins = {}
    for line in data:
        if line.split(",")[2] not in champion_to_wins.keys():
            champion_to_wins[line.split(",")[2]] = 1
        else:
            champion_to_wins[line.split(",")[2]] += 1
    return champion_to_wins

def get_winning_countries(data):
    """Create a set containing winning countries"""
    winning_countries = []
    for line in data:
        winning_countries.append(line.split(",")[1])
    return sorted(set(winning_countries))

main()

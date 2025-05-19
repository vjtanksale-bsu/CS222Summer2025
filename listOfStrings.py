def main():
    students = ["Alice", "Bob", "Carol", "Dave", "Eve"]
    print(len(students))
    print(students[2])
    print(len(students[4]))
    for s in students:
        for c in s:
            print(c)
    afc = [["Colts", "Titans", "Jaguars", "Texans"],
           ["Patriots", "Jets", "Dolphins", "Bills"],
           ["Steelers", "Bengals", "Ravens", "Browns"],
           ["Broncos", "Chargers", "Chiefs", "Raiders"]]
    print(afc[0])
    print(afc[1][2])
    print(afc[2][1][3])
    print(len(afc[2]))
    print(len(afc[3][0]))
main()
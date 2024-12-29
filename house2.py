# Uses match with case

name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ronn":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")
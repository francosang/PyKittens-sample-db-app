def start():
    show_main_menu()

def show_main_menu():
    while True:
        print("+-------------------------------+")
        print("|           Main Menu           |")
        print("+-------------------------------+")
        print("Select an option\n")
        print("\t1) Manage Kittens")
        print("\t2) Manage Families")    
        print("\tQ) Exit")    
        print("\nType an option > ")

        option = input()
        match option:
            case "1":
                show_kittens_menu()
            case "2":
                ... 
            case "Q" | "q":
                exit(0)

def show_kittens_menu():
    while True:
        print("+----------------------------------+")
        print("|           Kittens Menu           |")
        print("+----------------------------------+")
        print("Select an option\n")
        print("\tF) Find kitten")    
        print("\tA) Add kitten")    
        print("\tE) Edit kitten")    
        print("\tD) Delete kitten") 
        print("\tL) List all kittens")
        print("\tB) Back")
        print("\nType an option > ")

        option = input()
        match option:
            case "F" | "f" | "1":
                show_find_kitten()
            case "A" | "a" | "2":
                show_add_kitten()
            case "B" | "b":
                break
            case "Q" | "q":
                exit(0)

def show_find_kitten():
    print("+---------------------------------+")
    print("|           Find Kitten           |")
    print("+---------------------------------+")
    print("\nType a kitten name > ")

def show_add_kitten():
    print("+--------------------------------+")
    print("|           Add Kitten           |")
    print("+--------------------------------+")
    print("\nIntroduce the kitten info\n")

    name = input("Name: ")
    race = input("Race: ")
    color = input("Color: ")
    family = request_family()

def request_family():
    return int(input("Family: "))

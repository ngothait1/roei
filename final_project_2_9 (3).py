database = []

def add_entry():
    id_num = input("Enter ID number: ")
    
    if id_num.isdigit() == False:
        print("Error: ID must be a number.")
        return
    
    for entry in database:
        if entry['ID'] == id_num:
            print("Error: ID already exists in the system.")
            return
    
    name = input("Enter name: ")
    age = input("Enter age: ")
    
    if age.isdigit() == False:
        print("Error: Age must be a number.")
        return
    
    database.append({'ID': id_num, 'Name': name, 'Age': int(age)})
    print("ID " + id_num + " saved successfully!")

def search_by_id():
    id_num = input("Enter ID number to search: ")
    
    if id_num.isdigit() == False:
        print("Error: ID must be a number.")
        return
    
    for index, entry in enumerate(database):
        if entry['ID'] == id_num:
            print("Index: " + str(index))
            print("ID: " + entry['ID'])
            print("Name: " + entry['Name'])
            print("Age: " + str(entry['Age']))
            return
    print("Error: No entry found with this ID.")

def print_average_age():
    if len(database) == 0:
        print("No entries in the database.")
        return
    
    total_age = sum(entry['Age'] for entry in database)
    average_age = total_age / len(database)
    print("Average age: " + str(round(average_age, 2)))

def print_all_names():
    if len(database) == 0:
        print("No entries in the database.")
        return
    
    print("All names:")
    for index, entry in enumerate(database):
        print("Index: " + str(index))
        print("Name: " + entry['Name'])
        print()

def print_all_ids():
    if len(database) == 0:
        print("No entries in the database.")
        return
    
    print("All IDs:")
    for index, entry in enumerate(database):
        print("Index: " + str(index))
        print("ID: " + entry['ID'])
        print()

def print_all_entries():
    if len(database) == 0:
        print("No entries in the database.")
        return
    
    print("All entries:")
    for index, entry in enumerate(database):
        print("Index: " + str(index))
        print("ID: " + entry['ID'])
        print("Name: " + entry['Name'])
        print("Age: " + str(entry['Age']))
        print()

def print_entry_by_index():
    index = input("Enter the index of the entry to print: ")
    
    if index.isdigit() == False:
        print("Error: You must choose a number. '" + index + "' is not a number.")
        return
    
    index = int(index)
    
    if index < 0 or index >= len(database):
        print("Error: Index out of range. There are only " + str(len(database)) + " entries in the database.")
        return
    
    entry = database[index]
    print("Index: " + str(index))
    print("ID: " + entry['ID'])
    print("Name: " + entry['Name'])
    print("Age: " + str(entry['Age']))

def display_menu():
    while True:
        print("\nChoose an action:")
        print("1. Add a new entry")
        print("2. Search by ID")
        print("3. Print the average age")
        print("4. Print all names")
        print("5. Print all IDs")
        print("6. Print all entries")
        print("7. Print entry by index")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            search_by_id()
        elif choice == '3':
            print_average_age()
        elif choice == '4':
            print_all_names()
        elif choice == '5':
            print_all_ids()
        elif choice == '6':
            print_all_entries()
        elif choice == '7':
            print_entry_by_index()
        elif choice == '8':
            while True:
                confirm_exit = input("Are you sure you want to exit? (y/n): ")
                if confirm_exit == 'y':
                    print("Goodbye!")
                    return 
                elif confirm_exit == 'n':
                    break
        else:
            print("Error: Option " + choice + " does not exist. Please choose between 1 and 8.")
        
        input("Press ENTER to continue...")


display_menu()

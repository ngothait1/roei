def add_entry(id_number, name, age):
    if id_number in entries_dict:
        print("Error: ID already exists.")
        return
    entry = {"index": len(entries_list), "id": id_number, "name": name, "age": age}
    entries_list.append(entry)
    entries_dict[id_number] = entry
    print("ID", id_number, "saved successfully.")

def print_entry(entry):
    print("Index:", entry["index"])
    print("ID:", entry["id"])
    print("Name:", entry["name"])
    print("Age:", entry["age"])

def search_by_id(id_number):
    if id_number in entries_dict:
        print_entry(entries_dict[id_number])
    else:
        print("Error: ID not found.")

def average_age():
    if not entries_list:
        print("Error: No entries available.")
        return
    avg = sum(entry["age"] for entry in entries_list) / len(entries_list)
    print("Average age:", avg)

def print_all_names():
    for entry in entries_list:
        print("Index:", entry["index"])
        print("Name:", entry["name"])

def print_all_ids():
    for entry in entries_list:
        print("Index:", entry["index"])
        print("ID:", entry["id"])

def print_all_entries():
    for entry in entries_list:
        print_entry(entry)

def search_by_index(index):
    if not index.isdigit():
        print("Error: Input must be a number. '" + index + "' is not a number.")
        return
    index = int(index)
    if 0 <= index < len(entries_list):
        print_entry(entries_list[index])
    else:
        print("Error: Index out of range. Only", len(entries_list), "entries available.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add new entry")
        print("2. Search by ID")
        print("3. Print average age")
        print("4. Print all names")
        print("5. Print all IDs")
        print("6. Print all entries")
        print("7. Search by index")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            id_number = input("Enter ID: ")
            if not id_number.isdigit():
                print("Error: ID must be a number.")
                continue
            name = input("Enter name: ")
            age = input("Enter age: ")
            if not age.isdigit():
                print("Error: Age must be a number.")
                continue
            add_entry(int(id_number), name, int(age))
        
        elif choice == "2":
            id_number = input("Enter ID to search: ")
            if not id_number.isdigit():
                print("Error: ID must be a number.")
                continue
            search_by_id(int(id_number))
        
        elif choice == "3":
            average_age()
        
        elif choice == "4":
            print_all_names()
        
        elif choice == "5":
            print_all_ids()
        
        elif choice == "6":
            print_all_entries()
        
        elif choice == "7":
            index = input("Enter index: ")
            search_by_index(index)
        
        elif choice == "8":
            while True:
                confirm = input("Are you sure you want to exit? (y/n): ")
                if confirm == "y":
                    print("Exiting program...")
                    return
                elif confirm == "n":
                    break
        else:
            print("Error: Option", choice, "not available. Please choose a valid option.")
        
        input("Press ENTER to continue...")


entries_list = []
entries_dict = {}
main()

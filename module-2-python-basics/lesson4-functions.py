"""
What is Function?
Imagine you are managing a shelter full of pets. Lists are like a master notebook where you write down every pet's details line by line.
Loops allow you to automatically turn through the pages of that notebook one by one to perform tasks like counting how many pets are available for adoption versus already adopted, or searching for a specific pet's name without having to inspect every entry manually.

Vocabolary:
- list: A data structure that stores multiple items in a single variable in sequential order. 
- for loop: A control flow statement used to iterate over elements in a list one at a time. 
- while loop: A loop that keeps executing a block of code continuously as long as a specified condition remains True. 
- increment: Increasing the value of a counter variable (e.g., count = count + 1) to keep track of occurrences. - conditional statement: Statements (if / elif / else) that check whether certain criteria are met before executing code.

 CODE:
"""
pets = []

def display_menu():
    print("=== Pet Adoption Records Manager ===")
    print("1. Add new pet")
    print("2. View pet")
    print("3. Count available and adopted pet")
    print("4. Find pet")
    print("5. Remove pet")
    print("6. Exit")

    choice = input("Enter your choice from numbers 1-6: ")
    return choice

def add_pet(pet_list):
    name = input("Enter the pet name: ")
    a_type = input("Enter the animal type: ")
    status = input("Enter the status: Available or Adopted: ")

    pet_info = name + " - " + a_type + " - " + status
    pet_list.append(pet_info)
    print(f"Pet {pet_info} is added!")

def view_pets(pet_list):
    if len(pet_list) == 0:
        print("No pets added yet!")
    else:
        print("View All Pets")
        for pets in pet_list:
            print(pets)

def count_available_adopted(pet_list):
    if len(pet_list) == 0:
        print("No pets in inventory.")
        return 0, 0

    available = 0
    adopted = 0

    for pet in pet_list:
        if "Available" in pet:
            available = available + 1
        elif "Adopted" in pet:
            adopted = adopted + 1

    print("Available pets:", available)
    print("Adopted pets:", adopted)
    return available, adopted

def find_pet(pet_list):
    if len(pet_list) == 0:
        print("Not Found")
        return 

    s_name = input("Enter a name: ")
    found = False 

    for pets in pet_list:
        if s_name in pets:
            print(f"Found the {pets}")
            found = True
            break

    if not found:
        print("Not in the list!")

def remove_pet(pet_list):
    if len(pet_list) == 0:
        print("Not Found")
        return

    r_name = input("Enter a name to remove: ")
    found = False 

    for pets in pet_list:
        if r_name in pets:
            pet_list.remove(pets)
            print(f"Successfully remove the {pets}")
            found = True
            break

    if not found: 
        print("Not Found")

def main():
    running = True
    while running:
        choice = display_menu()
        
        if choice == "1":
            add_pet(pets)
        elif choice == "2":
            view_pets(pets)
        elif choice == "3":
            count_available_adopted(pets)
        elif choice == "4":
            find_pet(pets)
        elif choice == "5":
            remove_pet(pets)
        elif choice == "6":
            print("Exit")
            running = False
        else:
            print("Incorrect Input")

main()

"""
MISTAKE:
A mistake I made was with the'count_available_adopted' function where the counter wasn't incrementing at first. 
This happened because the string matching condition in the 'if' statement didn't match the exact casing or format of the status in the pet string (for example, looking for 'available' in lowercase instead of 'Available' with a capital 'A'). 
Because the condition evaluated to False, the increment code (available = available + 1) was skipped entirely during the loop iterations.


"""
Module 2 — Lesson 3: Loops & Lists
Student: Viar, Paolaine Esther M.
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Imagine your mom asks you to go to the grocery store and hands you a shopping list. A 'list' in coding is 
just like that paper, it holds multiple items in a specific order so you can keep track of them. 

A 'loop' is like what happens when you go to pay at the cashier, the cashier scans each item on your list 
one by one. If you reach the checkout and realize you missed an item from your mom's list, you have to 
loop back through the store aisles, find the missing item, and return to the cashier to scan it again 
until everything on the list is checked off.


============================================
KEY VOCABULARY
============================================
- list: An ordered collection of items stored in a single variable using square brackets, like ['milk', 'eggs']
- for loop: A block of code that repeats a set number of times, usually by stepping through each item in a list one by one
- while loop: A block of code that keeps repeating continuously as long as a specific condition remains True (like searching the store until no items are missed)
- index: The numerical position of an item inside a list, starting at 0 for the first item
- iteration: One single cycle or pass through a loop (like scanning one item or taking one trip back to find a missing item)
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

moms_list = ["Milk", "Eggs", "Bread", "Butter"]
cart = ["Milk", "Bread"] 

print("--- Cashier checks your cart ---")

for item in cart:
    print(f"Cashier scanned: {item}")

print("\nOh no! You missed some items from Mom's list!")

while len(cart) < len(moms_list):
    for item in moms_list:
        if item not in cart:
            print(f"Going back to the aisle to get missed item: {item}...")
            cart.append(item)
            print(f"Returned to cashier and scanned: {item}")

print("\nAll items from Mom's list are checked out!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

1. Forgetting that list indexing starts at 0, not 1
2. Creating an infinite loop in a 'while' loop by forgetting to update the condition (like forgetting to add the missing items to the cart, causing you to run around the store forever!).



============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""

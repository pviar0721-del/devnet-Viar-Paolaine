"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Viar, Paolaine Esther M.
Date: 09/27/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow with if, elif, and else is like giving your computer a main plan and a set of backup plans. 
You tell the code "IF this condition is true, do Plan A. ELIF (else if) Plan A isn't true, try Plan B instead. 
ELSE, if none of those conditions worked, default to Plan C." It allows the program to make decisions and 
take different paths depending on the situation.


============================================
KEY VOCABULARY
============================================
- condition: A statement or rule that evaluates to either True or False
- if / elif / else: This checks the condition in order. For every True statement it falls in True. There is an alternative condition which is the elif. Lastly, the else acts as the final plan if the statement falls False.
- comparison operator: Symbols used to compare values, such as ==, !=, >, or <
- boolean expression: An expression that evaluates directly to either True or False.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

my_allowance = 200

if my_allowance >= 150:
    print("Plan A: Have a fancy date.")
elif budget >= 50:
    print("Plan B: Have a tusok-tusok date.")
else:
    print("Plan C: Sleep.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Using a single equals sign (=) instead of a double equals sign (==) inside an 'if' statement. 
A single '=' assigns a value to a variable, while '==' compares two values to see if they are equal.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""

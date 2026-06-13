# Software Engineering Fundamentals
# - Software is a collection of instructions that tell a computer what to do
# - A software called a language for example Python, Java, C++, etc

# - Software Engineering - is the process of designing, creating, testing, and maintaining software

# - Software Designing Principles:
# 1. Planning
# 2. Drafting
# 3. Coding
# 4. Testing

# Pseudo Code -
# - is a description of how a task should function like 
# - is a high-level description of a program to outline the logic 
# and structure of the code.

# Example of Pseudo Code:
# Cooking Pap
# 1. Switch the stove on - Action
# 2. Place the pot on the stove - Action
# 3. Pour water into the pot - Action
# 4. Wait for water to boil - Condition
# 5. Add the maize meal to the boiling water - Action
# 6. Stir the mixture continuously to prevent lumps - Action
# 7. Cook for some minutes until the pap thickens - Condition 
# 8. Switch off the stove - Action
# 9. Serve the pap - Action

# 2. Drafting
# - is the process of creating a rough sketch of the software based on the pseudo code
# Example of Drafting:
# 1. Identify variables
# 2. Identify functions/methods

# 1. Identify variables - noun
# 1.1 stove
# 1.2 pot
# 1.3 water
# 1.4 maize meal
# 1.5 pap







# Making tea
"""
Pour water into the kettle - Action
Switch on the kettle - Action
Wait for the water to boil - Condition
Fetch the cup - Action
Place the ingredients in the cup -Action
Pour the boiling water into the cup - Action
Stir the mixture - Action
Serve the tea - Action
""" 

# Variables:
"""
1. water
2. kettle
3. cup
4. ingredients
"""


# Coding
# - is a process writing step by step instruction that tell a computer how to perform a task
# - is the process of translating the pseudo code and draft into a programming language like Python

# What are the tools we need to write code?
"""
1. Variables - is a container that holds a value/ temporary storage for data
2. Data Types - is a classification of data that tells the computer how to interpret the data
3. Operators - are symbols that perform operations on variables and values.
4. Functions/Methods - is a block of code that performs a specific task and can be reused in a program
"""

"""
Step 1 - Variables Intitalization - is the process of assigning a value to a variable
"""
water = False
kettle = False
cup = False
ingredients = False
is_water_boiled = False


"""
Step 2 - Defining functions/methods 
"""

#1. method to pour water into the kettle
def pour_water():
    print("Pouring water into the kettle...")

#2. function to switch on the kettle
def switch_on_kettle() -> bool:
    print("Switching on the kettle...")
    return True

# #3. Condition - Wait for the water to boil
# is_water_boiled = switch_on_kettle()
# if (is_water_boiled == True):
#     print("Water is boiling...")
# else:
#     print("Water is not boiling...")

#4. method to fetch the cup
def fetch_cup()->bool:
    print("Fetching the cup...")
    return True

#5. method to place the ingredients in the cup
def place_ingredients():
    print("Placing sugar and tea bags or coffee")

#6. method to pour the boiling water into the cup
def pour_boiling_water()->bool:
    print("Pouring boiling water into the cup...")
    return True

#7. method to stir the mixture
def stir_mixture():
    print("Stirring the mixture...")

#8. method to serve the tea
def serve_tea():
    print("Serving the tea...") 


pour_water()
switch_on_kettle()
is_water_boiled = switch_on_kettle()
if (is_water_boiled == True):
    print("Water is boiling...")
else:
    print("Water is not boiling...")
fetch_cup()
place_ingredients()
pour_boiling_water()
stir_mixture()
serve_tea()
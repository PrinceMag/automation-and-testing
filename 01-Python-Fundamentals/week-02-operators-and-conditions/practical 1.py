"""
# project 1
while True:
    student_results = int(input("Enter your grade: ")) # Well done  10/10

    if student_results <= 89: # Trap
        print("E")
    elif student_results <= 69:
        print("D")
    elif student_results <= 79:
        print("C")
    elif student_results <= 89:
        print("B")
    else:
        print("A")


#project 2
television_operation = (input("Enter your television operation: ")) # Well done 10/10

if television_operation == "green button":
    print("on")

else:
    print("off")


#project 3
church_attendence = (input("enter church attendence:")) # Well done 10/10

if church_attendence == "sunday":
    print("going to church")

else :
    print("not going to church")



#project 4
temperature = 20 # Excellent 10/10
if temperature >=25:
    print("hot")

else :
    print("cold")



# ====================Cooking pap program=====================================

def cook_pap():
    temperature = 0
    water = int(input("Enter the amount of water (in cups) for cooking pap: "))
    maize_meal = 3
    salt = 0.5
    is_the_pot_set = False

    # Preheat the stove/pot

    temperature = 3
    if temperature >= 3:
        print("Stove is preheated. Ready to cook pap.")
        is_the_pot_set = True
        if(is_the_pot_set == True):
            print("Pot is set on the stove.")
            # Add water to the pot
            print(f"Adding {water} cups of water to the pot.")

            if(water <= 0): # Error trapping/checking
                print("Error: Not enough water to cook pap.")
                return
            
            # Add maize meal to the pot
            print(f"Adding {maize_meal} cups of maize meal to the pot.")
            # Add salt to the pot
            print(f"Adding {salt} teaspoons of salt to the pot.")
            # Stir the mixture
            print("Stirring the mixture...")
            # Simulate cooking time
            print("Cooking pap... Please wait.")
    else:
        print("Preheating stove... Please wait.")


if __name__ == "__main__":
    cook_pap()
"""
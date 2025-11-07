food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_cabinet = food.split(',')
equipment_cabinet = equipment.split(',')
pets_cabinet = pets.split(',')
sleep_aids_cabinet = sleep_aids.split(',')

food_cabinet.sort()
equipment_cabinet.sort()
pets_cabinet.sort()
sleep_aids_cabinet.sort()


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food_cabinet, equipment_cabinet, pets_cabinet, sleep_aids_cabinet]
print("Cargo Hold:", cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
cabinet_number = int(input("Select a cabinet (0 - 3) in the cargo hold:"))


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
cabinet_number = int(input("Select a cabinet (0 - 3) in the cargo hold:"))
selected_cabinet = cargo_hold[cabinet_number]
if cabinet_number > 3 or cabinet_number <0:
    print(f"Invalid input.")
else:
    print("Selected cabinet:", selected_cabinet)


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”

cabinet_number = int(input("Select a cabinet (0 - 3) in the cargo hold:"))
item_name = str(input("Select an item:"))
if cabinet_number > 3 or cabinet_number <0:
    print(f"Invalid input.")
else:
    selected_cabinet = cargo_hold[cabinet_number]

    if item_name in selected_cabinet:
        print(f"Selected cabinet: {selected_cabinet} does contain {item_name}")
    else:
        print(f"Selected cabinet: {selected_cabinet} does not contain {item_name}")
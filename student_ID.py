#Joshua
id = input("input your student ID: ").strip().upper()

print(f"input: {id}")
if id == "AB123456":
    print(f"VALID ID - Masked ID {id[0:2]}****{id[6:]}")
elif id != "AB123456" and id[0:2].isalpha() != True:
    print("INVALID ID - first two characters must be letters")
elif id != "AB123456" and id[0:] != 8:
    print("INVALID ID - ID must be exactly 8 characters")
elif id != "AB123456" and id[3:].isdigit() != True:
    print("INVALID ID - Last 6 characters must be letters")
else:
    print("i... how'd you even get this?") #just added cuz i already did all of the things so i jsut added this incase SOMEHOW you got it. idk how you would tho
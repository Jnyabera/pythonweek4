# Part 1: Write to a file
with open("assignment.py", "w") as file:
        NewAssignmentDoc = file.write("Test writing")
print(NewAssignmentDoc)

# Part 2: Read from a file with error handling
try:
   with open("james.txt", "r") as file:
       james=file.read()
       print (james)
except FileNotFoundError:
    print("FIle not found")

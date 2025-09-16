print("Classroom Attendance System")

absentnumber = 0
presentnumber = 0
numberofstudent = int(input("Enter the Number Of Students: "))

for _ in range(numberofstudent):
    name = input("Enter the Name Of Student: ")
    
    while True:
        PA = input("Enter P for Present and A for Absent: ").upper()
        if PA in ["P", "A"]:
            break
        print("Invalid input! Only enter 'P' or 'A'. Please try again.")

    if PA == "P":
        presentnumber += 1
    else:
        absentnumber += 1

print(f"The Total Number Of Students is {numberofstudent}\nAbsent: {absentnumber}\nPresent: {presentnumber}")

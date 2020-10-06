### Sample python program
### Loan Process for Business /Govt EMP/ Private EMP

business_type = input("Enter Business_Type: ")

if business_type == "govt":
    salary = int(input("Salary: "))
    if salary >= 10000:
        print("Loan Approve for govt_job")
    else:
        print("No Loan for govt_job")


elif business_type == "Business":
    turn_over = int(input("Turn_over "))
    if turn_over >= 100000:
        print("Business Loan Approved")
    else:
        print("No Business Loan")



elif business_type == "private":
    salary = int(input("Salary: "))
    if salary >= 50000:
        print("Private Loan Approved")
    else:
        print("No Loan for Private Emp")
        print("Please change job and then come for loan")



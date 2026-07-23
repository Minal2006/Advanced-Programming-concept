driver=input("enter the drivers details married:")
age=int(input("enter the age of driver:"))
gender=input("enter the gender of driver:")
if driver=="married":
    print("driver is insured")
elif driver=="unmarried" and gender=="male" and age>=30:
    print("driver is insured")
elif driver=="unmarried" and gender=="female" and age>=25:
    print("driver is insured")
else:
    print("not insured")

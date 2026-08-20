emp1 = {"Python", "Java", "SQL", "HTML"}
emp2 = {"Python", "C++", "SQL", "CSS"}

print("Common skills:", emp1 & emp2)
print("Employee 1 only:", emp1 - emp2)
print("Employee 2 only:", emp2 - emp1)
print("All skills:", emp1 | emp2)
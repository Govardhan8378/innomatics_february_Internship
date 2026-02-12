marks = [45, 78, 90, 33, 60]

passed = 0
failed = 0

# Checking each student's marks
for mark in marks:
    if mark >= 50:
        passed += 1
    else:
        failed += 1

print("Total Students:", len(marks))
print("Total Passed Students:", passed)
print("Total Failed Students:", failed)

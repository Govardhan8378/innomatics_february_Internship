names = [" Alice ", "bob", " CHARLIE "]

cleanednames = []

for i in names:
    cleanname = i.strip().lower()
    cleanednames.append(cleanname)

print("Cleaned Names:", cleanednames)

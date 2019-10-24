names = input("Enter names:" )
names =  names.split()
for nam in names:
    if nam.startswith('a') or nam.endswith('l'):
        print(nam)


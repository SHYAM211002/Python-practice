n = input("Enter the words: ")
a = n.split()
d = {}

for i in a:
    if i not in d:  
        d[i] = 1    
    else:
        d[i] += 1   

print(d)

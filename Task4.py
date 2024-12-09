l1 = []
n = int(input("enter the number: "))

for i in range(n):
    a = int(input())
    l1.append(a)


even_l = []
odd_l = []
try: 
    for i in l1:
        if i%2 == 0:
            even_l.append(i)
        else:
            odd_l.append(i)
except Exception as e:
    print(f"{e}")
even_l.sort(reverse=True)
odd_l.sort(reverse=True)

merge1 = even_l
merge2 = odd_l



print("Even:", even_l)
print("Odd:", odd_l)
merged_list = []
even_index = 0
odd_index = 0

for i in range(max(len(even_l), len(odd_l))):
    if even_index < len(even_l):
            merged_list.append(even_l[even_index])
            even_index += 1
    if odd_index < len(odd_l):
            merged_list.append(odd_l[odd_index])
            odd_index += 1

   
print("Merged List:", merged_list)




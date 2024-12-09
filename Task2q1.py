def even_number(numbers):
    l1 = []
    for n in numbers:
        if n%2 == 0:
            l1.append(n)  
    return l1

def odd_number(numbers):
    l2 = []
    for n in numbers:
        if n%2 != 0:
            l2.append(n)  
    return l2


def sum_num(numbers):
    return sum(numbers)

user = input("Enter numbers: ")
numbers = list(map(int, user.split()))

even_no = even_number(numbers)
odd_no = odd_number(numbers)

even_sum = sum_num(even_no)
odd_sum = sum_num(odd_no)


print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")

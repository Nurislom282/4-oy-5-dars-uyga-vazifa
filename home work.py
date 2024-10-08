# 1
mahsulotlar = ["olma", "banan", "non", "sut"]

mahsulotlar.extend(["tuxum", "yog'"])

print(mahsulotlar)
# 2
numbers = [3, 7, 2, 9, 1]

max_number = max(numbers)
min_number = min(numbers)

print("Eng katta son:", max_number)
print("Eng kichik son:", min_number)
# 3
orders = {
    "Ali": "3 ta non",
    "Aziza": "2 ta olma",
    "Jasur": "1 ta kola",
    "Dilnoza": "5 ta banan"
}

customer_name = input("Xaridor nomini kiriting: ")

order = orders.get(customer_name)

if order:
    print(f"{customer_name}ning buyurtmasi: {order}")
else:
    print("Bunday xaridor topilmadi.")
# 4
juft_sonlar = [son for son in range(1, 101) if son % 2 == 0]

print(juft_sonlar)
# 5
def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2

    return median

numbers = [5, 2, 9, 1, 5, 6]
median = find_median(numbers)
print("Sorted list:", sorted(numbers))
print("Median:", median)

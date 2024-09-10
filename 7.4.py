def common_elements():
    first_numbers = [number for number in range(100) if number % 3 == 0]
    # print(first_numbers)
    second_numbers = [number for number in range(100) if number % 5 == 0]
    # print(second_numbers)
    return set(first_numbers).intersection(set(second_numbers))
print(common_elements())
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'Test1'
print("OK")
###
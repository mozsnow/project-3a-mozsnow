
num_1 = int(input("How many integers would you like to enter?"))
print("Please enter", num_1, "integers.")
_min = int(input())
_max = _min
for i in range(1, num_1):
    number = int(input())
    if number > _max:
        _max = number
    if number < _min:
        _min = number
print("Min:", _min)
print("Max:", _max)

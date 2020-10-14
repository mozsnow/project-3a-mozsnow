# get input from user
num_1 = int(input("How many integers would you like to enter?"))
# enter -4, 105,2, -7
print("Please enter", num_1, "integers:")
_min = int(input())
_max = _min
# integers are to be arranged from min to max
for i in range(1, num_1):
    number = int(input())
    if number > _max:
        _max = number
    if number < _min:
        _min = number
print("Min:", _min)
print("Max:", _max)

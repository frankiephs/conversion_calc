distance_dict = {
    "mm" : 1000,
    "cm" : 100,
    "m" : 1,
    "km" : .001
}

amount = float(input("How much? "))
from_unit = input("from unit? ")
to_unit = input("To unit? ")

multiply_by = distance_dict[to_unit]
standard = amount * multiply_by

divide_by = distance_dict[from_unit]
answer = standard / divide_by

print(f"There are {answer} {to_unit} in {amount} {from_unit}")

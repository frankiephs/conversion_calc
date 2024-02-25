# conversion calc

def calc():
    distance_dict = {
    "mm" : 1000,
    "cm" : 100,
    "m" : 1,
    "km" : .001
}

# returns val
def time(amount, from_unit, to_unit):
    time_dict = {
    "ms" : 1000,
    "s" : 100,
    "h" : 1,
    "d" : .001
}

def time(amount, from_unit, to_unit):


conv_type = input("what type of calc?")


amount = float(input("How much? "))
from_unit = input("from unit? ")
to_unit = input("To unit? ")

answer = 1 + 1


print(f"There are {answer} {to_unit} in {amount} {from_unit}")

distance_dict = {
    "mm" : 1000,
    "cm" : 100,
    "m" : 1,
    "km" : .001
}

# Time
time_dict = {
    "ms" : 3600000,
    "s" : 3600,
    "m" : 60,
    "h" : 1, # starting
    "d" : 0.0417,
    "year" : 0.0001141
}

# mass
mass_dict = {
    "mg" : 1000000,
    "g" : 1000,
    "kg" : 1, # starting
    "t" : .001
}


while True:
    # input
    category = input("what category? ")
    amount = float(input("How much? "))
    from_unit = input("from unit? ")
    to_unit = input("To unit? ")

    print("-- conversion calc --")
    def distance_calc():

        multiply_by = distance_dict[to_unit]
        standard = amount * multiply_by

        divide_by = distance_dict[from_unit]
        answer = standard / divide_by
        return answer


    def time_calc():
        multiply_by = time_dict[to_unit]
        standard = amount * multiply_by

        divide_by = time_dict[from_unit]
        answer = standard / divide_by
        return answer



    def mass_calc():
        multiply_by = mass_dict[to_unit]
        standard = amount * multiply_by

        divide_by = mass_dict[from_unit]
        answer = standard / divide_by
        return answer


    if category == "distance":
        print(distance_calc())
    elif category == "time":
        print(time_calc())

    elif category == "mass":
        print(mass_calc())
    else:
        print("error")

    
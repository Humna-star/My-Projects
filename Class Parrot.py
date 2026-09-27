class parrot:

    species = "birds"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = parrot ("Blu", 10)
woo = parrot ("Woo", 14)

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print("{} is {} year old".format(blu.name, blu.age))
print("{} is {} year old".format(woo.name, woo.age))
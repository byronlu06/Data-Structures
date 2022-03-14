ageone = 21
agetwo = 16
age3 = 0

def ageswap(age1, age2):
    age3 = age1
    age1 = age2
    age2 = age3
    return age1, age2

print('Swap')
(thing, thing2) = ageswap(ageone, agetwo)

print(ageone, agetwo)
print(thing, thing2)
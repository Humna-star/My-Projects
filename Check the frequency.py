test_dict = {'My': 9, 'life': 6, 'is': 8, 'a': 4, 'test': 9, 'that': 9, 'is': 6, 'to': 4, 'check': 9, 'the': 8, 'frequency': 9}

print("The original dictionary is : " + str(test_dict))

K = 9

res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("The frequency of K is : " + str(res))
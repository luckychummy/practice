# Python Program to create a List using custom key-value pair of a dictionary
# Input : test_list = [{'gfg': 1, 'is': 4, 'best': 6},
#              {'gfg': 10, 'is': 3, 'best': 7},
#              {'gfg': 9, 'is': 4, 'best': 2},
#              {'gfg': 4, 'is': 1, 'best': 0},
#              {'gfg': 6, 'is': 3, 'best': 8}], key, value = 'gfg’, 'best’
# Output : {1: 6, 10: 7, 9: 2, 4: 0, 6: 8}
test_list = [{'gfg': 1, 'is': 4, 'best': 6},
              {'gfg': 10, 'is': 3, 'best': 7},
              {'gfg': 9, 'is': 4, 'best': 2},
              {'gfg': 4, 'is': 1, 'best': 0},
              {'gfg': 6, 'is': 3, 'best': 8}]
res=dict()
key, value = 'gfg', 'best'
for i in test_list:
    res[i[key]] = i[value]
print(result)
# Input : test_list = [{‘gfg’ : 1, ‘is’ : 4, ‘best’ : 9},

#              {‘gfg’ : 6, ‘is’ : 3, ‘best’ : 8},

#              {‘gfg’ : 1, ‘is’ : 4, ‘best’ : 9},

#              {‘gfg’ : 1, ‘is’ : 1, ‘best’ : 9}]

# Output : [({‘gfg’: 1, ‘is’: 4, ‘best’: 9}, 2), ({‘gfg’: 6, ‘is’: 3, ‘best’: 8}, 1), ({‘gfg’: 1, ‘is’: 1, ‘best’: 9}, 1)]
from collections import Counter
test_list = [{'gfg': 1, 'is': 4, 'best': 9}, 
             {'gfg': 6, 'is': 3, 'best': 8}, 
             {'gfg': 1, 'is': 4, 'best': 9}, 
             {'gfg': 1, 'is': 1, 'best': 9}, 
             {'gfg': 6, 'is': 3, 'best': 8}]
temp = Counter(tuple(sorted(i.items())) for i in test_list)
print(temp)

res=[(dict([tuple(e) for e in i]), temp[i]) for i in temp]

print("Dictionary frequescyies", str(res))


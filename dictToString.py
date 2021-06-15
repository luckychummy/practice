# Input : test_dict = {‘Gfg’ : 4, ‘is’ : “1”, ‘best’ : [8, 10], ‘geek’ : (10, 11, 2)}, list_delim, tuple_delim = ‘*’, ‘,’

# Output : {‘Gfg’: ‘4’, ‘is’: ‘1’, ‘best’: ‘8*10’, ‘geek’: ‘10,11,2’}

# Explanation : List elements are joined by *, tuples by , symbol.

test_dict = {'Gfg' : 4, 'is' : "1", 'best' : [8, 10], 'geek' : (10, 11, 2)}

print("The original list is ",str(test_dict))

list_delim, tuple_dim='*',','
res=dict()

for i in test_dict:
    if isinstance(test_dict[i], list):
        res[i]=list_delim.join([str(ele) for ele in test_dict[i]])
    elif isinstance(test_dict[i], tuple):
        res[i]=tuple_dim.join([str(e) for e in test_dict[i]])
    else:
        res[i]=test_dict[i]
        
print("The updated list is ",str(res))
def removedup(str):
    l=[]
    for ch in str:
       if ch not in l:
           l.append(ch)
    return ("").join(l)

print(removedup("appliedcourse"))
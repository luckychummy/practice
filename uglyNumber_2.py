
def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    ugly=[1]
    #print(ugly[0])
    two,three,five=0,0,0
    while len(ugly)<n:
        print("hi",ugly[-1])
        while ugly[two]*2<=ugly[-1]:
            print("jai ho")
            two +=1
        while ugly[three]*3<=ugly[-1]:
            three +=1
        while ugly[five]*5<=ugly[-1]:
            five +=1
        ugly.append(min(ugly[two]*2, ugly[three]*3, ugly[five]*5))
        
    return ugly[-1]

if __name__ == '__main__':
    value=nthUglyNumber(3);
    print(value)
                
        
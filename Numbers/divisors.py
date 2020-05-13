def make_divisors(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if i*i != n:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n//i)
    return divisors
    
                

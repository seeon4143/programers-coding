def solution(numer1, denom1, numer2, denom2):
    a=numer1*denom2+numer2*denom1
    b=denom1*denom2
    i=2
    while True:
        if(a%i==0 and b%i==0):
            a=a/i
            b=b/i
            continue
        i+=1
        if i==1000:
            break
    answer = [a,b]
    return answer
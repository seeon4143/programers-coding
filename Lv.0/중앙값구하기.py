def solution(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if j>i and array[i]>array[j]:
                array[i],array[j]=array[j],array[i]
    answer= array[((len(array)+1)//2)-1]
                
    return answer
#finding majority element
maj_arr=[2,4,6,2,4,2,2,9,2]
def majority_element(arr):
    n=len(arr)//2
    lst={}
    for i in arr:
        if i in arr:
            lst[i]=lst.get(i,0)+1
        else:
            lst[i]=1
    for k,v in lst.items():
        if v >= n:
            return k
print(f"\nThe majority element of array {maj_arr} is {majority_element(maj_arr)}")
#Second way Moore's algorithm
def moore_algo(arr):
    n=len(arr)
    candidate=-1
    count=0
    for num in arr:
        if count==0:
            candidate=num
        elif num==candidate:
            count+=1
        else:
            count-=1
    c_count=0
    for i in arr:
        if i==candidate:
            c_count+=1
    if c_count>=n//2:
        return candidate
    else:
        return -1
print(f"\nThe majority element of array {maj_arr} using Moore's algo is {moore_algo(maj_arr)}")
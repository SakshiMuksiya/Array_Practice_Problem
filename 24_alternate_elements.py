from collections import deque
#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#arrange the elements alternately
def alternate_ele(arr):
    sarr=sorted(arr)
    dq=deque(sarr)
    res=[]
    while dq:
        if dq:
            res.append(dq.pop())
        if dq:
            res.append(dq.popleft())
    return res
print(f"\nThe alternate large-small element array is {alternate_ele(arr)}")
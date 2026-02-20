import math
#Product of array except self
pro_arr=[1,2,3,4]
def product_except_self(arr):
    n=len(arr)
    preproduct=[1]* len(arr)
    sufproduct=[1]* len(arr)
    res=[0]*len(arr)
    for i in range(1,n):
        preproduct[i]=arr[i-1]* preproduct[i-1]
    for j in range(n-2,-1,-1):
        sufproduct[j]=arr[j+1]* sufproduct[j+1]
    for k in range (n):
        res[k]=preproduct[k]*sufproduct[k]
    return res
print(f"\nThe product array of {pro_arr} is {product_except_self(pro_arr)}")
def product_except_self_log(arr):
    n=len(arr)
    ans=[0]*n
    zero_count=0
    for i in arr:
        if arr==0:
            zero_count+=1
    if zero_count>1:
        return ans
    if zero_count ==1:
        prod=1
        zeroIndex=-1
        for i in range(n):
            if arr[i]!=0:
                prod*=arr[i]
            else:
                zeroIndex=i
        ans[zeroIndex]=prod
        return ans
    sumlog=0.0
    sign=1
    for i in range(0,n):
        sumlog+=math.log10(abs(arr[i]))
        if arr[i]<0:
            sign*=-1
    for i in range(n):
        logval=sumlog-math.log10(abs(arr[i]))
        signval= -sign if arr[i]<0 else sign
        res=pow(10.0,logval)
        ans[i]=int(sign*(res+0.5)) 
    return ans
print(f"\nThe product array of {pro_arr} using log is {product_except_self_log(pro_arr)}")
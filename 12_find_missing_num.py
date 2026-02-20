#find the missing number from 1 to n element array
numb_arr=[1,2,3,4,5,7,8,9]
n=len(numb_arr)+1
expected_sum= n*(n+1)//2
actual_sum=sum(numb_arr)
print(f"\nThe missing element from the array {numb_arr} is: ",expected_sum-actual_sum)
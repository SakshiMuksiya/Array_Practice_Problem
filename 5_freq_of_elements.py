#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#Frequency count of elements
print("\nFrequency Count of elements")
freq={}
for element in arr:
    if element in freq:
        freq[element]+=1
    else:
        freq[element]=1
for k,v in freq.items():
    print(f"Element:{k} and Count={v}")
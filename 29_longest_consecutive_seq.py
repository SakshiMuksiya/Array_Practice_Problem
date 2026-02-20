#Longest consecutive sequence of integers
seq_arr=[1,3,6,7,2,4]
def longest_consec_subseq(arr):
    st=set()
    ans=0
    for i in arr:
        st.add(i)
    for val in arr:
        if val in st and (val-1) not in st:
            curt=val
            cnt=0
            while curt in st:
                st.remove(curt)
                curt+=1
                cnt+=1
            ans=max(ans,cnt)
    return ans
print(f"\nThe longest consecutive subsequence in the array {seq_arr} is ")
print(f"{longest_consec_subseq(seq_arr)}")
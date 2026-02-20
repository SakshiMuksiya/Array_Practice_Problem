#Find maximum product pair
prod_pair=[2,5,4,1,8,3]
def max_prod_pair(arr):
    if len(arr)<2:
        print("\nNo pairs exist")
        return 
    if len(arr)==2:
        print("\n",arr[0] ,' ', arr[1])
        return
    posa,posb=0,0
    nega,negb=0,0
    for ele in arr:
        if ele>0:
            if ele>=posa:
                posb=posa
                posa=ele
            elif ele>=posb:
                posb=ele
        elif ele<0:
            if ele>abs(nega):
                negb=nega
                nega=ele
            elif ele>abs(negb):
                negb=ele
    if (posa*posb)<(nega*negb):
        print(f"\nMaximum product pair :({nega},{negb})")
    else:
        print(f"\nMaximum product pair :({posa},{posb})")
max_prod_pair(prod_pair)
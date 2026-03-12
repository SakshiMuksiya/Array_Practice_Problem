from collections import defaultdict
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    
    positions = defaultdict(list)
    for i, dish in enumerate(A):
        positions[dish].append(i)
    
    def max_non_adjacent(pos_list):
        count = 0
        last_picked = -2 
        for pos in pos_list:
            if pos - last_picked > 1:  
                count += 1
                last_picked = pos
        return count
    
    best_type = -1
    best_count = -1
    for dish_type in sorted(positions.keys()):  
        count = max_non_adjacent(positions[dish_type])
        if count > best_count:
            best_count = count
            best_type = dish_type
    print(best_type)

T = int(input())
for _ in range(T):
    solve()
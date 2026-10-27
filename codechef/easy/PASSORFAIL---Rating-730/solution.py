# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    n, x, p = map(int, input().split())
    
    # Calculate Chef's total score
    correct_marks = x * 3
    incorrect_penalty = (n - x) * 1
    total_score = correct_marks - incorrect_penalty
    
    # Check if he passes or fails
    if total_score >= p:
        print("PASS")
    else:
        print("FAIL")
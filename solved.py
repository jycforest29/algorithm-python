import sys
input = sys.stdin.readline

def possible(i, j, k):
    if k == "<":
        return i < j
    return i > j

def f(depth, s):
    global min_ans, max_ans

    if depth == k+1:
        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s
        return
    
    for i in range(10):
        if not visit[i]:
            if depth == 0 or possible(s[-1], str(i), inputs[depth-1]):
                visit[i] = 1
                f(depth+1, s+str(i))
                visit[i] = 0


k = int(input())
inputs = input().split()
visit = [0 for _ in range(10)]
min_ans, max_ans = "", ""
f(0, "")
print(max_ans)
print(min_ans)
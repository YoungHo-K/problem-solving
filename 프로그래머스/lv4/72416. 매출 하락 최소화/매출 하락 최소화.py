
from collections import defaultdict

global tree


def solution(sales, links):
    global tree

    tree = defaultdict(list)
    for a, b in links:
        tree[a].append(b)
        
    dp = [[0, 0]] + [[0, s] for s in sales]
    dfs(1, dp)
    
    return min(dp[1])
        

def dfs(node, dp):
    global tree
    
    if len(tree[node]) == 0:
        return
    
    min_cost, not_pick, min_diff = 0, 0, float("inf")
    for child in tree[node]:
        dfs(child, dp)
        
        min_cost += min(dp[child])
        if dp[child][0] < dp[child][1]:
            not_pick += 1
            min_diff = min(min_diff, dp[child][1] - dp[child][0])
                
    dp[node][1] += min_cost
    dp[node][0] += min_cost + min_diff if not_pick == len(tree[node]) else min_cost
        
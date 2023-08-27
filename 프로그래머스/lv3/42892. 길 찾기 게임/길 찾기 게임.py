import sys
import copy

from collections import defaultdict

global levels

sys.setrecursionlimit(2000)


def solution(nodeinfo):
    global levels
    
    tree = defaultdict(list)
    for index, (x, y) in enumerate(nodeinfo):
        tree[y].append((x, index + 1))

    levels = list(tree.keys())
    levels.sort(reverse=True)
                
    for l in levels:
        tree[l].sort(reverse=True)
    
    preorder = list()
    search_order(copy.deepcopy(tree), preorder, -1, 100_001, 0, mode="pre")
    
    postorder = list()
    search_order(copy.deepcopy(tree), postorder, -1, 100_001, 0, mode="post")
    
    return [preorder, postorder]
    
    
def search_order(tree, order, left, right, depth, mode="pre"):
    global levels
    
    if len(levels) == depth:
        return

    current_level = levels[depth]    
    if len(tree[current_level]) == 0:
        return

    if not (left < tree[current_level][-1][0] < right):
        return 
    
    x, node_id = tree[current_level].pop()
    
    if mode == "pre":
        order.append(node_id)

    search_order(tree, order, left, x, depth + 1, mode)
    search_order(tree, order, x, right, depth + 1, mode)
    
    if mode == "post":
        order.append(node_id)

    
import random

pruned_states = 0

#Task-Lab03-18101635
def minimax_algo(depth, max_depth, index, branch, leaf_nodes, Alpha, Beta, maximizing_Player):
    global pruned_states
    
    if depth == 0:
        return leaf_nodes[index]

    if maximizing_Player:
        min_eval = -float("inf")
        for i in range (branch):
            new_index= index*branch+i
            value = minimax_algo(depth-1, max_depth, new_index, branch, leaf_nodes, Alpha, Beta, False)                      
            min_eval = max(min_eval, value)
            Alpha = max(Alpha, value)          
            if Beta <= Alpha:
                pruned_states+=1   
                break                                     
        return min_eval

    else:
        max_eval = float("inf")
        for i in range(branch):
            new_index= index*branch+i
            value = minimax_algo(depth-1, max_depth, new_index, branch, leaf_nodes, Alpha, Beta, True)        
            max_eval = min(max_eval, value)
            Beta = min(Beta, value)            
            if Beta <= Alpha:
                pruned_states+=1   
                break           
        return max_eval
    


turn = int(input("Turn: "))
DEPTH = 2*turn
branching_factor = int(input("Number of branch for each node: "))
minimum_leaf_node , maximum_leaf_node = map(int,input("Minimum & Maximum value: (ex- 1 20) ").split())
number_of_leaf_node = pow(branching_factor, DEPTH)


leaf_nodes = [random.randint(minimum_leaf_node,maximum_leaf_node) for i in range(number_of_leaf_node)]
#leaf_nodes = [3,12,8,2,4,6,14,5,2]

Maximum_amount = minimax_algo(DEPTH, DEPTH, 0, branching_factor, leaf_nodes, -float("inf"), float("inf"), True)
after_alphaBeta_pruning = number_of_leaf_node - pruned_states

print("Leaf nodes value:",leaf_nodes)
print()
print("Depth:",DEPTH)
print("Branch:",branching_factor)
print("Terminal States (Leaf Nodes):",number_of_leaf_node)
print("Maximum amount:",Maximum_amount)
print("Comparisons Before Alpha-beta Pruning:",number_of_leaf_node)
print("Comparisons After Alpha-beta Pruning:",after_alphaBeta_pruning)

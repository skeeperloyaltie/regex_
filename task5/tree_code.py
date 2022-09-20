
import random

def tree_code(treeSize):
    if treeSize == 0:
        return []
    elif treeSize == 1:
        return [0]
    else:
             
        if random.random() < 0.5:
            # left subtree
            leftTree = tree_code(treeSize - 1)
            return [0] + leftTree
        else:
            # right subtree
            rightTree = tree_code(treeSize - 1)
            return [1] + rightTree
def probability_of_degenerate_height_helper(height):
    if height == 0:
        return 1
    elif height == 1:
        return 1
    else:
       
        if random.random() < 0.5:
            # left subtree
            return probability_of_degenerate_height_helper(height - 1)
        else:
            # right subtree
            return probability_of_degenerate_height_helper(height - 1)

def probability_of_degenerate_height(numNodesCreated):
    numTrees = 0
    for i in range(numNodesCreated):
        numTrees += probability_of_degenerate_height_helper(i)
    return numTrees / (2 ** numNodesCreated)
    
def main():
    numNodesCreated = 7
    print("Probability of degenerate height of 7 node")
    print("{:<10}{:<10}".format("Height", "Probability"))
    for i in range(numNodesCreated):
        print("{:<10}{:<10.5f}".format(i, probability_of_degenerate_height(i)))

if __name__ == "__main__":
    main()



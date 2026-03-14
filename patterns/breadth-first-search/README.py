


"""
# bfs pattern
# vertical search: Explores as far as possible along each branch before backtracking.
----
# TRIGGERS SEEN (when and why we use it)
- invert-binary-tree: used to swap nodes level by level going all the way to base and swapping

----
psuedo code (recursive):
- Define a base case: If the current node is None, return a default value.
- Pre-order Logic: Perform operations on the current node before visiting children.
- Recurse on the left child.
- Recurse on the right child.
- Post-order Logic: Perform operations after visiting children (using the values returned by the subtrees).

"""

def dfs_recursive(root):
    # 1. Base Case: What happens at the end of a branch?
    if not root:
        return None # or 0, or False, depending on the problem
    
    # 2. Pre-order Processing (Optional)
    # e.g., if root.val == target: return True
    
    # 3. Recurse: Dive deeper into the tree
    left_result = dfs_recursive(root.left)
    right_result = dfs_recursive(root.right)
    
    # 4. Post-order Processing (Optional)
    # This is where you "bubble up" information from the bottom.
    # e.g., return max(left_result, right_result) + 1
    
    return # The synthesized result of this subtree

def dfs_iterative(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        # --- PROBLEM LOGIC GOES HERE ---
        # e.g., visit(node)
        # -------------------------------
        
        # Note: Push Right then Left so that Left is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)



"""
# bfs pattern
# level order search: processes nodes level by level
----
# TRIGGERS SEEN (when and why we use it)

- (inverting a binary tree): used to swap nodes level by level going down a binary tree.

----
psuedo code:
- check if source_node is valid
- initialize queue 'Q' with source_node
- initialize level_size to len(Q)
- while Q is not empty:
    - assign level_size to len(Q)
    - for number in n to level_size (each node)
        - initialize temp_node to first node in queue (removing node from queue)
        - ### --- processing stage for problem --- ###
        - if the temp_node has a left child: append to Q
        - if the temp_node has a right child: append to Q

"""

from collections import deque

def bfsTemplate(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            
            # --- PROBLEM LOGIC GOES HERE ---
            # Examples: 
            # if node.val == target: return True
            # current_level.append(node.val)
            # -------------------------------
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
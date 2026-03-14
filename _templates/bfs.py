def bfs(source_node):
    from collections import deque
    q = deque()
    q.append(source_node)
    while q:
        num_nodes_at_current_level = len(q)
        for _ in range(num_nodes_at_current_level):
            node = q.popleft()
            
            # this is where the processing is usually done around here
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return q
    
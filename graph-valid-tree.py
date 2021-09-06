class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges) == 0 and n == 1:
            return True
        graph = {}
        # builds the graph
        for node1, node2 in edges:
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append(node2)
            graph[node2].append(node1)
        # see if there are any cycles
        if len(graph) != n:
            return False
        queue = [(0, -1)]
        visited = set([0])
        while len(queue) > 0:
            (cur, par) = queue.pop(0)
            for node in graph[cur]:
                if node == par:
                    continue
                if node in visited:
                    return False
                visited.add(node)
                queue.append((node, cur))
        print(f"possibly true {n} {len(visited)}")
        return len(visited) == len(graph) # final check to see if all nodes have been visited

from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list = defaultdict(set)
        parent = set([0])
        for nfrom, nto in edges:
            if nfrom in parent:
                adj_list[nfrom].add(nto)
                parent.add(nto)
            else:
                adj_list[nto].add(nfrom)
                parent.add(nfrom)
        res = []
        
        for index, label in enumerate(labels):
            count = 0
            stack = [index]
            visited = set()
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                if node < len(res) and labels[node] == label:
                    count += res[node]
                    continue
                count += (labels[node] == label) 
                for child in adj_list[node]:
                    stack.append(child)
            res.append(count)
        return res
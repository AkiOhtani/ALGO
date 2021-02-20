from collections import defaultdict, Counter

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(index):
            visited.add(index)
            
            label_count = Counter()
            
            for child in adj_list[index]:
                if child in visited:
                    continue
                label_count += dfs(child)
            
            label_count[labels[index]] += 1
            res[index] = label_count[labels[index]]
            
            return label_count
            
        adj_list = defaultdict(set)
        
        for nfrom, nto in edges:
            adj_list[nfrom].add(nto)
            adj_list[nto].add(nfrom)
        
        visited = set([])
        
        res = [0 for num in range(n)]
        
        dfs(0)
        
        return res
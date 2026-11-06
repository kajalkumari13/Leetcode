class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs += [(-id, time+x+1) for id, time in logs]
        logs += enumerate(queries, n+1)
        logs.sort(key=itemgetter(1))
        recent = Counter()
        for id, _ in logs:
            if id > n:
                queries[id-n-1] = n - len(recent)
            elif id > 0:
                recent[id] += 1
            else:
                recent[-id] -= 1
                if not recent[-id]:
                    del recent[-id]
        return queries
class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(n)]

        for caller, called in invocations:
            graph[caller].append(called)

        suspicious = [False] * n
        suspicious[k] = True
        queue = [k]
        index = 0

        while index < len(queue):
            method = queue[index]
            index += 1

            for called in graph[method]:
                if not suspicious[called]:
                    suspicious[called] = True
                    queue.append(called)

        for caller, called in invocations:
            if not suspicious[caller] and suspicious[called]:
                return list(range(n))

        return [method for method in range(n) if not suspicious[method]]
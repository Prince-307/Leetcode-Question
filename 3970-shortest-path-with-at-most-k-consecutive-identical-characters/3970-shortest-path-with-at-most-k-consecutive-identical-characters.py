class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][count] = minimum cost to reach this state
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Initially, node 0 has a consecutive run of length 1
        dist[0][1] = 0

        # (cost, node, consecutive_count)
        pq = [(0, 0, 1)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            # Ignore outdated states
            if cost != dist[u][count]:
                continue

            # First valid minimum-cost state at the destination
            if u == n - 1:
                return cost

            for v, w in graph[u]:

                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1

                # Cannot exceed k consecutive identical characters
                if next_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][next_count]:
                    dist[v][next_count] = new_cost

                    heapq.heappush(
                        pq,
                        (new_cost, v, next_count)
                    )

        return -1
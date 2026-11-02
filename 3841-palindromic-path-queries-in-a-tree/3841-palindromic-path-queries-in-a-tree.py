class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        chars = [1 << (ord(c) - ord('a')) for c in s]

        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        parent = [0] * n

        # Iterative DFS: Euler tour
        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = u if p == -1 else p
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))

                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer
                timer += 1

        # Binary lifting for LCA
        LOG = n.bit_length()
        up = [[0] * n for _ in range(LOG)]
        up[0] = parent[:]

        for j in range(1, LOG):
            for u in range(n):
                up[j][u] = up[j - 1][up[j - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            j = 0

            while diff:
                if diff & 1:
                    u = up[j][u]
                diff >>= 1
                j += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # Fenwick tree for XOR
        size = 2 * n
        bit = [0] * (size + 1)

        def update(index, value):
            index += 1
            while index <= size:
                bit[index] ^= value
                index += index & -index

        def prefix_xor(index):
            index += 1
            result = 0

            while index > 0:
                result ^= bit[index]
                index -= index & -index

            return result

        # Store each node's mask at entry and exit times
        for u in range(n):
            update(tin[u], chars[u])
            update(tout[u], chars[u])

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                new_mask = 1 << (ord(c) - ord('a'))
                delta = chars[u] ^ new_mask

                update(tin[u], delta)
                update(tout[u], delta)

                chars[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])

                pu = prefix_xor(tin[u])
                pv = prefix_xor(tin[v])

                w = lca(u, v)
                mask = pu ^ pv ^ chars[w]

                answer.append((mask & (mask - 1)) == 0)

        return answer
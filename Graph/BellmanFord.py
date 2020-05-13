def BellmanFord(s, N, Edge):
    INF = 10**20
    dist = [INF] * N
    dist[s] = 0
    for i in range(N):
        isUpdated = False
        for t in range(N):
            if dist[t] == INF:
                continue
            for v,c in Edge[t]:
                if dist[t]+c < dist[v]:
                    dist[v] = dist[t]+c
                    isUpdated = True
        if not isUpdated:
            break
        elif i==N-1:
            return -1
    return dist

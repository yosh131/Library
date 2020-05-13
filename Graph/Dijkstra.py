# -*- coding: utf-8 -*-
import heapq


def dijkstra(S, N, Edge):
    # S: start vertex
    # N: number of vertices
    # Edge: adjacent list [node, cost]
    
    INF = 10**20
    dist = [INF]*N
    dist[S] = 0
    que = [[0, S]]
    heapq.heapify(que)
    
    while que:
        c, v = heapq.heappop(que)
        if dist[v] < c: continue

        for nv, nc in Edge[v]:
            if c+nc < dist[nv]:
                dist[nv] = c+nc
                heapq.heappush(que, [c+nc, nv])
    
    return dist
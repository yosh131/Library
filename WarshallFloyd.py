def WarshallFloyd(d, N):
    #d[i][j]: iからjへの最短距離（隣接行列）
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
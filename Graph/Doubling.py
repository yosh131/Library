
class doubling:
    # A: 各頂点の親の番号 (0-indexed)
    # 頂点SのK個上の親の番号を返す．

    # 構築
    def __init__(self, A, K):
        self.M = 0
        temp = K
        N = len(A)
        self.Kb = []
        # 2^(M-1)乗まで計算
        while temp>0:
            self.M += 1
            self.Kb.append(temp&1)
            temp>>=1

        # 初期化
        self.nexts = [[-1]*N for _ in range(self.M)]
        for i in range(N):
            self.nexts[0][i] = A[i]

        # ダブリング計算
        for t in range(1,self.M):
            for i in range(N):
                self.nexts[t][i] = self.nexts[t-1][self.nexts[t-1][i]]

    # クエリ：ノードSのK個上のノードの番号を求める
    def query(self, S, K):
        res = S
        for i in reversed(range(self.M)):
            if self.Kb[i]:
                res = self.nexts[i][res]
        return res



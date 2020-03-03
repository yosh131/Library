
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] #各ノードの親番号
        self.rank = [0] * (n) #各ノードのランク（木の高さ）
        self.root = [-1]*(n+1) # -（各ノードの属するグループの要素数）

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            # node = [x]
            # cur = node[0]
            # while self.par[cur] != cur:
            #     cur = self.par[cur]
            #     node.append(self.par[cur])
            
            # for n in node:
            #     self.par[n] = cur
            
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.root[x] += self.root[y]
            self.root[y] = self.root[x]
        else:
            self.par[y] = x
            self.root[x] += self.root[y]
            self.root[y] = self.root[x]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
                
    # グループ数
    def groupsize(self):
        cnt = 0
        for i,x in enumerate(self.par):
            if x == i:
                cnt += 1
        return cnt

    # xの属すグループの要素数
    def size(self, x):
        return -self.root[self.find(x)]
    
    # xの属すグループの要素リスト
    def members(self, x):
        ret = []
        rootNode = self.find(x)
        for i in range(len(self.par)):
            if self.find(i) == rootNode:
                ret.append(i)
        return ret
    
    # ルートノードのリストを取得
    def get_roots(self):
        ret = []
        for i,x in enumerate(self.par):
            if x==i:
                ret.append(i)
        return ret
    
    # 各グループ毎の要素リストを取得
    def all_members(self):
        L = len(self.par)
        roots = self.get_roots()
        namedict = [0]*L
        for i,r in enumerate(roots):
            namedict[r] = i
        
        
        ret = [[] for _ in range(len(roots))]
        for i in range(len(self.par)):
            p = namedict[self.find(i)]
            ret[p].append(i)
        return ret
            
    

N,M,K = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(M)]
CD = [list(map(int,input().split())) for _ in range(K)]
    
uf = UnionFind(N)
for a,b in AB:
    uf.union(a-1,b-1)
    
ans = [0]*N
 
for group in uf.all_members():
    L = len(group)-1
    for a in group:
        ans[a] = L
        
# friends = [0]*N
# brock = [0]*N
for a,b in AB:
    ans[a-1] -= 1
    ans[b-1] -= 1
 
for c,d in CD:
    if uf.same_check(c-1,d-1):
        ans[c-1] -= 1
        ans[d-1] -= 1
 
print(*ans)
        
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
import sys
import math

#区間加算，1点取得
class SegTree2:
    # n : 元の配列の長さ
    # init_list: 元の配列
    # segfunc : 載せる関数（演算）
    # ide_ele : segfuncの単位元
        
    def __init__(self, n, init_list ,segfunc, ide_ele):
        #　num : 2**num >= n となる最小の整数 （葉の数）
        # seg : segtreeのリスト
        self.num = 2**((n-1).bit_length())
        self.seg = [ide_ele]*(2*self.num)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        # 葉の要素をセット
        for i in range(n):
            self.seg[i+self.num-1] = init_list[i]        
        # segtreeの構築
        for i in range(self.num-2, -1, -1):
            self.seg[i] = segfunc(self.seg[2*i+1],self.seg[2*i+2])
        
        #memo: 要素iの子ノードは要素2*i+1, 2*i+2
        #    : 要素iの親ノードは要素(i-1)//2
        
    # 更新[l,r)にxを加算
    def update(self,l,r,x):
        if r<=l:
            return self.ide_ele
        l += self.num-1 #葉のノードのインデックス
        r += self.num-2 #半開区間から閉区間へ
         
        while r-l>1:
            if l&1 == 0:
                self.seg[l] = self.segfunc(self.seg[l],x)       
            if r&1 == 1:
                self.seg[r] = self.segfunc(self.seg[r],x)
                r -= 1
            # 親ノードへ遷移
            l = l//2
            r = (r-1)//2
        if r==l:
            self.seg[r] = self.segfunc(self.seg[r],x)
        else:
            self.seg[l] = self.segfunc(self.seg[l],x)
            self.seg[r] = self.segfunc(self.seg[r],x)
  
    # k番目の要素に加算されている合計値を計算
    def query(self,k):    
        k += self.num-1 #葉のノードのインデックス
        ret = self.seg[k]
        #末端から頂点まで更新
        while k:
            k = (k-1)//2
            ret = self.segfunc(ret, self.seg[k])
        return ret
    
            
def segfunc(x,y):
    return x|y



N,D,A = map(int,input().split())
XH = [list(map(int,input().split())) for _ in range(N)]
XH.sort()

#%%
ans = 0
damage = 0
seg = SegTree2(N,[0]*N,lambda x,y:x+y,0)

right = 1
for i in range(N):
    d = XH[i][1] - seg.query(i)
    if d<=0:
        continue
    else:
        c = math.ceil(d/A)
        ans += c
        
        while right<N and XH[right][0]<=XH[i][0]+2*D :
            right += 1
        
        seg.update(i,right,c*A)

print(ans)
            
        
        

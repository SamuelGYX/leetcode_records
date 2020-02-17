'''
765. Couples Holding Hands
Hard

N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. 

Solution:

    1. Greedy method

        Switch as long as we should and count the answer.

        Tricky point:

            We shall also swap the value of pos list.

    2. Union-Find set

        Treat each couple as a node. One mismatch connects the concerned two couples, resulting a disjoint set with circles in each group. Each mismatch does not necessarily combine two separate groups, but each swap must split a group into two. Therefore, the number of swaps is equal to the largest number of groups (N) minus the current number of groups.

'''

class Solution1:
    def minSwapsCouples(self, row: List[int]) -> int:
        n, ans = len(row), 0
        pos = [None] * n
        par = lambda i: i-1 if i%2 else i+1
        for i, v in enumerate(row):
            pos[v] = i
        for i in range(0, n, 2):
            while row[i+1] != par(row[i]):
                cur, exp = row[i+1], par(row[i])
                row[pos[cur]], row[pos[exp]] = row[pos[exp]], row[pos[cur]]
                pos[cur], pos[exp] = pos[exp], pos[cur]
                ans += 1
        return ans

class Solution2:
    def minSwapsCouples(self, row: List[int]) -> int:
        class uf_set():
            def __init__(self, n):
                self.N = n
                self.lead = [-1 for i in range(n)]
            def find(self, i):
                if self.lead[i] < 0:
                    return i
                else:
                    self.lead[i] = self.find(self.lead[i])
                    return self.lead[i]
            def unionLead(self, i, j):
                if self.lead[i] > self.lead[j]:
                    i, j = j, i
                self.lead[i] += self.lead[j]
                self.lead[j] = i
                self.N -= 1
            def union(self, i, j):
                a, b = self.find(i), self.find(j)
                if a != b:
                    self.unionLead(a, b)
        n = len(row)
        uf = uf_set(n//2)
        for i in range(0, n, 2):
            uf.union(row[i]//2, row[i+1]//2)
        return n//2 - uf.N
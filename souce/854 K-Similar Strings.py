'''
854. K-Similar Strings
Hard

Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Solution:

    Each string A could have multiple possible swaps in order to approach B. We could adopt BFS to compute the minimum number of swaps (minimum depth).

    For example:
    A = aabbccde
    B = dcacbeba

    0                   aabbccde
    1                   dabbccae
    2       dcbbacae                dcbbcaae
    3       dcabbcae                dcabcabe
    4       dcacbbae                dcacbabe
    5       dcacbeab                dcacbeba(==B)

    Tricky points:

        1. Pre-process A and B in order to eliminate the same characters.

        2. `diff` is the first character where A != B. This value is the same for each level. So we could initialize it with `diff_lvl` instead of 0.

        3. deque(): 

            We must feed the constructor an iterable object as input. But `append()` only takes an element as input.

            Initialize: Q = collections.deque([A])
            Append:     Q.append(A)

        4. For a given string A, there may be an optimal swap among all possible swaps:

                A:  __a__b__
                B:  __b__a__

            i.e. one swap, two matches. We could ignore all other possible swaps like

                A:  __a__b__
                B:  __b__c__

            But keep in mind, this swap is optimal for one given A but NOT for all nodes in the same level.

        5. shallow copy v.s. deep copy

            Rename:     temp = A        
                temp and A point to the same obj
            Shallow:    temp = list(A)  
                modifications on temp does not affect A
            Deep:       temp = copy.deepcopy(A)
                modifications on elements in temp does not affect elements in A
'''

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        A, B = [a for a, b in zip(A, B) if a != b], [b for a, b in zip(A, B) if a != b]
        if not len(A):
            return 0
        Q, depth, diff = collections.deque([A]), -1, 0
        while Q:
            depth += 1
            diff_lvl = diff
            # for one level of nodes
            for _ in range(len(Q)):
                # for each node in one level
                A, cand, diff = Q.popleft(), [], diff_lvl
                while A[diff] == B[diff]:
                    diff += 1
                for i in range(diff+1, len(A)):
                    if A[i] == B[diff]:
                        cand.append(i)
                        if A[diff] == B[i]:
                            A[diff], A[i] = A[i], A[diff]
                            if A == B:
                                return depth+1
                            Q.append(A)
                            cand = []
                            break
                for c in cand:
                    temp = list(A)
                    temp[diff], temp[c] = temp[c], temp[diff]
                    Q.append(temp)
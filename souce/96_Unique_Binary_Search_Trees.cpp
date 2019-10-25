/*
Overview:

	Given a number n, return the number of unique BST's constructed with number 1, 2, .., n.

Solution:

	A direct solution shall be recursion: Every number x in range [1, n] could be used as the root. The solution of this subset is computed by the number of combinations in the left subtree times the right subtree. This recursive thought could be represented by the following formula:

		G(i) = F(1, i) + F(2, i) + ... + F(n, i)							(1)

	where G(i) is the number of BST's and F(x, i) means the number of BST's with root = x. Then it is observed that

		F(1, i) = G(0) * G(i-1);	// left subtree * right subtree
		F(2, i) = G(1) * G(i-2);
		F(3, i) = G(2) * G(i-3);
		...
		F(x, i) = G(x-1) * G((i-1)-(x-1)) = G(x-1) * G(i-x)					(2)
		...
		F(n, i) = G(n-1) * G(i-n)

	Therefore, from (1) and (2), we get

		G(i) = G(0) * G(i-1) + G(1) * G(i-2) + ... + G(n-1) * G(i-n)		(3)

	This problem also proves that Dynamic Programming (bottom-up) is mainly an optimization over plain recursion (top-down).

Tricky point:

	The size of the result array should be n+1 instead of n because res[n] is the used for recording the result with n numbers.
*/

class Solution {
public:
    int numTrees(int n) {
        vector<int> res(n+1, 0);
        res[0] = 1;
        res[1] = 1;
        for (int i = 2; i <= n; i++)
            for (int j = 0; j < i; j++)
                res[i] += res[j] * res[i-1-j];
        return res[n];
    }
};
/*
50. Pow(x, n) Medium

Overview:

	Computer x^abs(n) (double^int) first, then take reciprocal if n<0.

	Every n is represented as a sequence of 0's and 1's in computer. If n = 1001, n = 2^3 + 2^0 = 9, then x^n = x^(2^3 + 2^0) = x^(2^3) + x^(2^0).

	Check each bit of n from LSB to MSB, if i-th bit is 1, accumulate x^(2^i) as a multiplier in the final result. 

	The corresponding multiplier of each bit is just the square of the former one (i.e. x^(2^3) = x^(2^2) * x^(2^2)). 

	Therefore, one iteration on each bit of n solved this problem.

Tricky points:

	INT_MIN again

	abs(INT_MIN) is INT_MAX + 1, i.e. we need to use labs to get the absolute value of n.
*/

class Solution {
public:
    double myPow(double x, int n) {
        long n_l = labs(n);
        double res = 1.0;
        cout << n_l << ' ' << res << endl;
        while (n_l > 0) {
            if (n_l & 1) {
                res *= x;
            }
            x *= x;
            n_l >>= 1;
        }
        cout << res << endl;
        return n >= 0 ? res : 1 / res;
    }
};
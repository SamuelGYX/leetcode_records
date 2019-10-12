/*
29. Divide Two Integers
[https://leetcode.com/problems/divide-two-integers/]
Medium
*/

/*
Overview:
    
    Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator. e.g. input: 10 3 output: 3

    quotient = 0
    for i <- the MSB to LSB (left to right):
        if dvs << i + accu_value <= dvd:
            set the i-th bit of quotient

    For example, if we want to compute 1010 / 0011 (10 / 3) and record the result in 4 bits ----
    0   + 0011 << 3 = 1,1000> 1100          quotient = 0---, temp = 0;
    0   + 0011 << 2 = 1100  > 1100          quotient = 00--, temp = 0;
    0   + 0011 << 1 = 0110  < 1010          quotient = 001-, temp = 0110;
    0110+ 0011 << 0 = 1001  < 1100          quotient = 0011, temp = 1001;
    Therefore, quotient = 0011 (3)

Tricky points:

    1. Overflow (2's complement)

        The only overflow situation is when INT_MIN / -1 results in INT_MAX + 1.

        INT_MAX:    0x7fffffff  01111111,1111....   2147483647 (2x10^9)
        INT_MIN:    0x80000000  10000000,0000....   -2147483648
        INT_MIN+1:  0xffffffff  11111111,1111....   -2147483647

        INT_MAX and INT_MIN+1 is symmetric while the special -0 value is utilized as INT_MIN. This is a special setting in C++.

        //TODO

        Therefore, we could arbitrarily negate positive or negative value except for INT_MIN because abs(INT_MIN) = abs(INT_MAX) + 1

    2. labs()

        > Returns the absolute value of parameter n ( /n/ ).
        >
        > This is the long int version of abs.

        Using abs(INT_MIN) results in overflow error (int type cannot hold -INT_MIN). But labs(INT_MIN) solves this problem by returning a long long type value. The problem statement says

        > Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range

        But this setting is only the reason for handling overflow and it is legitimate to use long long type in the program.
    
*/

#define ll long long
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1)
            return INT_MAX;
        
        int sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;
        ll dvd = labs(dividend), dvs = labs(divisor);
        ll quotient = 0, temp = 0;
        for (int i = 31; i >= 0; i--) {
            if (temp + (dvs << i) <= dvd) {
                quotient |= 1LL << i;
                temp += dvs << i;
            }
        }
        return sign * quotient;
    }
};
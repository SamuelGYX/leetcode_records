/*
Overview:

    Get 2 input string representing 2 numbers (with length < 110, i.e. extremely large numbers) and return a string representing the product of them.

Solution:

    The key point is to find out the basic principles of production.

            76
            10
         -----
            00  6*0
           00   7*0
           06   6*1
          07    7*1
         -----
          0760

    1. What is the relationship between num1.length, num2.length and product.length?

        Ans:  production.length = num1.length + num2.length 
        (But the first several bits may be take by 0's.)

    2. Every bit i (0->length-1 from left to right) from num1 and bit j from num2 has impact on 2 bits in the product (pos1 and pos2). What is the relationship between i, j and pos1, pos2?

        Ans: pos1 = i + j; pos2 = i + j + 1;

Triky points:

    1. Be careful to handle the conversion between int and char.

    2. We need to compute every bit of product from right to left because there may be carries from the right bits to left bits.

    3. Remember to trim off the first several 0's from the result before return.
*/

class Solution {
public:
    string multiply(string num1, string num2) {
        int m = num1.length(), n = num2.length();
        int sum;
        string res(m+n, '0');
        for (int i = m-1; i >= 0; i--) {
            for (int j = n-1; j >= 0; j--) {
                sum = (num1[i]-'0') * (num2[j]-'0') + (res[i+j+1]-'0');
                
                res[i+j] += sum/10;
                res[i+j+1] = sum%10 + '0';
            }
        }
        
        for (int i = 0; i < res.length(); i++) {
            if (res[i] != '0')
                return res.substr(i);
        }
        
        return "0";
    }
};
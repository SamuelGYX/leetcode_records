/*
6. ZigZag Conversion Medium

Overview:

    Re-arrange the string in a very strange way.

    Two common methods to solve this kind of problem:

        M1. Emulate the behavior of statement and output in a certain sequence.
        
        M2. Find the relationship between new index and old index. I adopted this method because M1 may be LTE in hard problems.

Tricky points:

    1. Handle numRows == 1 as special case because it resulted in a dead loop with cycle = 0.

    2. The index of next char in short rows is i+j+(numRows-1-i)*2, which is equal to j+cycle-i.
*/

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1)
            return s;
        
        int len = s.length(), cycle = numRows * 2 - 2;
        string res = "";
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j + i < len; j += cycle) {
                res += s[i+j];
                if (i > 0 && i < numRows-1 && j + cycle - i < len) {
                    res += s[j + cycle - i];
                }
            }
        }
        return res;
    }
};
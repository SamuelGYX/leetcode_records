/*
8. String to Integer (atoi) Medium

Overview:

    A simple problem. Take care of initialization of sign as well as INT_MAX situation.
*/

class Solution {
public:
    int myAtoi(string str) {
        int len = str.length();
        int sign = 1, loc = 0, cur_dig;
        long res = 0;
        while (str[loc] == ' ') {
            loc++;
        }
        if (str[loc] == '+' || str[loc] == '-') {
            sign = str[loc++] == '+' ? 1 : -1;
        }
        
        while (loc < len && str[loc] >= '0' && str[loc] <= '9') {
            cur_dig = str[loc++] - '0';
            res = res * 10 + cur_dig;
            if (res > INT_MAX) {
                if (sign > 0) 
                    return INT_MAX;
                else 
                    return INT_MIN;
            }
        }
        
        return res * sign;
    }
};
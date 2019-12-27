/*
139. Word Break Medium

Overview:

    Given a string and a dictionary, decide whether the string could be totally separated into words in the dictionary.

Solution:

    Dynamic programming:

        1. dp[i] = true means s.substr(0,i) is separable.

        Note: s.substr(0,i) means the sub-string with index 0 to i-1 (length = i)

        2. dp[i] = dp[j] && (s.substr(j,i-j) is in dictionary)

    Example:

        s = "leetcode", wordDict = ["leet", "code"]
        dp = 100010001

Tricky point:

    1. Why don't we use dp[i] to record data of sub-string with index 0 to i instead of i-1?

        Because we need a place to hold the property that "s.substr(0,0) is separable". If we adopt this notation, we should set dp[-1] = true. But this is not convenient in vector indexing.

    2. s = s.substr(0,len), thus the max index in dp[] shall be len, thus the length of dp[] shall be len+1

    3. Pay attention to the API of sort() and binary_search()
 */

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int len = s.length();
        vector<bool> dp(len+1, false);
        
        sort(wordDict.begin(), wordDict.end());
        dp[0] = true;
        
        for (int i = 1; i <= len; i++) {
            for (int j = i-1; j >= 0; j--) {
                if (dp[j]) {
                    string seg = s.substr(j, i-j);
                    if (binary_search(wordDict.begin(), wordDict.end(), seg)) {
                        dp[i] = true;
                        break;
                    }
                }
            }
        }
        
        return dp[len];
    }
};
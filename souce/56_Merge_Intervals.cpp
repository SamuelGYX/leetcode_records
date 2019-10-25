/*
Overview:

    Given a list of intervals ([a, b]), combine all overlapped ones and return.

Solution:

    Sort the list according to the start point, then keep track of the rightmost cover point in the result. Merge or push back according to the relationship between rightmost_cover and new interval.
*/

class Solution {
public:
    static bool myCompare(vector<int>& a, vector<int>& b) {
        return a[0] < b[0];
    }
    
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<int> v;
        vector<vector<int>> res;
        if (intervals.empty())
            return res;
        
        sort(intervals.begin(), intervals.end(), myCompare);
        
        res.push_back(intervals[0]);
        int rightmost_cover = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++) {
            v = intervals[i];
            if (rightmost_cover < v[0])
                res.push_back(v);
            else if (rightmost_cover < v[1])
                res[res.size()-1][1] = v[1];
            rightmost_cover = max(rightmost_cover, v[1]);
        }
        return res;
    }
};
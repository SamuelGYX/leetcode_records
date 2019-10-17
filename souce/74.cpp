/*
74. Search a 2D Matrix Medium

Overview: 

    An easy binary search problem.

Tricky points:

    Transform 1-D index into 2-D indexes.
*/


class Solution {
public:
    int m, n;
    
    void getIndex(int index, int &x, int &y) {
        x = index / n;
        y = index % n;
    }
    
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty()) {
            return false;
        }
        m = matrix.size();
        n = matrix[0].size();
        
        int low = 0, high = m*n-1, mid;
        int x, y;
        while (low <= high) {
            mid = (low+high)/2;
            getIndex(mid, x, y);
            
            if (matrix[x][y] < target) {
                low = mid + 1;
            } else if (matrix[x][y] > target) {
                high = mid - 1;
            } else {
                return true;
            }
        }
        return false;
    }
};
/*
Overview:

    Check whether the current state of a Sudoku is valid or not.

    Utilize three boolean arrays to record the state of rows, cols, and blocks.
*/

class Solution {
public:
    bool containRow[9][9] = {0}, containCol[9][9] = {0}, containBlo[9][9] = {0};
    
    bool isValidSudoku(vector<vector<char>>& board) {
        int val, block;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.')
                    continue;
                val = board[i][j] - '1';
                block = i/3 * 3 + j/3;
                if (containRow[i][val] || containCol[j][val] || containBlo[block][val])
                    return false;
                containRow[i][val] = true;
                containCol[j][val] = true;
                containBlo[block][val] = true;
            }
        }
        return true;
    }
};
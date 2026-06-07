class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int columns = grid[0].size();
        int islandCounter = 0;
        int directions[5] = {-1, 0, 1, 0, -1}; // up right down left

        function<void(int, int)> dfs = [&](int row, int column) {
            grid[row][column] = '0';
            for (int i = 0; i < 4; ++i) {
                int nextRow = row + directions[i];
                int nextColumn = column + directions[i+1];

                // checking to see if the adjacent cell is within bounds+unvisited
                if (nextRow >= 0 && nextRow < rows && nextColumn >= 0 && nextColumn < columns && grid[nextRow][nextColumn] == '1') {
                    dfs(nextRow, nextColumn); // recursive call to visit the next adjacent cell
                }
            }
        };

        // now traverse the entire grid
        for (int j = 0; j < rows; ++j) {
            for (int k = 0; k < columns; ++k) {
                //if an unvisited land cell is found, it counts as a new island
                if (grid[j][k] == '1') {
                    dfs(j, k);
                    ++islandCounter;
                }
            }
        }
        return islandCounter;
    }
};

/*
 * @lc app=leetcode id=120 lang=cpp
 *
 * [120] Triangle
 */

// @lc code=start
class Solution
{
public:
    int minimumTotal(vector<vector<int>> &triangle)
    {
        int f[triangle.size() + 1];
        f[0] = 0;
        for (auto &row : triangle)
        {
            if (row.size() > 1)
            {
                f[row.size() - 1] = f[row.size() - 2] + row[row.size() - 1];
            }
            for (int j = row.size() - 2; j >= 1; j--)
            {
                f[j] = std::min(f[j], f[j - 1]) + row[j];
            }
            f[0] = f[0] + row[0];
        }
        int min = 1 << 30;
        for (int i = 0; i < triangle.size(); i++)
        {
            if (f[i] < min)
            {
                min = f[i];
            }
        }
        return min;
    }
};
// @lc code=end

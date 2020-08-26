/*
 * @lc app=leetcode id=169 lang=cpp
 *
 * [169] Majority Element
 */

// @lc code=start
class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        int value = nums[0], cnt = 1;
        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i] != value)
            {
                if (cnt > 0)
                {
                    cnt--;
                }
                else if (cnt == 0)
                {
                    cnt++;
                    value = nums[i];
                }
            }
            else
            {
                cnt++;
            }
        }
        cnt = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == value)
                cnt++;
        }
        return value;
    }
};
// @lc code=end

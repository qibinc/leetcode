/*
 * @lc app=leetcode id=229 lang=cpp
 *
 * [229] Majority Element II
 */

// @lc code=start
class Solution
{
public:
    vector<int> majorityElement(vector<int> &nums)
    {
        int n = nums.size();
        int counter_1 = 0, counter_2 = 0, n1, n2;
        for (size_t i = 0; i < n; i++)
        {
            if (n1 == nums[i])
            {
                counter_1++;
            }
            else if (n2 == nums[i])
            {
                counter_2++;
            }
            else if (counter_1 == 0)
            {
                counter_1++;
                n1 = nums[i];
            }
            else if (counter_2 == 0)
            {
                counter_2++;
                n2 = nums[i];
            }
            else
            {
                counter_1--;
                counter_2--;
            }
        }
        counter_1 = 0;
        counter_2 = 0;
        for (size_t i = 0; i < n; i++)
        {
            if (nums[i] == n1) counter_1 ++;
            if (nums[i] == n2) counter_2 ++;
        }
        vector<int> results;
        if (counter_1 > n / 3) results.push_back(n1);
        if (counter_2 > n / 3) results.push_back(n2);
        return results;
    }
};
// @lc code=end

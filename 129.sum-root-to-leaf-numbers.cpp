/*
 * @lc app=leetcode id=129 lang=cpp
 *
 * [129] Sum Root to Leaf Numbers
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        return sumNumbersRecursive(root, 0);
    }
    int sumNumbersRecursive(TreeNode* root, int val) {
        if (root == NULL)
        {
            return 0;
        }
        val = val * 10 + root->val;
        if (root->left == NULL and root->right == NULL)
        {
            return val;
        }
        int ret = 0;
        ret += sumNumbersRecursive(root->left, val);
        ret += sumNumbersRecursive(root->right, val);
        return ret;
    }
};
// @lc code=end


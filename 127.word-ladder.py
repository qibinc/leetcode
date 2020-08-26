#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque, defaultdict
from typing import List
class Solution:
    def __init__(self):
        self.dict = defaultdict(list)
        self.comb_dict = defaultdict(list)

    def preprocess(self, wordList):
        for word in wordList:
            for i in range(len(word)):
                self.comb_dict[word].append(word[:i] + "*" + word[i + 1:])
                self.dict[word[:i] + "*" + word[i + 1:]].append(word)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        self.preprocess(wordList + [beginWord])
        q = deque()
        q.append((beginWord, 1))
        dists = {}
        while q:
            s, d = q.popleft()
            for l in self.comb_dict[s]:
                for w in self.dict[l]:
                    if w not in dists:
                        dists[w] = d + 1
                        if w == endWord:
                            return dists[w]
                        q.append((w, dists[w]))
        return 0

# @lc code=end


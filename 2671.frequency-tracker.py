#
# @lc app=leetcode id=2671 lang=python3
#
# [2671] Frequency Tracker
#

# @lc code=start

from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.number_freq = defaultdict(int)
        self.freq_count = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq_count[self.number_freq[number]] -=1
        self.number_freq[number] += 1
        self.freq_count[self.number_freq[number]] +=1

    def deleteOne(self, number: int) -> None:
        if self.number_freq[number] > 0:
            self.freq_count[self.number_freq[number]] -=1
            self.number_freq[number] -= 1
            self.freq_count[self.number_freq[number]] +=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
# @lc code=end


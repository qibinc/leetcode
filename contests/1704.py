class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def num_vowels(st):
            return len(list(filter(lambda x: x in ["a", "e", "i", "o", "u"], st.lower())))
        return num_vowels(s[:len(s) // 2]) == num_vowels(s[len(s) // 2:])

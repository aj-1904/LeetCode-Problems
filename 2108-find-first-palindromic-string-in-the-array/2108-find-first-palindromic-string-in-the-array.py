class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if self.reverse(words[i]) == words[i]:
                return words[i]
        return ""
    def reverse(self, string):
        reverseString = ""
        for i in range(len(string)):
            reverseString = string[i] + reverseString
        return reverseString
            
        
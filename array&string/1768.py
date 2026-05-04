# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        min_len = min(len(word1), len(word2))
        for ii in range(min_len):
            ans.append(word1[ii])
            ans.append(word2[ii])
        ans.extend(word1[min_len:] if len(word1) > len(word2) else word2[min_len:])
        return "".join(ans)
#Clarify: find all words that are anagrams group them into sublists, what is an easy way to create a sublist
#Examples & edge cases:["act","pots","tops","cat","stop","hat"] from left to right act doesnt have an anagram yet create new list same for pots. Tops is anagram of pots add tops to list with pots. cat is act anagram add to list. Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#Brute force: compare every word with every other word and form multiple lists of anagrams as we go
#optimize: store anagrams we have seen perform lookup as we go instead of extra loop and just find a easy way to calculate anagram
#pseudocode
#follow-ups: struggled with creating a fuctional dictionary for this problem

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)- ord("a")]+=1
            anagrams[tuple(count)].append(s)
        
        return list(anagrams.values())

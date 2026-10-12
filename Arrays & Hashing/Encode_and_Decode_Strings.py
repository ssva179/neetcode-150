#Clarify: encode a list of strings into a unique single string that can then be decoded back to original list
#Examples n edge cases: ["Hello","World"] -> Encode -> -> decode -> ["Hello","World"] 
#edge cases: finding a unique marker for decoding that wouldnt be present in a string, empty string
#looked at video -> realized having a count fixes the need for a unique marker O(n)
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j+1: j+1+length])
            i = j+1+length
        return decoded

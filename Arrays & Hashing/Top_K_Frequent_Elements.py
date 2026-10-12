#Clarify: find the k numbers that are the most frequent in the array
#order does not matter
#Examples n edge cases: [1,2,2,3,3,3], k = 2 -> 1 = 1 appearance 2=2 and 3 =3 the top two are 2 and 3 bc they have more occurances than 1 so we return 2&3
#edge cases: non unique answer, empty list
#Brute force: nested loop and compare appearance as we go 
#optimize: keep track of how many times we see each number at the end
#pick top k counts O(n)
#pseudocode:
    #for i in nums
        #count of num[i] + 1

    #for i in range k 
        #[top k]+ max count val
        #remove curr max
    #return [top k]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        topK=[]
        for i in range(k):
            topK.append(max(count, key=count.get))
            count.pop(max(count, key=count.get))
        return topK

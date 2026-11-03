#similar to sum but we can include duplicates
#we just do where we take one element and then shuffle through the other elements in array
#Optimize: we recurse to bottom and build permutations back up as we add element into permutation we add it at every positble position creating a permutation.
#O(n!) -> we look at permutations and insertion
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        permutations = self.permute(nums[1:])
        #the element we skipped we add it into every permutation
        res = []
        for perm in permutations:
            for i in range(len(perm)+1):#first is at 0
                newP = perm.copy()
                newP.insert(i, nums[0])
                res.append(newP)

        return res      


        
        

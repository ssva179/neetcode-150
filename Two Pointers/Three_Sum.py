class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        checkDupe = set()
        triplets = []
        
        for i in range(len(nums)):
            if nums[i] in checkDupe:
                continue
            else:
                checkDupe.add(nums[i])
                left = i + 1 
                right = len(nums)-1
                while left < right:
                    currSum = nums[left] + nums[right]
                    if currSum+nums[i] == 0:
                        potentialTriplet = [nums[left], nums[right],nums[i]]
                        if potentialTriplet in triplets:
                            left +=1
                        else:
                            triplets.append([nums[left], nums[right], nums[i]])
                            left+=1
                    elif currSum + nums[i] < 0:
                        left +=1
                    else:
                        right -=1
        return triplets

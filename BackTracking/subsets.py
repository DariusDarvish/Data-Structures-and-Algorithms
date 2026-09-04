class Solution:
    def __init__(self):
        pass

    def subsets(self, nums: list[int]) -> list[list[int]]:
        visited=[]
        def dfs(subset,index):
            nonlocal nums

            #base case
            if index==len(nums):
                visited.append(subset)
                return

            dfs(subset+[nums[index]],index+1)
            dfs(subset,index+1)

        dfs([],0)
        return visited


solutions = Solution()
print(solutions.subsets(nums=[1,2,3]))
class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        visited=[]
        def dfs(subset,current_count,index):
            nonlocal nums
            nonlocal target

            #base case
            if current_count==target:
                visited.append(subset)
                return

            if index>len(nums)-1:
                return
            
            if current_count>target:
                return

            
            #keep taking the same
            dfs(subset+[nums[index]],current_count+nums[index],index)
            
            #reject and go next
            dfs(subset,current_count,index+1)
        
        dfs([],0,0)
        return visited

solutions = Solution()
print(solutions.combinationSum(nums=[2,3,6,7], target=7))

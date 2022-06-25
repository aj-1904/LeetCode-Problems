class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        '''Approach:

We have to count the number of drops. One 'drop' is defined as nums[i] > nums[i + 1].

If the given array has more than 1 drop, then the answer should be false, as we can't make the array increasing by changing only one element.

Now, if the array has 1 drop only, then we have to check whether we can make it non-decreasing or not.

Suppose the drop occurs at index 'i'. [..... i i+1 .....]. It means nums[i] > nums[i + 1]. Now, we have two options i.e. either change the i'th element or change the (i+1)'th element and see if the sequence is valid or not.

If we choose to change the i'th element, then the condition that must be satisfied after changing is that, nums[i + 1] should always be greater than or equal to nums[i - 1]. If it is violated, then we can conclude that we can't change the i'th element.

If we then choose the change the (i+1)'th element, then the condition that must be satisfied after changing is that, nums[i + 2] should always be greater than or equal to nums[i]. If it is violated, then we can say that we can't change (i+1)'th element also.

Now, if we can not change any of the above elements, then we conclude that it cannot be done and thus we return false. Else return true.

You can dry-run the above idea with the testcases like [5, 7, 1, 8] and [3, 4, 2, 3] and think why the above points are valid.

Time Complexity: O(N)
space complexity: O(1)'''
        
        count = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                count += 1
                if count > 1 or (i > 0 and i < n-2 and nums[i-1] > nums[i+1] and nums[i]>nums[i+2]):
                    return False
                
        return True
        
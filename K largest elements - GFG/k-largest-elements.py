#User function Template for python3
import heapq
class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        # code here
    
        heap = li[0:k]
        heapq.heapify(heap)
        
        for i in range(k,n):
            if heap[0] < li[i]:
                heapq.heapreplace(heap, li[i])
        heap.sort(reverse=True)
        return heap
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n=li[0]
    k=li[1]
    li = [int(x) for x in input().strip().split()]
    ob=Solution()
    k_largest_list = ob.kLargest(li,n,k)
    
    for element in k_largest_list:
        print(element, end = ' ')
    print('')
# } Driver Code Ends
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        ''' 1. sort courses based on end time in ascending order
            2. Max Heap to track the max duration courses using Priority Queue.
            3. Time + duration and put duration to max heap.
            4. If pass the last day, remove the courses takes longest time.
            5. Heap size is the max courses number we take.'''
        
        max_heap = []
        time = 0
        courses.sort(key=lambda x: x[1])
        
        for duration, end in courses:
            heapq.heappush(max_heap, -duration) # push the duration in heap
            time += duration                  # sum of durations (total time taken to read)=>D
            
            if time > end:                 # check D > end 
                time += heapq.heappop(max_heap)     # removing the largest duration from heap
                
        return len(max_heap)
        
        
        
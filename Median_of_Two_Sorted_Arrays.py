class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 >= n2:
            main = nums1
            sub = nums2
        else:
            main = nums2
            sub = nums1
        place = 0
        
        while len(sub) != 0:
            popcorn = sub.pop(0)
            while place < len(main):
                if main[place] >= popcorn:
                    main = main[:place] + [popcorn] + main[place:]
                    place += 1
                    break
                place += 1
                if place == len(main):
                    main = main + [popcorn]
        
        if (n1+n2)%2 == 1:
            median = main[(n1+n2)//2]
        else:
            median = (main[(n1+n2)//2-1] + main[(n1+n2)//2])/2
        return median
       

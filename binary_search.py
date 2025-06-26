




class search:
    def __init__(self,data):
        self.data = data
    
    def binary_search(self,target):
        
        # binary search works on sorted array

        # takes time complexity of O(logN) 

        array = sorted(self.data)

        l,r = 0,len(array)-1

        while l<=r:
            mid = (l+r)//2

            if array[mid]==target:
                return True
            
            elif array[mid]>target:
                # midvalue is greater than the targeted value
                # so targeted values must be lying left of midvalue
                # so move r to mid
                r = mid-1

            elif array[mid]<target:
                # midvalue is lesser than the targeted value
                # so targeted values must be lying right of midvalue
                # so move l to mid
                l = mid+1

        return False
    




x = [9,1,7,8,2,6,4,5,3]

values = search(x)

print(values.binary_search(20))

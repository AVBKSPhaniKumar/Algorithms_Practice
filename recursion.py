class recursion:
    def __init__(self,data):
        self.data = data

    def SumofList(self):

        #base case 
        if len(self.data)==0:
            return 0
        
        else:
            return self.data[0]+recursion(self.data[1:]).SumofList()
        

    def ElementCountofList(self):

        #base case:
        if self.data==[]:
            return 0
        else:
            return 1+recursion(self.data[1:]).ElementCountofList()
        
    def FindMaximum(self,max=-10E10):
        
        #base case

        if self.data==[]:
            return None
        
        elif len(self.data)==1:
            return self.data[0]
        
        else:
            maximum = self.data[0] if self.data[0]>max else max
            return recursion(self.data[1:]).FindMaximum(maximum)

             

    def BinarySearch(self,target):

        l = 0
        r = len(self.data)

        if l<r:
            mid = (l+r)//2 

            if self.data[mid]==target:
                return "Found"
            
            elif target<self.data[mid]:
                return recursion(self.data[:mid]).BinarySearch(target)
            
            elif target>self.data[mid]:
                return recursion(self.data[mid+1:]).BinarySearch(target)

            else:
                return "Not Found"
        else:
            return "None"
        

input = [1,2,3,4]

input_data = recursion(input)

output = input_data.SumofList()
print("output >> ",output)

count = input_data.ElementCountofList()
print("count >> ",count)

maximum = input_data.FindMaximum()
print("maximum >> ", maximum)

print(input_data.BinarySearch(1))
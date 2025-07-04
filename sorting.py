

class sort:
    def __init__(self,data):
        self.data = data

    def get_minimum(self):
        min_val =  1e+10  #initiating with high value
        for i in range(len(self.data)):
            if self.data[i]<min_val:
                min_val = self.data[i]
        return min_val
    

    def selection_sort(self):
        """
        takes a complexity of O(N*N)

        takes a space complexity of O(N)
        """
        sorted_data = []
        for i in range(len(self.data)):
            min_val = self.get_minimum()
            #print("min_val >> ",min_val)
            sorted_data.append(min_val)
            self.data.remove(min_val)
        self.data = sorted_data

    def quick_sort(self):
        """
        takes complexity of O(NlogN)

        Best case scenario -> O(NlogN)

        Worst case scenario -> O(N*N)
        """

        if len(self.data)<2:
            return self.data
        
        else:
            pivot = self.data[len(self.data)//2]
            left = [i for i in self.data if i <pivot]
            right = [i for i in self.data if i >pivot]

            return sort(left).quick_sort()+[pivot]+sort(right).quick_sort()





input = [6,5,8,1,4,0]

data = sort(input)

# data.selection_sort()
# print(data.data)
sorted_Data = data.quick_sort()
print("sorted_Data >> ", sorted_Data)
 


class sort:
    def __init__(self,data):
        self.data = data

    def get_minimum(self):
        min_val =  1e+10 #self.data[0]
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





input = [6,5,8,1,4,0]

data = sort(input)

data.selection_sort()

print(data.data)

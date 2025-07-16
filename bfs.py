


#we are going to implement graphs
#to do that we use hash tables or dictionaries here

from collections import deque


class create_graph:
    def __init__(self,data):
        self.data = data



class breadthfirstsearch(create_graph):

    def person_is_seller(self,name):
        return name[-1]=="m"

    def search(self,name):
        search_queue = deque()
        search_queue+=self.data[name]
        searched = []
        while search_queue:
            person = search_queue.popleft()
            #print("searching for person ",person)
            if person not in searched:
                if self.person_is_seller(person):
                    print(person + " is a seller")
                    return True

                else:
                    search_queue+=self.data[person]
                    searched.append(person)
        print("no seller found ")
        return False



graph = {}

graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

input_data = breadthfirstsearch(graph)

input_data.search("you")




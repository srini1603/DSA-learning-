# hashtable are more likely dict in python
# the complete operation have function or mechanism called Hash function
# key({key:value}) is send to the hash function and the function returns address and dict where to store
# hash function is one way operation, and it is deterministic(gives address)
# somtime a key and value can get address of some other key and value  it is called collision
# to avoid collision linear probing is used(method of seeing for free address after the allocated address)
# O(1) time complexity
class HashTable:
    RAN_PRIME = 23  # a random prime used in HashTable
    def __init__(self,size=7): # size should be a prime so we can avoid collision
        self.size = size
        self.map_data = [None] * size


    def HashFunction(self,key):
        my_hash = 0
        for i in key:
            my_hash = (my_hash + ord(i) * self.RAN_PRIME) % len(self.map_data)
        #   my_hash = (my_hash + ASCII of i * self.RAN(bcoz global can be used only by instance ) % len(map)
        #   len(map) which is size  so that we can get a number between 0 - size
        return my_hash

    def Set_Value(self,key,value):
        index = self.HashFunction(key)
        if self.map_data[index] == None: # if the index of the table is NOne we need to create a list the we can append
            self.map_data[index] = []
        self.map_data[index].append([key, value])
        return True

    def Get_Value(self,key):
        index = self.HashFunction(key)
        if self.map_data[index] is not None:
            for i in range(len(self.map_data[index])):
                if self.map_data[index][i][0] == key:
                    return self.map_data[index][i]
        else:
            return False

    def PrintHashTable(self):
        for i ,value in enumerate(self.map_data):
            print(i,":",value)

my_hash = HashTable()
my_hash.Set_Value("hellos",100)
my_hash.Set_Value("hello",1030)
print(my_hash.Get_Value("hellos"))
my_hash.PrintHashTable()

# interview question
# return True if there is a same value present in the give listdef

def checkinboth(l1,l2):
    my_dict= {}
    for i in l1:
        my_dict[i] = True
    for j in l2:
        if j in my_dict:
            return True
    else:
        return False

l1=[1,2,3]
l2 =[5,6,4]
print(checkinboth(l1,l2))

















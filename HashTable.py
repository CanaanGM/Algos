class HashTable:
    def __init__(self, size: int = 7) -> None:
        self.data_map = [None] * size 


    def __hash(self, key):
        my_hash = 0

        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    
    def insert(self, key, value):

        hashed_key = self.__hash(key)

        if self.data_map[hashed_key] is None:
            self.data_map[hashed_key] = []
    
        self.data_map[hashed_key].append((key, value)) 
        return True
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range (len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []

        for item in self.data_map:
            if item:
                for k in item:
                    all_keys.append(k[0])
        return all_keys

    @property
    def print_table(self):
        print("-" * (len(self.data_map) * 5 +1), "--|")
        for k, v in enumerate(self.data_map):
            print(f"| {k} : {v}")
            print("-"*( len(self.data_map) * 5 +1), "--|")
            

def common_item(listA, listB):
    from collections import Counter
    # freq list
    items =Counter(listA)
    common_items = []
    for item in listB:
        if item in items.keys():
            common_items.append(item)

    return common_items


    

mh = HashTable()
mh.insert("canaan", 99)
mh.insert("canaan", 99)
mh.insert("casdasdanaan", 99)
mh.insert("canaan123", 99)
mh.print_table
print(mh.get_item("canaan"))
print(mh.keys())
print(" *** " * 40)
print(common_item([1,2,3,4,5,1], [5,6,7,8,9,0]))
print(common_item(["canaan", "dante", "maria", "mary", "canaan"], ["vergil", "nero", "alphard", "mary"]))

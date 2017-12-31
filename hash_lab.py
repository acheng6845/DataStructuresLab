from random import randint


def _hash_number_loop(hash_num):
    number = randint(0, 100)
    while number == hash_num:
        number = randint(0, 100)
    return number


class Cuckoo:
    def __init__(self):
        self._A0 = [None] * 10
        self._A1 = [None] * 10
        self._size = 0
        self._hash0 = randint(1, 100)
        self._hash1 = randint(1, 100)

    def _set_hash_number(self, number):
        if number == 0:
            self._hash0 = _hash_number_loop(self._hash0)
        elif number == 1:
            self._hash1 = _hash_number_loop(self._hash1)

    def _hash_index(self, key, num):
        if num == 0:
            return hash((key, 0, self._hash0))%len(self._A0)
        elif num == 1:
            return hash((key, 1, self._hash1))%len(self._A1)
        else:
            raise ValueError("Value Error: "+repr(num))

    def __getitem__(self, key):
        hash_index = self._hash_index(key, 0)
        if self._A0[hash_index]:
            return self._A0[hash_index][1]
        else:
            hash_index = self._hash_index(key, 1)
            if self._A1[hash_index]:
                return self._A1[hash_index][1]
            else:
                raise KeyError("Key doesn't exist")

    def __delitem__(self, key):
        hash_index = self._hash_index(key, 0)
        if self._A0[hash_index]:
            self._A0[hash_index] = None
            self._size -= 1
        else:
            hash_index = self._hash_index(key, 1)
            if self._A1[hash_index]:
                self._A1[hash_index] = None
                self._size -= 1
            else:
                raise KeyError("Key doesn't exist")

    def __len__(self):
        return self._size

    def __setitem__(self, key, value):
        if key in self:
            hash0 = self._hash_index(key, 0)
            hash1 = self._hash_index(key, 1)
            if self._A0[hash0][0] == key:
                self._A0[hash0] = (key,value)
            else:
                self._A1[hash1] = (key,value)
        else:
            self._set_item(key, value)

    def _set_item(self, key, value, okey=None):
        if key == okey:
            data = self.items().append((key, value))
            self._rebuild(2*len(self._A0), data)
        hash_index = self._hash_index(key, 0)
        if okey is None:
            okey = key
        if self._A0[hash_index]:
            prev_tuple0 = self._A0[hash_index]
            self._A0[hash_index] = (key, value)
            hash_index = self._hash_index(prev_tuple0[0], 1)
            if self._A1[hash_index]:
                prev_tuple1 = self._A1[hash_index]
                self._A1[hash_index] = prev_tuple0
                self._set_item(prev_tuple1[0], prev_tuple1[1], okey)
            else:
                self._A1[hash_index] = prev_tuple0
                self._size += 1
                if self._size > len(self._A1):
                    data = self.items()
                    self._rebuild(2*len(self._A1), data)
        else:
            self._A0[hash_index] = (key, value)
            self._size += 1
            if self._size > len(self._A0):
                data = self.items()
                self._rebuild(2*len(self._A0), data)

    def __contains__(self, key):
        hash_index = self._hash_index(key, 0)
        if self._A0[hash_index] and self._A0[hash_index][0] == key:
            return True
        else:
            hash_index = self._hash_index(key, 1)
            if self._A1[hash_index] and self._A1[hash_index][0] == key:
                return True
        return False

    def __iter__(self):
        for x in self._iter_helper():
            yield x[0]

    def _iter_helper(self):
        for b in self._A0:
            if not b is None:
                yield b
        for b in self._A1:
            if not b is None:
                yield b

    def keys(self):
        return list(iter(self))

    def values(self):
        return_list = []
        for x in self._iter_helper():
            return_list.append(x[1])
        return return_list

    def items(self):
        return list(self._iter_helper())

    def _rebuild(self, new_length, data):
        self._hash0 = randint(1, 100)
        self._hash1 = randint(1, 100)

        self._A0 = [None] * new_length
        self._A1 = [None] * new_length

        #print(data)
        for k,v in data:
            self[k] = v



# C = Cuckoo()
# print(C._hash0, C._hash1)
# print(hash(((1,1),0,C._hash0))%10)
# C._set_hash_number(0)
# C._set_hash_number(1)
# print(C._hash0, C._hash1)

T=Cuckoo()
for i in range(200):
    T[i]=i*i
for i in T.keys():
    T[i]=T[i]+1
for i in range(5,400):
    if i in T:
        del T[i]
K=T.items()
K.sort()
print(K)
print(len(K))

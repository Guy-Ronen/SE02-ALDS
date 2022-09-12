class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # Collision!

        number_collisions = 1

        # As long as the key is different than our input:
        while(current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            # If the key is None, we can assign the key and value at that index
            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            # If the key is the same, we overwrite the value at that index with the same key
            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            # If none of the previous conditions met, we increment number_collisions and try again.
            number_collisions += 1

        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        # If the first element at the index matches the input, return the second element in that array
        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1

        # While the first element in the possible return value in not the input index:
        while possible_return_value[0] != key:

            #making a new index based on the amount of collisions
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_index_array = self.compressor(new_hash_code)

            # re-assigning possible return value to the element at the new index
            possible_return_value = self.array[retrieving_index_array]

            if possible_return_value == None:
                return None

            # If the first element in the new index is the same as the input key - return the value
            if possible_return_value[0] == key:
                return possible_return_value[1]
            
            # else - increment the collisions and try again the whole thing
            retrieval_collisions += 1

        return

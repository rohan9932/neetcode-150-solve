from typing import List

class Solution:
    # Approach:
    # Time complexity: O(n)
    
    # take each string and add string's length and "#" to the encoded string, then add the actual string to the encoded string.
    
    # in the decoding part we will split the encoded string by "#" and get the actual strings.
    
    def encode(self, strs: List[str]) -> str:
        encoded_words = ""

        for s in strs:
            encoded_words += str(len(s)) + "#" + s

        return encoded_words

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_list = []
        while i < len(s):
            j = i
            while s[j] != "#": # find the end of the number
                j += 1
            length = int(s[i:j]) # num excluding # sign, used for handling double digits

            decoded_list.append(s[j+1: j+1+length]) # add the actual string to the list
            i = j+1+length # move pointer to next word
            
        return decoded_list
    
# Test cases
if  __name__ == "__main__":
    solution = Solution()
    print(solution.encode(["Hello", "World"])) # "5#Hello4#World"
    print(solution.decode("5#Hello5#World")) # ["Hello", "World"]
    print(solution.encode([""])) # "0#"
    print(solution.decode("0#")) # [""]

"""Input: An array of characters (Max 100)
Output: An array of array of characters

Option 1:
create a dictionary
For each word, sort the word alphabetically
check if that sorted word is in the dictionary
    if not:
        add the sorted word into the dictionary as a key with the original word as  
        the value
    else:
        add the original word to the list value

Use sorted() (Onlogn) to sort the characters in a word

Option 2:
Instead of sorting, keep track of word frequency
example:
for the word "act"
act_dictionary = {('a' : 1), ('c' : 1) ('t' : 1)}
whole_dict = {(act_dictionary : ["act"])}

create a main_dict (this wholes a dict as a key and a list[str] as the value)
for each string in the list, make a frequency dictionary
check if the freq dict is in main_dict
    if true:
        add the original word to the value of the key
    else:
        add the freq_dict as a key to the main_dict with a list with the original 
        word as the value
when the loop is done, return all values in the dictionary as a list
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_dict = {}
        return_list = []
        for word in strs:
            freq_dict = {}
            for letter in word:
                if letter in freq_dict:
                    freq_dict[letter] = freq_dict[letter] + 1
                else:
                    freq_dict[letter] = 1
            key_rep = frozenset(freq_dict.items())
            if key_rep in main_dict:
                main_dict[key_rep].append(word)
            else:
                main_dict[key_rep] = [word]
        for value in main_dict.values():
            return_list.append(value)
        return return_list
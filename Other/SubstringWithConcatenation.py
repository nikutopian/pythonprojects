__author__ = 'user'
import string

char_index = dict([(v,i) for i,v in enumerate(string.ascii_lowercase)])

def get_char_index(c):
    return char_index[c]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isleaf = True
        self.index = -1

    def insert(self, word, index):
        if len(word) == 0:
            self.index = index
            return
        c_index = get_char_index(word[0])
        if c_index not in self.children:
            self.children[c_index] = TrieNode()
        self.children[c_index].insert(word[1:], index)
        self.isleaf = False

    
    def get_index(self, word):
        if len(word) == 0 and self.isleaf:
            return self.index
        c_index = get_char_index(word[0])
        if c_index not in self.children:
            return -1
        return self.children[c_index].get_index(word[1:])

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word, word_index):
        self.head.insert(word, word_index)

    def get_index(self, word):
        return self.head.get_index(word)

class Solution(object):
    def findSubstring(self, s, words):
        trie = Trie()
        word_index = 0
        for word in words:
            trie.insert(word, word_index)
            word_index += 1

        word_length = len(words[0])
        num_of_words = len(words)

        matched_indices = []

        for j in range(0,len(s) - word_length):
            visited_words = set()
            for i in range(j,len(s) - word_length,word_length):
                sub_word = s[i:i+word_length]
                sub_word_index = trie.get_index(sub_word)
                if sub_word_index != -1 and sub_word_index not in visited_words:
                    visited_words.add(sub_word_index)
                else:
                    break
                if len(visited_words) == num_of_words:
                    matched_indices.append(j)
                    break

        return matched_indices


    
a =Solution()
print(a.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
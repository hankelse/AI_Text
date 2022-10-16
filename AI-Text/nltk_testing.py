from nltk import *
from nltk.corpus import *
from matplotlib import pyplot as plt
 
def main():
    text = "The quick brown fox jumps over a lazy dog."
#     text = "Pack my box with five dozen liquor jugs."
    
    """
    A token is a string that is a single part of some text that was broken
    up by some kind of rules.
    """
    #words = word_tokenize(text) # word_tokenize is from nltk
    words = text.split()
    print(words)
    
    """
    Stop words are commonly used word (such as “the”, “a”, “by”, “in”) that a
    search engine has been programmed to ignore, both when indexing entries for
    searching and when retrieving them as the result of a search query. 
    """
#     stops = stopwords.words("english")
#     print(stops)
    
    """
    Parts of speech are categories to which a word is assigned in accordance with
    its function in a sentence. The most common parts of speech are noun, pronoun,
    adjective, determiner, verb, adverb, preposition, conjunction, and interjection.
    
    See https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
    """
#     words_pos = pos_tag(words)
#     print(words_pos)
    
    """
    The entries in words_pos list are called "tuples", which are like lists only they
    are denoted with () instead of [], and we are not able to change their entries.
    """
#     for tup in words_pos:
#         print(tup[0], tup[1])
    
    """
    isalpha() checks if all of the letters in the word are alphabetical, upper or lower,
    and returns True or False
    """
#     for word in words:
#         print(f"word is {word} and isalpha is {word.isalpha()}")
    
    """
    This is a dictionary, a data structure that, like a list, holds data; however, a dictionary
    is more powerful in that it allows each matches between a "key" and a "value":
    """
#     scores = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4}
#     
#     for key in scores:
#         print(key, scores[key])
#         
#     for key, value in scores.items():
#         print(key, value)
#         
#     print(list(scores.keys()))
#     print(list(scores.values()))
 
main()

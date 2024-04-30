# your code goes here!
class Anagram:

  def __init__(self, word):
    self.word = word

  def match(self, array):
    return [worddd for worddd in array if sorted(self.word) == sorted(worddd)] or []
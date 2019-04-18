class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        Morse = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        temp, string = [], ''
        for i in words:
            for j in i:
                string += Morse[j]
            temp.append(string)
            string = ''
        #print(temp, set(temp))
        return len(set(temp))

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        word_reached = False
        count = 0

        # Start from the end of the string and iterate backwards
        for i in range(len(s) - 1, -1, -1):
            # If we've already gotten to the word and now encounter a space
            # It means we've surpassed the last word so can exit the loop
            if word_reached and s[i] == ' ':
                break
            # If we've gotten to the word and haven't encountered a space
            # as the current character, it is a letter and the length of
            # the word can be incremented
            elif word_reached:
                count += 1
            # If word hasn't been reached yet because we've only yet encountered
            # spaces, and are now encountering a non-space, we know we have 
            # started reading the last word, and that this is the first 
            # (or rather last) character of it
            elif not s[i] == ' ':
                word_reached = True
                count += 1

        return count


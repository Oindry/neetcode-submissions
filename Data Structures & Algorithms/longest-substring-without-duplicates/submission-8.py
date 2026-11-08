class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newS = []
        count = []
        i = 0

        for c in s:
            if c in newS:
                # Store the length of the current substring
                count.append(len(newS))
                # Find the index of the duplicate character
                index = newS.index(c)
                # Start a new substring after the duplicate character
                newS = newS[index + 1:]

            # Add the current character to the new substring
            newS.append(c)

        # Append the length of the last substring
        count.append(len(newS))

        return max(count)

class BaseSolution:
    def reverseWords(self, text):
        pass

class Solution(BaseSolution):
    # @param A : string
    # @return string
    @classmethod
    def reverseWords(cls, text):
        words = [word for word in text.split() if word]
        words = words[::-1]
        return " ".join(words)

if __name__ == '__main__':
    text = "the sky is blue"
    revtext = Solution.reverseWords(text)
    print(revtext)

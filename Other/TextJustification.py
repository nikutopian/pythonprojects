__author__ = 'user'

class Solution(object):

    def justifyLine(self, words, maxWidth, islastline=False):
        if islastline:
            output_line = " ".join(words)
            output_line += ' ' * (maxWidth - len(output_line))
        else:
            number_of_words = len(words)
            number_of_gaps = number_of_words - 1 if number_of_words > 1 else 1
            word_length = sum([len(x) for x in words])
            output_line = ''
            number_of_spaces = ((maxWidth - word_length) // (number_of_gaps))
            number_of_additional_spaces = ((maxWidth - word_length) % (number_of_gaps))
            index = 0
            for word in words:
                output_line += word
                if index < number_of_gaps:
                    output_line += ' ' * number_of_spaces
                if index < number_of_additional_spaces:
                    output_line += ' '
                index += 1

        return output_line
            

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        output = []
        number_of_words = len(words)

        index = 0

        while(index < number_of_words):
            current_words = []
            current_width = 0

            while (index < number_of_words and current_width + len(words[index]) <= maxWidth):
                current_width += len(words[index]) + 1
                current_words.append(words[index])
                index += 1

            output.append(self.justifyLine(current_words, maxWidth, (index > number_of_words - 1)))

        return output

a = Solution()
outp = a.fullJustify(["a","b","c","d","e"], 3)
print(outp)
outp = a.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 17)
print(outp)


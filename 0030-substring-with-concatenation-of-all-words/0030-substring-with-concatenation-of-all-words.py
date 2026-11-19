class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        result = []

        word_count = {}
        for w in words:
            if w in word_count:
                word_count[w] += 1
            else:
                word_count[w] = 1

        # word_len starts nunchi check chey - 0, 1, 2...
        # Endukante words anni word_len size lo ne cut avthayi
        for start in range(word_len):
            left = start
            seen = {}
            count = 0

            # word_len jump chesthu vellu
            for right in range(start, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]

                # Ee word words lo lekapothe window ni reset chey
                if word not in word_count:
                    seen = {}
                    count = 0
                    left = right + word_len
                    continue

                if word in seen:
                    seen[word] += 1
                else:
                    seen[word] = 1
                count += 1

                # Oka word ekkuva sarlu vachithe left nunchi thagginchu
                while seen[word] > word_count[word]:
                    left_word = s[left : left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

                # Anni words sarigga dorikithe
                if count == total_words:
                    result.append(left)
                    # Next window kosam left ni okka word munduku jaru
                    left_word = s[left : left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

        return result
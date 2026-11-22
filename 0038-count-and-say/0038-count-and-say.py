class Solution:
    def countAndSay(self, n):
        # Start - 1st term eppudu "1"
        result = "1"

        # 2nd nunchi n varaku build chey
        for _ in range(n - 1):
            next_result = ""
            count = 1

            # result lo prathi char ni chudu
            for i in range(1, len(result) + 1):
                # Inka ade char vasthunda? Leka group aipoyinda?
                if i < len(result) and result[i] == result[i - 1]:
                    count += 1
                else:
                    # Group aipoyindi - "count + char" ni add chey
                    # Ex: "11" ante "2 ones" -> "21"
                    next_result = next_result + str(count) + result[i - 1]
                    count = 1

            result = next_result

        return result

# from typing import List


# class Solution:
#     def removeComments(self, source: List[str]) -> List[str]:
#         status_inline = 0
#         status_block = 0
#         status_newline = 0
#         ans = []
#         for i, line in enumerate(source):
#             line = list(line)
#             dis = len(line)
#             flag = 0
#             temp = []
#             while flag < dis:
#                 if line[flag] == '/':
#                     if line[flag + 1] == '/':
#                         status_inline = 1
#                         flag += 1
#                         status_newline = 1
#                     if line[flag + 1] == '*':
#                         status_block = 1
#                         flag += 1
#                 if line[flag] == '*':
#                     if line[flag + 1] == '/':
#                         status_block = 0
#                         flag += 2
#                 if status_inline == 1:
#                     status_inline = 0
#                     break
#                 elif status_block == 1:
#                     pass
#                 else:
#                     if flag < dis:
#                         temp.append(line[flag])
#                 flag += 1
#             if len(temp) != 0:
#                 clean_str = ''.join(temp)
#                 ans.append(clean_str)

#         return ans


# sol = Solution()

# print(sol.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;",
#                           "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dis_x = [0, 1, 0, -1]
        dis_y = [1, 0, -1, 0]
        number = n * n
        ans = [[0 for x in range(n)] for y in range(n)]
        ans[0][0] = 1
        counter = 2
        x_pos = 0
        y_pos = 0
        head = 0
        k = n - 1
        while counter <= number:
            x = 0
            while x < k:
                x_pos += dis_x[head]
                y_pos += dis_y[head]
                ans[x_pos][y_pos] = counter
                counter += 1
                x += 1
            head = (head + 1) % 4
            if head == 3:
                k -= 1

        return ans


sol = Solution()

print(sol.generateMatrix(4))

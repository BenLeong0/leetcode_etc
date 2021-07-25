from collections import defaultdict
from typing import List

class Solution:
    code_passed = defaultdict(int)
    guess_passed = defaultdict(int)

    def check_guess(self, code: List[str], guess: List[str]) -> List[int]:
        self.code_passed.clear()
        self.guess_passed.clear()
        score = [0,0]
        for code_el, guess_el in zip(code, guess):
            if code_el == guess_el:
                score[0] += 1
            else:
                if self.guess_passed[code_el] != 0:
                    self.guess_passed[code_el] -= 1
                    score[1] += 1
                else:
                    self.code_passed[code_el] += 1

                if self.code_passed[guess_el] != 0:
                    self.code_passed[guess_el] -= 1
                    score[1] += 1
                else:
                    self.guess_passed[guess_el] += 1
        return score


sol = Solution()
x = sol.check_guess(['r','f','b','b'], ['r','p','g','b'])
print(x)

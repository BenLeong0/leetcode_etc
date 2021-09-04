from collections import defaultdict
from typing import List
from random import randint
from timeit import timeit

class Solution:
    code_passed = defaultdict(int)
    guess_passed = defaultdict(int)

    def gen_random_set(self, n) -> List[int]:
        return [randint(0, n) for _ in range(4)]

    def gen_code_guess_pair(self, n=4):
        return self.gen_random_set(n), self.gen_random_set(n)

    def check_guess(self, code: List, guess: List) -> List[int]:
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
        # print(code, guess, score, sep=" | ")
        return score

    def check_guess_loop(self, n=10000):
        for _ in range(n):
            self.check_guess(*self.gen_code_guess_pair())


    def check_guess_alex(self, code, guess):
        # print(code, guess, sep=" | ")
        score = [0,0]
        for i in range(4):
            if code[i] == guess[i]:
                score[0] += 1
                code[i] = guess[i] = False
        for i in range(4):
            for j in range(4):
                if code[i] == guess[j]:
                    score[1] += 1
                    code[i] = guess[i] = False
                    break
        # print(score)
        return score

    def check_guess_alex_loop(self, n=10000):
        for _ in range(n):
            self.check_guess_alex(*self.gen_code_guess_pair())




sol = Solution()

print(timeit(sol.check_guess_loop))
print(timeit(sol.check_guess_alex_loop))

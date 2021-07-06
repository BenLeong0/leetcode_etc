class Solution:
    def __init__(self):
        self.pre_e = True

    def isNumber(self, s):
        if not s or s in "+-":
            return False

        can_be_decimal = self.pre_e

        digits = {str(i) for i in range(10)}
        has_digit = False
        if s[0] in "+-":
            s = s[1:]
        if s[0] in "eE":
            return False

        for (i, char) in enumerate(s):
            if char in digits:
                has_digit = True
            elif char == "." and can_be_decimal:
                can_be_decimal = False
            elif char in "eE":
                if not has_digit or not self.pre_e:
                    return False
                self.pre_e = False
                return self.isNumber(s[i + 1 :])
            else:
                return False
        return has_digit


sol = Solution()

for s in [
    "2",
    "0089",
    "-0.1",
    "+3.14",
    "4.",
    "-.9",
    "2e10",
    "-90E3",
    "3e+7",
    "+6e-1",
    "53.5e93",
    "-123.456e789",
]:
    print(sol.isNumber(s))
    sol.pre_e = True


# def isNumberOld(s):
#     # Idea: Split up s by any 'e' or 'E' - more than 2 parts => invalid
#     # Decimal = '.' with integer on one or boths sides of it
#     # Check if each part is an integer - left side can have max one '.' (decimal)
#     # Parts cannot be empty, and must contain at least one digit (has_digit)

#     def is_valid(s, can_be_decimal=True):
#         if not s:
#             return False

#         digits = {str(i) for i in range(10)}
#         has_digit = False
#         if s[0] in "+-":
#             s = s[1:]

#         for char in s:
#             if char in digits:
#                 has_digit = True
#             elif char == "." and can_be_decimal:
#                 can_be_decimal = False
#             else:
#                 return False
#         return has_digit

#     # Split by 'e' or 'E'
#     strs = s.split("e")
#     if len(strs) == 1:
#         strs = strs[0].split("E")

#     # Multiple e's or E's
#     if len(strs) > 2:
#         return False

#     # Check first section
#     if not is_valid(strs[0]):
#         return False

#     # Check second section if exists
#     if len(strs) == 2:
#         if not is_valid(strs[1], can_be_decimal=False):
#             return False

#     return True
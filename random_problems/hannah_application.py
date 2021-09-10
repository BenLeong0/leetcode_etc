import re
from typing import Callable, Dict, List, Set, Tuple


def get_duplicate_locations(directions: str) -> int:
    """
    Given input string of robot movement, return the number of locations visited more than once
    """
    filtered_directions: List[str] = [dir for dir in directions if dir in "NESW"]

    current_pos: Tuple[int] = (0,0)
    visited: Set[Tuple[int]] = {(0,0)}
    visited_twice: Set[Tuple[int]] = set()

    transformations: Dict[str, Callable[[Tuple[int]], Tuple[int]]] = {
        "N": ( lambda pos: (pos[0], pos[1]+1) ),
        "E": ( lambda pos: (pos[0]+1, pos[1]) ),
        "S": ( lambda pos: (pos[0], pos[1]-1) ),
        "W": ( lambda pos: (pos[0]-1, pos[1]) ),
    }

    for dir in filtered_directions:
        current_pos = transformations[dir](current_pos)
        if current_pos in visited:
            visited_twice.add(current_pos)
        else:
            visited.add(current_pos)

    return len(visited_twice)

assert get_duplicate_locations("NS") == 1
assert get_duplicate_locations("WEWNES") == 2
assert get_duplicate_locations("SxWxNxN") == 0
print("get_duplicate_locations passed test!")


def longest_palindrome_centres(s: str) -> str:
    """
    Given a string, return the longest palindromic substring
    """
    n = len(s)
    if n <= 1:
        return s

    def expand_around_centre(l: int, r: int, max_length: int, ans: str) -> Tuple[int, str]:
        while l>=0 and r<n and s[l]==s[r]:
            l -= 1
            r += 1
        if r - l - 1 > max_length:
            return r-l-1, s[l+1:r]
        return max_length, ans

    ans = ''
    max_length = 0
    for i in range(n-1):
        max_length, ans = expand_around_centre(i,i,max_length,ans)
        max_length, ans = expand_around_centre(i,i+1,max_length,ans)

    return ans

assert longest_palindrome_centres("bob has a racecar") == "racecar"
assert longest_palindrome_centres("bob has a racecar and a bike") == "a racecar a"
assert longest_palindrome_centres("anna arrived at noon") == "anna"
print("longest_palindrome passed tests!")


def common_words(string1: str, string2: str) -> int:
    """
    Given two strings, return the number of common words between them
    """
    def get_words(s: str) -> List[str]:
        return re.findall(r"[a-zA-Z'-]+", s)

    string1_words = set(get_words(string1))
    string2_words = set(get_words(string2))
    common_words = string1_words.intersection(string2_words)

    return len(common_words)

assert common_words("Yes, we all really like pizza", "Where can we buy pizza around here?") == 2
assert common_words("There were four people at dinner","There were seven people at dinner") == 5
print("common_words passed tests!")


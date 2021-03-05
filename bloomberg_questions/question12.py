from collections import deque

def minSteps(n):
    if n == 1:
        return 0
    queue = deque([1])
    steps = 0
    visited = {1}

    while queue:
        print(queue)
        number_to_dequeue = len(queue)
        steps += 1

        for _ in range(number_to_dequeue):
            curr = queue.popleft()
            multByTwo = 2*curr
            divByThree = curr//3

            if multByTwo == n or divByThree == n:
                return steps

            if multByTwo not in visited:
                visited.add(multByTwo)
                queue.append(multByTwo)
            if divByThree != 0 and divByThree not in visited:
                visited.add(divByThree)
                queue.append(divByThree)




print(minSteps(10))
print(minSteps(3))

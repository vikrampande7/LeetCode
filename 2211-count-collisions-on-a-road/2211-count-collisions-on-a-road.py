class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0

        for car in directions:
            if not stack or car == 'S' or car == 'L' and stack[-1] == 'L':
                stack.append(car)
                continue
            if car == 'L':
                top = stack.pop()
                if top == 'R':
                    collisions += 2
                elif top == 'S':
                    collisions += 1
                while stack and stack[-1] == 'R':
                    stack.pop()
                    collisions += 1
                stack.append('S')
            elif car == 'R':
                stack.append(car)
            elif car == 'S':
                while stack and stack[-1] == 'R':
                    stack.pop()
                    collisions += 1
                stack.append('S')
        
        return collisions
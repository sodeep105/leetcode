class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in asteroids:
            # Process current asteroid
            while stack and i < 0 and stack[-1] > 0:
                # There is a collision
                if stack[-1] < -i:  # The top of the stack explodes
                    stack.pop()
                    continue  # Continue checking the current asteroid `i`
                elif stack[-1] == -i:  # Both asteroids explode
                    stack.pop()
                    break
                else:  # Current asteroid `i` explodes
                    break
            else:
                # No collision or after handling collision, push the current asteroid
                stack.append(i)
        
        return stack

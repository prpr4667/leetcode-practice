def trap(height):
    result = 0

    for i in range(len(height)):
        left_max = max(height[: i + 1])
        right_max = max(height[i:])
        result += min(left_max, right_max) - height[i]

    return result


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))

height = [4, 2, 0, 3, 2, 5]
print(trap(height))

def trap(height):
    result = 0

    for i in range(len(height)):
        left_max = max(height[: i + 1])
        right_max = max(height[i:])
        result += min(left_max, right_max) - height[i]

    return result


def trap_DP(height):
    result = 0
    left_max = [0 for _ in range(len(height))]
    right_max = [0 for _ in range(len(height))]

    left_max[0] = height[0]
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[len(height) - 1] = height[len(height) - 1]
    for i in range(len(height) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    for i in range(0, len(height)):
        result += min(left_max[i], right_max[i]) - height[i]

    return result


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_DP(height))

height = [4, 2, 0, 3, 2, 5]
print(trap_DP(height))

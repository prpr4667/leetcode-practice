def maxArea(height):
    _max = 0
    l, r = 0, len(height) - 1

    while l < r:
        left = height[l]
        right = height[r]
        _max = max(_max, min(left, right) * (r - l))

        if left < right:
            l += 1
        else:
            r -= 1

    return _max


height = [1, 1]
print(maxArea(height))

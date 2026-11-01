def clip_grass(heights, max_height):
    for i in range(len(heights)):
        if heights[i] > max_height:
            heights[i] = max_height


def test_clip_grass():
    print('Testing clip_grass... ', end='')
    # Case 1
    heights = [1, 2, 3, 4, 5]
    clip_grass(heights, 3)
    assert [1, 2, 3, 3, 3] == heights

    # Case 2
    heights = [1, 2, 3, 3, 3]
    clip_grass(heights, 3)
    assert [1, 2, 3, 3, 3] == heights

    # Case 3
    heights = [10, 20, 200, 20, 400]
    clip_grass(heights, 25)
    assert [10, 20, 25, 20, 25] == heights
    print('OK')

if __name__ == '__main__':
    test_clip_grass()
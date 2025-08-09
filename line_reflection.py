def isReflected(points):
    point_set = set((x, y) for x, y in points)
    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)
    mirror = max_x + min_x

    for x, y in points:
        reflected_x = mirror - x
        if (reflected_x, y) not in point_set:
            return False
    return True





# print(isReflected([[1,1],[-1,1]]))    # True (симметрия по x=0)
print(isReflected([[1,2],[-3,2]]))  # False (вторая точка не зеркальна пер
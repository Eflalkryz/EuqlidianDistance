points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]   # 5 points

def euqlid_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


for i in range(len(points) - 1):
    for p in points:
        print(f"Distance between {points[i]} and {p} is {euqlid_distance(points[i], p)}")
    
def quickSort(points, s, e):
    if (e-s+1) <= 1:
        return points

    pivot_pt   = points[e]
    pivot_dist = points[e][0]**2 + points[e][1]**2
    left       = s

    for i in range(s,e):
        current_distance = points[i][0]**2 + points[i][1]**2
        if current_distance <= pivot_dist:
            tmp_left     = points[left]
            points[left] = points[i]
            points[i]    = tmp_left
            left     += 1
    
    points[e]    = points[left]
    points[left] = pivot_pt

    quickSort(points, s,      left-1)
    quickSort(points, left+1, e)

    return points

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        s = 0
        e = len(points) - 1
        return quickSort(points, s, e)[:k]






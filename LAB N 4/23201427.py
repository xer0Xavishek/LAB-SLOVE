def closest_pair(points):
    
    def getX(point):
        return point[1][0]
    

    pointWID = [(i+1, (x, y)) for i, (x, y) in enumerate(points)]
    
    sortp_X = sorted(pointWID, key=getX)
    

    def dSQ(p1, p2):

        dx = p1[1][0] - p2[1][0]
        dy = p1[1][1] - p2[1][1]

        return dx * dx + dy * dy
    
    def base(pts):

        if len(pts) == 2:

            return (pts[0][0], pts[1][0]), dSQ(pts[0], pts[1])
        
        elif len(pts) == 3:

            d1 = dSQ(pts[0], pts[1])

            d2 = dSQ(pts[0], pts[2])

            d3 = dSQ(pts[1], pts[2])

            min_dSQ = min(d1, d2, d3)

            if min_dSQ == d1:

                return (pts[0][0], pts[1][0]), d1
            
            elif min_dSQ == d2:

                return (pts[0][0], pts[2][0]), d2
            
            return (pts[1][0], pts[2][0]), d3
        
        return None, float('inf')
    


    def divNc(pts_x):

        n = len(pts_x)

        if n <= 3:

            return base(pts_x)
        
        mid = n // 2

        mid_point = pts_x[mid]
        
        left = pts_x[:mid]

        right = pts_x[mid:]
        
        left_pair, leftdSQ = divNc(left)

        right_pair, rightdSQ = divNc(right)
        
        if leftdSQ < rightdSQ:

            minp, min_dSQ = left_pair, leftdSQ
        else:

            minp, min_dSQ = right_pair, rightdSQ
        
        strip = []

        for point in pts_x:

            dx = point[1][0] - mid_point[1][0]

            if dx * dx < min_dSQ:

                strip.append(point)
        
        def getY(point):

            return point[1][1]

        sortp_y = sorted(strip, key=getY)
        
        for i in range(len(sortp_y)):

            for j in range(i+1, len(sortp_y)):

                dy = sortp_y[j][1][1] - sortp_y[i][1][1]

                if dy * dy >= min_dSQ:

                    break

                dist_sq = dSQ(sortp_y[i], sortp_y[j])

                if dist_sq < min_dSQ:

                    min_dSQ = dist_sq

                    minp = (sortp_y[i][0], sortp_y[j][0])
        
        return minp, min_dSQ
    
    pair, dist_sq = divNc(sortp_X)

    id1, id2 = sorted(pair)

    distance = dist_sq ** 0.5

    return f"{id1} {id2} {distance:.6f}"






n = int(input())


points = []


for i in range(n):

    x, y = map(int, input().split())

    points.append((x, y))


print(closest_pair(points))
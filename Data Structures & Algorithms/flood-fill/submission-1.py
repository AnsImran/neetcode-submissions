class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        self.image = image
        init_color = self.image[sr][sc]

        def matrixdfs(image, sr, sc, color, init_color, visits):
            rows, cols = len(image), len(image[0])
            if min(sr, sc) < 0 or sr==rows or sc ==cols or image[sr][sc] != init_color or (sr, sc) in visits:
                return
            if image[sr][sc] == init_color:
                image[sr][sc] = color

            visits.add((sr, sc))

            matrixdfs(image, sr+1, sc,   color, init_color, visits)
            matrixdfs(image, sr-1, sc,   color, init_color, visits)
            matrixdfs(image, sr,   sc+1, color, init_color, visits)
            matrixdfs(image, sr,   sc-1, color, init_color, visits)

            visits.remove((sr, sc))

            return
        matrixdfs(self.image, sr, sc, color, init_color, set())
        return self.image
        

        
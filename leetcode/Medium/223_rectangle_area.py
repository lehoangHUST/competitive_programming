class Solution:

    def inters(self, bbox_a, bbox_b):
            # determine the coordinates of the intersection rectangle
            x_left = max(bbox_a[0], bbox_b[0])
            y_left = max(bbox_a[1], bbox_b[1])
            x_right = min(bbox_a[2], bbox_b[2])
            y_right = min(bbox_a[3], bbox_b[3])
            if x_right > x_left and y_right > y_left:
                return (x_right - x_left) * (y_right - y_left)
            else:
                return 0

    def calculate_rectangle(self, bbox):
        return (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        bbox_a = [ax1, ay1, ax2, ay2]
        bbox_b = [bx1, by1, bx2, by2]

        area_inter = self.inters(bbox_a, bbox_b)
        return self.calculate_rectangle(bbox_a) + self.calculate_rectangle(bbox_b) - area_inter
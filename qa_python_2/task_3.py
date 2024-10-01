class PointsForPlace:
    def __init__(self, place=0):
        self.place = place

    def get_points_for_place(self):
        if self.place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif self.place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 101 - self.place
            return points



class PointsForMeters:
    def __init__(self, meters=0):
        self.meters = meters

    def get_points_for_meters(self):
        if self.meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = self.meters * 0.5
            return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self):

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
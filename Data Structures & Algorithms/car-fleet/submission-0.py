class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        fleets = 0
        curtime = 0

        for dist, speed in sorted(cars, reverse = True):
            dest_time = (target - dist) / speed
            if curtime < dest_time:
                fleets += 1
                curtime = dest_time
            
        return fleets
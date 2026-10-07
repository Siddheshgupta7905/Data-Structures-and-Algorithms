class Solution:
    def getAngle(self, s: str) -> float:
        # code here
        hour = int(s[0:2])
        minutes = int(s[3:5])
        
        
        # 1. Convert 24-hour time to 12-hour format
        hour = hour % 12

        # 2. Calculate the Angle
        angle = abs((30*hour) - (5.5*minutes))
        
        
        # 3. Return the smallest angle (cannot exceed 180 degrees)
        if angle > 180:
            angle = 360 - angle

        return angle
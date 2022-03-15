def degrees(hourse, minutes):
    if hourse == 24:
        hourse = 0
    if hourse >= 12: 
        hourse -= 12
    if minutes == 60:
        minutes = 0

    def minutes_degrees(minutes):
        one_step_min_deg = 360 / 60    
        return one_step_min_deg * minutes

    def hourse_degrees(hourse, minutes):
        one_step_hour_deg = 30 / 60
        full_hour_deg = one_step_hour_deg * hourse * 60
        return full_hour_deg + (one_step_hour_deg * minutes)

    return max(minutes_degrees(minutes), hourse_degrees(hourse, minutes)) - min(minutes_degrees(minutes), hourse_degrees(hourse, minutes))

print('Degree:', degrees(int(input('Hourse: ')), int(input('Minutes: '))))
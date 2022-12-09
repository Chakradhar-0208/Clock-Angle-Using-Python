import math
def Clock_Angle(h,m):

        if (h < 0 or m < 0 or h > 24 or m > 60):
            print('Wrong input')
         
        if (h == 12):
            h = 0
        if (m == 60):
            m =60-m
            h += 1;
        if(h>12):
                   h = h-12;
        
        h_angle = 0.5 * (h * 60 + m)
        h_angle=math.ceil(h_angle)
        m_angle = 6 * m
        angle = abs(h_angle - m_angle)   
        angle = min(360 - angle, angle)
        return angle
print("Format=HH:MM")

kl=input("Time:")
if (":" not in kl):
    print("Please enter in a valid format")
else:
    sd=kl.split(":")
    h,m=int(sd[0]),int(sd[1])
    print('Angle B/W Hour & Minutes needle: {}°'.format( Clock_Angle(h,m)))
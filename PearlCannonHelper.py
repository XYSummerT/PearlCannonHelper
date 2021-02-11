#输入珍珠坐标
#pearlx = input("请输入珍珠X坐标")
#pearlz = input("请输入珍珠z坐标")
pearlx = -155.0625
pearlz = -55.9375
float (pearlx)
float (pearlz)
#player = input("请输入玩家y坐标")
#输入终点坐标
destinationx = input("请输入终点x坐标")
destinationz = input("请输入终点z坐标")
float(destinationx)
float(destinationz)
#输入到达目标gametick
gt = input("请输入到达目标gametick")
float(gt)
#输入tnt加速度
dv = input("请输入tnt加速度")
float(dv)
#计算动量
momentumx = (float(destinationx) - float(pearlx))
momentumz = (float(destinationz) - float(pearlz))
print(momentumx)
print(momentumz)

#确定珍珠炮方向
#计算tnt数量
#比较大小
if momentumx < 0:
    momentumx = momentumx * -1
    if momentumz < 0:
        momentumz = momentumz * -1
        if momentumx > momentumz:
            #进行计算
            tntz = (momentumx-momentumz)/(2*float(dv))
            tnta = (momentumx-float(dv)*tntz)/float(dv)
            print("浅灰"+str(tnta))
            print("深灰"+str(tntz))
            momentumx = momentumx * -1
            momentumz = momentumz * -1
            print("方向east 01")
        else:
            tntz = (momentumz-momentumx)/(2*float(dv))
            tnta = (momentumz-float(dv)*tntz)/float(dv)
            print("深灰"+str(tnta))
            print("浅灰"+str(tntz))
            print("方向north 11")
            momentumx = momentumx * -1
            momentumz = momentumz * -1
    else:
        if momentumx > momentumz:
            #进行计算
            tntz = (momentumx-momentumz)/(2*float(dv))
            tnta = (momentumx-float(dv)*tntz)/float(dv)
            print("深灰"+str(tnta))
            print("浅灰"+str(tntz))
            print("方向west 01")
            momentumx = momentumx * -1
        else:
            tntz = (momentumz-momentumx)/(2*float(dv))
            tnta = (momentumz-float(dv)*tntz)/float(dv)
            print("深灰"+str(tnta))
            print("浅灰"+str(tntz))
            print("方向north 11")
            momentumx = momentumx * -1
else:
    if momentumz < 0:
        momentumz = momentumz * -1
        if momentumx > momentumz:
            #进行计算
            tntz = (momentumx-momentumz)/(2*float(dv))
            tnta = (momentumx-float(dv)*tntz)/float(dv)
            print(str(tnta))
            print(str(tntz))
            print("方向east 10")
            momentumz = momentumz * -1
        else:
            tntz = (momentumz-momentumx)/(2*float(dv))
            tnta = (momentumz-float(dv)*tntz)/float(dv)
            print("浅灰"+str(tnta))
            print("深灰"+str(tntz))
            print("方向east 11")
            momentumz = momentumz * -1
    else:
        if momentumx > momentumz:
            #进行计算
            tntz = (momentumx-momentumz)/(2*float(dv))
            tnta = (momentumx-float(dv)*tntz)/float(dv)
            print("深灰"+str(tnta))
            print("浅灰"+str(tntz))
            print("方向east 10")
        else:
            tntz = (momentumz-momentumx)/(2*float(dv))
            tnta = (momentumz-float(dv)*tntz)/float(dv)
            print("浅灰"+str(tnta))
            print("深灰"+str(tntz))
            print("方向south 00")






#计算剩下的轨迹
time = 0
while time != 9:
    destinationx = float(destinationx) + momentumx*0.99
    destinationz = float(destinationz) + momentumz*0.99
    print("x"+str(destinationx)+"z"+str(destinationz))
    time = time+1
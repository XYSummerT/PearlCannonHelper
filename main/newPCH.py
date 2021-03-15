#!/usr/bin/python 

# -*- coding: utf-8 -*-



#导入模块
import PCalculator
import Trajectory




#输入值
px = float(input("请输入珍珠坐标x"))
pz = float(input("请输入珍珠坐标z"))
dx = float(input("请输入目的地坐标x"))
dz = float(input("请输入目的地坐标z"))
dtnt = float(input("请输入tnt加速度"))
gt = float(input("请输入到达时间"))





#计算 比较
mx = dx - px
mz = dz - pz



if mx > 0:
    if mz > 0:
        tntx,tntz,mx,mz = PCalculator.pearl(mx,mz,gt,dtnt)
    else:
        mz = mz * (-1)
        tntx,tntz,mx,mz = PCalculator.pearl(mx,mz,gt,dtnt)
else:
    mx = mx*(-1)
    if mz > 0:
        tntx,tntz,mx,mz = PCalculator.pearl(mx,mz,gt,dtnt)
    else:
        mz = mz * (-1)
        tntx,tntz,mx,mz = PCalculator.pearl(mx,mz,gt,dtnt)



#输出结果
print(str(tntx)+" "+ str(tntz))



#计算弹道？


time = 0
dx = px + mx
dz = pz + mz
print(dx,dz)
while time != 10:
    mx,mz,dx,dz = Trajectory.Trajectory(mx,mz,dx,dz)
    time = time+1
    print(dx,dz)


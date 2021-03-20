#!/usr/bin/python 

# -*- coding: utf-8 -*-



#导入模块
import PCalculator
import Trajectory




#输入值
#px = float(input("请输入珍珠坐标x"))
#pz = float(input("请输入珍珠坐标z"))
#dx = float(input("请输入目的地坐标x"))
#dz = float(input("请输入目的地坐标z"))
#dtnt = float(input("请输入tnt加速度"))
#gt = float(input("请输入到达时间"))

mx = 200.0
mz = 100.0
dtnt = 0.6025
gt = 1.0
px = 0.0
pz = px





#计算 比较
#mx = dx - px
#mz = dz - pz



if mx > 0:
    if mz > 0:
        if mx - mz > 0:
            tntx,tntz = PCalculator.pearl(mx,mz,gt,dtnt)
            r = 1
            l = 1
        else:
            mx1 = mx
            mx = mz
            mz = mx1
            tntz,tntx = PCalculator.pearl(mx,mz,gt,dtnt)
            r = 1
            l = 1
    else:
        mz = mz * (-1)
        if mx - mz > 0:
            tntx,tntz = PCalculator.pearl(mx,mz,gt,dtnt)
            r = 1
            l = 1
        else:
            mx1 = mx
            mx = mz
            mz = mx1
            tntz,tntx = PCalculator.pearl(mx,mz,gt,dtnt)
            r = 1
            l = 1
else:
    mx = mx * (-1)
    if mz > 0:
        if mx - mz > 0:
            tntx,tntz = PCalculator.pearl(mx,mz,gt,dtnt)
            r = 1
            l = 1
        else:
            mx1 = mx
            mx = mz
            mz = mx1
            tntz,tntx = PCalculator.pearl(mx,mz,gt,dtnt)
            r = 1
            l = 1
    else:
        mz = mz * (-1)
        if mx - mz > 0:
            tntx,tntz = PCalculator.pearl(mx,mz,gt,dtnt)
            r = 1
            l = 1
        else:
            mx1 = mx
            mx = mz
            mz = mx1
            tntz,tntx = PCalculator.pearl(mx,mz,gt,dtnt)
            r = 1
            l = 1


#输出结果
print(str(tntx)+" "+ str(tntz))



#计算弹道？



time = 0

if tntx >= tntz:
    mx = dtnt * (tntx + tntz)
    mz = dtnt * (tntx - tntz)
    s = 1
else:
    mz = dtnt * (tntx + tntz)
    mx = dtnt * (tntz - tntx)
    s = 2


dx = px + mx
dz = pz + mz
print(dx,dz)
if s == 1:
    while time != 10:
        mx,mz,dx,dz = Trajectory.Trajectory(mx,mz,dx,dz)
        print(dx,dz)
        time = time+1
else:
    while time != 10:
        mx,mz,dx,dz = Trajectory.Trajectory(mx,mz,dx,dz)
        print(dx,dz,mx,mz)
        time = time+1




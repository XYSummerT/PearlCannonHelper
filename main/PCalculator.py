#!/usr/bin/python 

# -*- coding: utf-8 -*-




def pearl(mx,mz,gt,dtnt):
    if gt > 3:
        a = gt - 1
        rtnt = a + 0.99**(2*gt)
        mx = mx/rtnt
        mz = mz/rtnt
        print(mx,mz)
        tntx = (mx - mz)/(2*dtnt)
        tntz = (mx - dtnt*tntx)/dtnt
    else:
        if gt == 3:
            rtnt = 2.970299
            mx = mx/rtnt
            mz = mz/rtnt
            print(mx,mz)
            tntx = (mx - mz)/(2*dtnt)
            tntz = (mx - dtnt*tntx)/dtnt
        else:
            if gt == 2:
                rtnt = 1.99
                mx = mx/rtnt
                mz = mz/rtnt
                print(mx,mz)
                tntx = (mx - mz)/(2*dtnt)
                tntz = (mx - dtnt*tntx)/dtnt
            else:
                #1gt直达计算
                tntx = (mx - mz)/(2*dtnt)
                tntz = (mx - dtnt*tntx)/dtnt
    return tntx,tntz,mx,mz

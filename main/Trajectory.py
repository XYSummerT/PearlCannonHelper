def Trajectory(mx,mz,dx,dz):
    mx = mx*0.99
    mz = mz*0.99
    dx = dx + mx
    dz = dz + mz
    return mx,mz,dx,dz
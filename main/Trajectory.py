def Trajectory(mx,mz,dx,dz):
    mx = mx*0.99
    dx = dx + mx
    mz = mz*0.99
    dz = dz + mz
    return mx,mz,dx,dz

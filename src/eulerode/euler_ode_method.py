import numpy as np

# THIS PART ASSUMES 2D COUPLED EQUATIONS OF FORM:
# [dx/dt] = [ax + by] = [a, b] * [x]
# [dy/dt]   [cx + dy]   [c, d]   [y]
# So x' = Ax, where A is a 2*2 matrix.

# uses simple Euler approximation
# (x0, y0) is starting point, "h" is step size in time (t), and "N" is number of points to generate (So ending time predicted is h*N, or (time per step) * (number of steps))
def numericalMethod (A: [[float]], x0: float, y0: float, h: float, N: int):
	t = [i for i in range (0, int(N*h))]
	#pre-allocate x and y for speed (so program doesn't need to dynamically change their size later. This helps program run faster, since it knows how much memory to allocate, without re-allocating more memory later)
	x = np.empty(len(t))
	y = np.empty(len(t))
	
	Vx = np.empty(len(t))
	Vy = np.empty(len(t))
	
	x[0] = x0
	y[0] = y0
	#print ("A[0][0] == ", A[0][0], "A[0][1] == ", A[0][1], "A[1][0] == ", A[1][0], "A[1][1] == ", A[1][1])
	for i in range (1, len(t)):
		#x = xold + slope*h. x[n] = x[n-1] + (x'[n-1] * h)
		#x[i] = x[i-1] + ((A[0][0]*x[i - 1]) + (A[0][1]*y[i - 1]))*h
		#y[i] = y[i-1] + ((A[1][0]*x[i - 1]) + (A[1][1]*y[i - 1]))*h
		
		
		Vx[i-1] = (A[0][0]*x[i - 1]) + (A[0][1]*y[i - 1])
		Vy[i-1] = (A[1][0]*x[i - 1]) + (A[1][1]*y[i - 1])
		x[i] = x[i-1] + (Vx[i-1])*h
		y[i] = y[i-1] + (Vy[i-1])*h
		
		
		#print ("x[", i, "]=", x[i], ", y[", i, "]=", y[i])
	#return [t, x, y]
	return [t, x, y, Vx, Vy]
	
t, x, y, Vx, Vy = numericalMethod(3.5, 4.5, 1, 10)
speed = np.sqrt(Vx*Vx + Vy*Vy)
#!/usr/bin/python
import matplotlib.pyplot as plt	#has plotting tools
import numpy as np	#has array and matrix tools
from numpy import linalg	# has eig()

# This code assumes 2D coupled linear equations
# line thickness is proportional to speed. Color is too

#THIS CAN PLOT IN 3D!!!: http://docs.enthought.com/mayavi/mayavi/auto/example_lorenz.html#example-lorenz

#plot will plot from -xWindow to +xWindow horizontally, and from -yWindow to +yWindow vertically
# {x | -xWindow < x < +xWindow}
# {y | -yWindow < y < +yWindow}
xWindow = 3
yWindow = 3 #Bug: Currently, the plot gets messed up if plotting the eigenvectors when xWindow > yWindow, and the eigenvector goes beyond window of streamplot
plotEigenvectors = True

#input:
#in python 3.5, "raw_input()" was renamed to "input()"
str = input ("Please enter a 2*2 matrix (e.g.: 1 0 1 0): ")

#imaginary:
#str = "0 -1 1 -1"

#real:
#str = "1 2 1 0"

str_matrix = str.split()
nn_matrix = [int(str_matrix[i]) for i in range (0, len(str_matrix))]
total_cells = len(nn_matrix)	# counts how many cells are in matrix
row_cells = int(total_cells**0.5)	# square root of number of cells is number of rows
A = [nn_matrix[i:i+row_cells] for i in range (0, total_cells, row_cells)]
print("matrix is: ")
print(A)
print("\n")


#getting eigenvectors and eigenvalues:
egvals, eigvects = linalg.eig(A)
print ("Eigenvalues:\n")
print (egvals)


#reverse eigenvalues so they match the order of eigenvectors:
print ("reverse eigenvalue array so they are in order of eigenvectors:\n")
eigvalues = egvals#[::-1]	#"eigvalues" is in reverse order, but later code needs it this way to plot the eigenvector diagram
egvals = egvals[::-1]	#"egvals" is reversed, and is used to print eigenvalues. This is in the correct order
print("eigenvalues: ", egvals)

#normailize the eigenvector:

#rotate the eigenvector to make each row a vector:
#print ("rotate:\n")
#eigvects = zip(*eigvects[::-1])
#print(eigvects)

#for i in range (0, len(eigvects)):
#	for j in range (1, len(eigvects)):
#		for 
#	for j in range (0, len(eigvects)):
#		eigvects[0][j] = 1
	

print ("\nEigenvectors:\n")
print (eigvects)
'''
for vect in eigvects:
	for val in vect:
		val = val/vect[0]
'''		

#normalize eigenvectors so first item in each vector is 1 (useful for homework problems with "nice" numbers)
print ("Normalized: \n")
for j in range (0, len(eigvects)):
	
	for i in range (1, len(eigvects[j])):
		eigvects[i][j] = eigvects[i][j] /eigvects[0][j] 
	eigvects[0][j]  = 1
print (eigvects)

print ("rotated 90 degrees so each row is a vector:\n")
print (np.rot90(eigvects))

#*******************************CALCULATE THE VELOCITY: **************************
'''
# uses simple Euler approximation
# (x0, y0) is starting point, "h" is step size in time (t), and "N" is number of points to generate (So ending time predicted is h*N, or (time per step) * (number of steps))
def numericalMethod (x0, y0, h, N):
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
'''

#********************Make the Stream Plot:***************

y, x = np.mgrid[-1*yWindow:yWindow:100j, -xWindow:xWindow:100j]
Vx = (A[0][0]*x) + (A[0][1]*y)
Vy = (A[1][0]*x) + (A[1][1]*y)
speed = np.sqrt(Vx*Vx + Vy*Vy)

lw = 4*speed/speed.max()	#set line width to be proportional to speed
fig0, ax0 = plt.subplots()
strm = ax0.streamplot(x, y, Vx, Vy, color=speed, linewidth=lw, cmap=plt.cm.autumn)
cbar = fig0.colorbar(strm.lines)
cbar.set_label("Speed of movement: |V| = sqrt(Vx^2 + Vy^2)")

#fig1, (ax1, ax2) = plt.subplots(ncols=2)
#ax1.streamplot(X, Y, U, V, density=[0.5, 1])

#lw = 5*speed / speed.max()
#ax2.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)


#**********************************PLOTTING THE EIGENVECTORS (IF REAL)***************************************************************:
# - first, each eigenvector is plotted as a line
# - second, overlapping arrows are drawn over the eigenvector to show direction

#Check if the number is complex:
isComplex = False
for i in range (0, len(eigvalues)):
	if (isinstance(eigvalues[i], complex)):
		isComplex = True
		break;
if (isComplex):
	print ("Complex Eigenvalues, so can't draw eigenvectors\n")
elif(plotEigenvectors == False):
	print("EigenVector plotting is turned off\n")
else:
	#each eigenvector is a line through the origin, taking the form y = m*x. So calculate "m", "x", and "y"
	
	#calculate the slopes of the lines:
	print ("slopes:\n")
	m = [(eigvects[1][i]/eigvects[0][i]) for i in range (0, row_cells)]
	print(m)
	
	# FINDING X AND Y VALUES
	#find the x values of the eigenvector line:
	print ("x values:\n")
	#x1 = [i  for i in range (-10, 10)]
	x1 = [-xWindow, 0, xWindow]
	print(x1)

	#Find Y-values of each eigenvector line, for every eigenvector in eigvects:
	yVals = [x1 for i in range (0, row_cells)]
	print("yVals array: ", yVals)
	for i in range(0, len(eigvects)):
		y = [x1[i] for i in range(0, len(x1))] 	#[0 for i in range (0, len(x1))]	#pre-allocate y
		for j in range (0, len(x1)):
			y[j] =  m[i] * x1[j]
		print ("y values for eigenvector #", i, "are:", y)
		print ("x1 values for eigenvector #", i, "are:", x1)
		print ("\n")
		yVals[i] = y
	
	#ax = plt.axes()
	for i in range (0, len(eigvects)):
		plt.plot(x1, yVals[i])	#plot each eigenvector as a line
		#startPoint = [0, 0]
		#outerPoint = [0, 0]
		outerPoint = [x1[len(x1) - 1], yVals[i][len(y) - 1]]
		
		# draw arrow outward if eigenvalue is positive, but inward if eigenvalue is negative
		if (eigvalues[i] >= 0):
			print ("eig", i, " is: ", eigvalues[i])
			# let startpoint be (0,0) and endpoint be (x1[len(x1) - 1], y[len(y) - 1])
			plt.annotate(s='', xy=(  outerPoint[0],     outerPoint[1]),   xytext=(-1 *outerPoint[0],  -1*outerPoint[1]), arrowprops=dict(arrowstyle='<->'))
			plt.annotate(s='', xy=(2*outerPoint[0]/3, 2*outerPoint[1]/3), xytext=(-2*outerPoint[0]/3, -2*outerPoint[1]/3), arrowprops=dict(arrowstyle='<->'))
			plt.annotate(s='', xy=(  outerPoint[0]/3,   outerPoint[1]/3), xytext=(-1*outerPoint[0]/3, -1*outerPoint[1]/3), arrowprops=dict(arrowstyle='<->'))
		else:
			# let startpoint be (x1[len(x1) - 1], y[len(y) - 1]) and endpoint be (0,0)
			#startPoint = [x1[len(x1) - 1], y[len(y) - 1]]
			
			#draw 3 arrows on one side pointing to origin
			plt.annotate(s='', xy=(                0,                 0), xytext=(  outerPoint[0],     outerPoint[1]), arrowprops=dict(arrowstyle='->'))
			plt.annotate(s='', xy=(  outerPoint[0]/3,   outerPoint[1]/3), xytext=(  outerPoint[0],     outerPoint[1]), arrowprops=dict(arrowstyle='->'))
			plt.annotate(s='', xy=(2*outerPoint[0]/3, 2*outerPoint[1]/3), xytext=(  outerPoint[0],     outerPoint[1]), arrowprops=dict(arrowstyle='->'))
			
			#draw 3 arrows on other side pointing to origin
			plt.annotate(s='', xy=(                 0,                  0), xytext=(-1*outerPoint[0],   -1*outerPoint[1]), arrowprops=dict(arrowstyle='->'))
			plt.annotate(s='', xy=(-1*outerPoint[0]/3, -1*outerPoint[1]/3), xytext=(-1*outerPoint[0],   -1*outerPoint[1]), arrowprops=dict(arrowstyle='->'))
			plt.annotate(s='', xy=(-2*outerPoint[0]/3, -2*outerPoint[1]/3), xytext=(-1*outerPoint[0],   -1*outerPoint[1]), arrowprops=dict(arrowstyle='->'))
			







plt.title ("Phase portrait:")
plt.ylabel("Y(t) value")
plt.xlabel("X(t) value")
plt.show()
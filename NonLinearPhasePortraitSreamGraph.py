#!/usr/bin/python
import matplotlib.pyplot as plt	#has plotting tools
import numpy as np	#has array and matrix tools
from numpy import linalg	# has eig()

'''
Goals for this code:

1) draw phase prtrait of non-linear systems of 2D coupled differential equations
2) find the Jacobian matrix of these systems
3) be able to trace a single curve in the system using a numerical method of choice
4) plot any eigenvectors
'''

# This code assumes 2D coupled linear equations
# line thickness is proportional to speed. Color is too

#plot will plot from -xWindow to +xWindow horizontally, and from -yWindow to +yWindow vertically
# {x | -xWindow < x < +xWindow}
# {y | -yWindow < y < +yWindow}
xWindow = 3
yWindow = 3 #Bug: Currently, the plot gets messed up if plotting the eigenvectors when xWindow > yWindow, and the eigenvector goes beyond window of streamplot
plotEigenvectors = True

#input:
#in python 3.5, "raw_input()" was renamed to "input()"
print("Please enter the 2 equations of the form \nx' = x(a1x + b1y + c1)\ny' = y(a2x + b2y + c2)\n")
str = "1 0 "	#input ("Enter the 6 numbers,(ie: 1 2 3 4 5 6):\n")

str_matrix = str.split()
nn_matrix = [float(str_matrix[i]) for i in range (0, len(str_matrix))]
total_cells = len(nn_matrix)	# counts how many cells are in matrix
row_cells = 3	#int(total_cells**0.5)	# square root of number of cells is number of rows
A = [nn_matrix[i:i+row_cells] for i in range (0, total_cells, row_cells)]
print("Array is: ")
print(A)
print("\n")


#********************Find Stationary Points:***************
P1 = (0, 0)

P2 = (0, 0)
if (A[0][1] != 0):
	P2 = (-1*A[0][0]/A[0][1], 0)
else :
	P2 = None

P3 = (0, 0)
if (A[1][2] != 0):
	P3 = (0, -1*A[1][0]/A[1][2])
else:
	P3 = None

P4 = (0, 0)
if ((A[0][1]*A[1][2] - A[1][1]*A[0][2] != 0) and (A[0][1]*A[1][2] - A[1][1]*A[0][2] != 0)):
	P4 = ((A[1][0]*A[0][2] - A[0][0]*A[1][2]) / (A[0][1]*A[1][2] - A[1][1]*A[0][2]), (A[0][0]*A[1][1] - A[1][0]*A[0][1]) / (A[0][1]*A[1][2] - A[1][1]*A[0][2]));
else :
	P4 = None

stationaryPts = [P1, P2, P3, P4]

print ("Stationary Points: ", stationaryPts)

#********************Find Jacobians:***************
J = [ [[0, 0],[0, 0]] for i in range (0, len(stationaryPts))]
print ("\n\nJACOBIANS:")
for i in range (0, len(stationaryPts)):
	if stationaryPts[i] == None:
		continue
	plt.plot([stationaryPts[i][0]], [stationaryPts[i][1]], marker='o', markersize=3, color="red")
	xVal = stationaryPts[i][0]
	yVal = stationaryPts[i][1]
	J[i][0][0] = A[0][0]+ 2*A[0][1]*xVal + A[0][2]*yVal
	J[i][0][1] = A[0][2]*xVal
	J[i][1][0] = A[1][1]*yVal
	J[i][1][1] = A[1][0] + A[1][1]*xVal + 2*A[1][2]*yVal
	print ("J ", stationaryPts[i], " = ", J[i])

	#getting eigenvectors and eigenvalues:
	egvals, eigvects = linalg.eig(J[i])
	#print ("Eigenvalues:\n")
	#print (egvals)

	#reverse eigenvalues so they match the order of eigenvectors:
	#print ("reverse eigenvalue array so they are in order of eigenvectors:\n")
	eigvalues = egvals#[::-1]	#"eigvalues" is in reverse order, but later code needs it this way to plot the eigenvector diagram
	#egvals = egvals[::-1]	#"egvals" is reversed, and is used to print eigenvalues. This is in the correct order
	print("eigenvalues: ", egvals)	

	print ("\nEigenvectors:\n")
	print (eigvects)

	#normalize eigenvectors so first item in each vector is 1 (useful for homework problems with "nice" numbers)
	
	for j in range (0, len(eigvects)):	# for each eigenvector
		#if ((eigvects[0][j] == 0) and (eigvects[1][j] == 0)):
			#do nothing
		if   ((eigvects[0][j] == 0) and (eigvects[1][j] != 0)):
			eigvects[1][j] = 1
		elif ((eigvects[0][j] != 0) and (eigvects[1][j] == 0)):
			eigvects[0][j] = 1
		elif ((eigvects[0][j] != 0) and (eigvects[1][j] != 0)):	#neither component is 0
			for i in range (1, len(eigvects[j])):
				eigvects[i][j] = eigvects[i][j] /eigvects[0][j] 
			eigvects[0][j]  = 1
	print ("Normalized:\n", eigvects)

	#print ("rotated 90 degrees so each row is a vector:\n")
	#print (np.rot90(eigvects))
	print ("\n\n\n")
	



	
	
	
	
	
	
	
#********************Make the Stream Plot:***************

y, x = np.mgrid[-1*yWindow:yWindow:100j, -xWindow:xWindow:100j]
Vx = x * (A[0][0] + (A[0][1]*x) + (A[0][2]*y))	#(A[0][0]*x) + (A[0][1]*y)
Vy = y * (A[1][0] + (A[1][1]*x) + (A[1][2]*y))	#(A[1][0]*x) + (A[1][1]*y)

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



#********************Show the Plot:***************
plt.title ("Phase portrait:")
plt.ylabel("Y(t) value")
plt.xlabel("X(t) value")
plt.show()

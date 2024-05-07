# Differential-Equation-Plotting

# TODO
Goals for this code:

1) Done: draw phase prtrait of non-linear systems of 2D coupled differential equations
2) Done: find the Jacobian matrix of these systems
3) Done: be able to trace a single curve in the system using a numerical method of choice
4) Done: plot any eigenvectors

TODO: Write documentation
TODO: Add requirements.txt
TODO: Publish GitHub package
TODO: Organize, productionalize all plotting code into a single, well documented function, and remove uneccessary code.
TODO: Use [Google Python Fire](https://github.com/google/python-fire) to make the Python function into an organized, production ready CLI function.
TODO: Try to follow [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

## How to use this code

```python
def plot(plot_eigenvectors = True)

plot(blaah=foo, ...)

```
#### Documentation
* matrix (required): A 2 by 2 matrix for the phase portrait stream plot.
* plot_eigenvectors (optional, default true): If any eigenvalue is complex, this option does nothing. If all eigenvalues are real (none are complex) then plots arrows indicating the direction of the eigenvectors.
* 


Result:
<div align="center">
<img src = "ResultImages/RealEigenValues.png" width="50%"/>
</div>


# Credits

This code was inspired by the Fall 2017 Math 125 Ordinary Differential Equations class at UC Merced. Special thanks to Professor Shilpa Khatri, as well as Ms. Shayna Bennett and Ms. Matea Alvarado, for teaching the class.

Much of the code was also inspired by the MATLAB code of the author of the textbook. The code can be found at:
http://www.cambridge.org/us/academic/subjects/mathematics/differential-and-integral-equations-dynamical-systems-and-co/introduction-ordinary-differential-equations?format=PB&isbn=9780521533911#i6bXGsqpr95zt3FP.97


Here is a link to the textbook:
http://www.cambridge.org/0521533910

More differential equation software:
http://math.rice.edu/~dfield/index.html

# Resources used:
* Python:	https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python
* Matplotlib:
	* https://matplotlib.org/users/pyplot_tutorial.html
	* https://matplotlib.org/examples/images_contours_and_fields/streamplot_demo_features.html
	* https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.streamplot.html
* numpy:
	* https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.mgrid.html
	* http://docs.enthought.com/mayavi/mayavi/auto/example_lorenz.html#example-lorenz
* stackoverflow:	https://stackoverflow.com/questions/15908371/matplotlib-colorbars-and-its-text-labels

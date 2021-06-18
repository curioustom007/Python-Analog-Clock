# Python-Analog-Clock
An interesting version of analog clock created using some simple python GUI programming and a bit of geometry.
* **Prerequisites:**
  - Python3
  - Pyglet - 1.5.16
* **How to run:**
``` python AnalogClock.py ```
* **Mathematics behind:**
  - Formulas to calculate points on the circumference.
     - <img src="https://latex.codecogs.com/svg.latex?&space;(X,Y)=(\cos(\frac{2\pi}{nx})r&space;&comma;&space;\sin(\frac{2\pi}{nx})r)" />
   - where, 
     - r = radius of circle
     - n = number of points expected
     - 0 <= x >= n

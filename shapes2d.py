import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def main():
  # Create a new figure --- a window where plots can go.  Note that we don't
  # actually get to *see* the figure yet; we put everything in the figure first,
  # and then show it at the end of the program.
  fig = plt.figure()

  # Add a set of axes on which you can plot things.
  ax = fig.add_subplot(1, 1, 1, aspect='equal')
  ax.set_xlim(-5, 5)
  ax.set_ylim(-5, 5)
  ax.grid(True)

  # The function says to "draw" on the plane, but we won't see it until we show
  # the figure at the end.
  drawPolyline(polylineXAxis(4) + np.reshape([2.5, 2.5], (2, 1)), ax)
  drawPolyline(polylineVee(4) + np.reshape([-2.5, 2.5], (2, 1)), ax)
  drawPolygon(polygonSquare(3) + np.reshape([-2.5, -2.5], (2, 1)), ax)
  drawPolygon(polygonCircle(10) + np.reshape([2.5, -2.5], (2, 1)), ax)

  # Show figures.
  plt.show()

def polylineXAxis(K):
  """Returns a 2x(K+2) array representing points in the plane, along the X
axis, from (-1,0) to (1,0), with K extra points equally spaced in the middle.
  """
  xValues = np.linspace(-1, 1, K+2)
  yValues = np.zeros(K+2)
  points = np.concatenate(([xValues], [yValues]), 0)
  return points

def polylineVee(K):
  """Returns a 2x(2K+3) array representing points in the plane in a V shape,
with K points equally spaced in the middle of each leg.  The V fits inside the
"unit square", centered on the origin.
  """
  xValues = np.linspace(-1, 1, 2*K + 3)
  leftY = np.linspace(1, -1, K+1, False)
  rightY = np.linspace(-1, 1, K+2)
  yValues = np.concatenate((leftY, rightY), 0)
  points = np.concatenate(([xValues], [yValues]), 0)
  return points

def polygonSquare(K):
  """Returns a 2x(4K+4) array representing points in the plane in a square, with
K points equally space in the middle of each side.  This is the "unit square",
centered on the origin with side length 2.
  """
  # X-coordinate values counter-clockwise around square.
  topX = np.linspace(1, -1, K+1, False)
  leftX = np.repeat([-1], K+1, 0)
  bottomX = np.linspace(-1, 1, K+1, False)
  rightX = np.repeat([1], K+1, 0)

  # Y-coordinate values counter-clockwise around square.
  topY = np.repeat([1], K+1, 0)
  leftY = np.linspace(1, -1, K+1, False)
  bottomY = np.repeat([-1], K+1, 0)
  rightY = np.linspace(-1, 1, K+1, False)

  xValues = np.concatenate((topX, leftX, bottomX, rightX), 0)
  yValues = np.concatenate((topY, leftY, bottomY, rightY), 0)
  points = np.concatenate(([xValues], [yValues]), 0)
  return points

def polygonCircle(K):
  """Returns a 2x(K+3) array representing points in the plane equally
distributed around the unit circle.
  """
  # Finds equally distributed angles from 0 to 2pi
  maxAngle = 2*np.pi
  angles = np.linspace(0, maxAngle, K+3, False)

  # Finds respective points according to angle
  xValues = np.cos(angles)
  yValues = np.sin(angles)
  points = np.concatenate(([xValues], [yValues]), 0)
  return points

# ---- You don't need to change or add anything below this line. ----

def drawPolyline(points, ax, linespec=None):
  """Given a 2xN array (or matrix) representing N points in the plane, plot all
the points as dots, connected by straight line segments.  ax is the pyplot axes
on which to plot.
  Optional argument "linespec" may be any Matplotlib line format string.  See
    http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
  """
  if linespec is None:
    linespec = color_cycle.next() + 'o-'
  ax.plot(points[0,:].T, points[1,:].T, linespec)

def drawPolygon(points, ax, linespec=None):
  """Given a 2xN array (or matrix) representing N points in the plane, plot all
the points as dots, connected by straight line segments, with a final segment
going back to the first dot.  ax is the pyplot axes on which to plot.
  Optional argument "linespec" may be any Matplotlib line format string.  See
    http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
  """
  if linespec is None:
    linespec = color_cycle.next() + 'o-'
  ax.plot(np.concatenate((points[0,:], [points[0,0]]), 1).T,
          np.concatenate((points[1,:], [points[1,0]]), 1).T, linespec)

# -- Begin gross hack for storing global state about colors of plotted lines --
def makeColorCycleGenerator():
  colors = 'bgrcmyk'
  next_color = 0
  while(True):
    color = colors[next_color]
    next_color = (next_color + 1) % len(colors)
    yield color

color_cycle = makeColorCycleGenerator()
# -- End gross hack --


# This calls main() when the program is invoked from the command line.
if __name__ == "__main__":
  main()

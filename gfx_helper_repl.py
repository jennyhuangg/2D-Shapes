# gfx_helper_repl.py --- setup script for interactive experimentation with
# Matplotlib in the Python interactive interpreter.
#   By Jadrian Miles, December 2015
# 
# To use, start a Python REPL session, and then:
# >>> from gfx_helper_repl import *
# This will execute all the following commands in the namespace of your
# interactive session.

import numpy as np
import matplotlib
# Set the Matplotlib backend to Tk, to prevent hangs.
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# Turn on interactive mode.  DON'T DO THIS IN YOUR SCRIPTS!
plt.ion()

# Now you can plot interactively.

# Below you will find annotated examples of a simple plotting task, performed
# in three different styles.  The first two styles are for interactive
# experimentation, using this setup script.  They differ in how much work you
# need to do to convert them to non-interactive plotting commands.  The third
# example shows the equivalent non-interactive approach, which would be the
# way to do it in a script.

# ----------------------------------------------------------------------------
# 1. QUICK STYLE: Easy to do while you're on the command line;
#                 tricky to translate into a script.
# 
# This style makes all plotting calls directly on plt, which keeps track of
# the state of all your figures and axes for you, in the background.
"""
from gfx_helper_repl import *
x = np.linspace(-5, 5, 51)
y = 0.4*x**2 - 0.8*x - 4
plt.plot(x, y)
plt.grid(True)
"""
# Notice that, as soon as you call anything directly on plt, the effects of
# your call are displayed immediately.
#   However, if you want to mess with the axes, you need to ask plt for them,
# and the changes you make will not appear immediately.  To get them to show
# up, you need to explicitly tell plt to re-show the current plot.
"""
plt.gca().set_xlim(-5,5)  # GCA stands for Get Current Axes.
plt.gca().set_ylim(-5,5)
plt.show()
"""
# We can plot more, and our next plot will show up on the same axes in a
# different color, all taken care of for us by plt:
"""
plt.plot(x, -y)
"""


# ----------------------------------------------------------------------------
# 2. CAREFUL STYLE: Annoying to do while you're on the command line;
#                   easier to translate into a script.
# 
# This style explicitly creates a figure and axes, and works with them much
# like a non-interactive script would.  However, that means that every time
# you plot something, you have to let the system know to re-draw.
"""
from gfx_helper_repl import *
x = np.linspace(-5, 5, 51)
y = 0.4*x**2 - 0.8*x - 4
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect='equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid(True)
ax.plot(x, y)
"""
# Notice that, though the figure window popped up right away, no axes or plots
# have yet appeared.  In order to show our plot, we have to explicitly tell
# the figure to re-render its contents:
"""
fig.show()
"""
# We can plot more, and our next plot will show up on the same axes in a
# different color, just as in the example above.  But we again have to tell
# the figure to show its new contents.
"""
ax.plot(x, -y)
fig.show()
"""


# ----------------------------------------------------------------------------
# 3. SCRIPT STYLE: The appropriate way to plot in non-interactive scripts.
# 
# This style explicitly creates a figure and axes, just like the Careful Style
# above.  There are just a couple differences:
"""
from gfx_helper_script import *  # <-- DIFFERENCE #1: _script, not _repl.

x = np.linspace(-5, 5, 51)
y = 0.4*x**2 - 0.8*x - 4
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect='equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid(True)
ax.plot(x, y)
"""
# We can't show the figure until we've plotted everything we need to plot!
# Unfortunately, though, plt doesn't keep track of the plot colors for us, so
# we have to specify a different color if we want it.
"""
ax.plot(x, -y, 'g')  # <-- DIFFERENCE #2: explicitly specifying line style.
"""
# Now that we've set up the figure and axes, we show everything at once,
# causing a window to pop up.  This should usually be the last call executed
# in your script.  Execution will pause here until the window is closed.
# Once the window is gone, your figure and axes are invalid, so you'd have to
# make all new ones to do anything further.
"""
plt.show()  # <-- DIFFERENCE #3: plt, not fig.
"""

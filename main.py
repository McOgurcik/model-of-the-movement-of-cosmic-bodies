import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle
import PySimpleGUI as sg
import math
import matplotlib as mt
import numpy as np
h = 12
w = 2
dt = 0.001
vx = 0
vy = 1.3
x_0 = 1
x = 1.2
y = 0
tk = 40
class Canvas(FigureCanvasTkAgg):
  """
    Create a canvas for matplotlib pyplot under tkinter/PySimpleGUI canvas
    """

  def __init__(self, figure=None, master=None):
    super().__init__(figure=figure, master=master)
    self.canvas = self.get_tk_widget()
    self.canvas.pack(side='top', fill='both', expand=1)
def cm_to_inch(value):
  return value / 2.54
def f(u,x,y):
    k = (x*x + y*y)**0.5
    return (-1*u/(k*k*k))
def plot_figure(vx,vy,x_0,tk):
    try:
        ax.cla()
        tk = float(tk)
        x_0 = float(x_0)
        vy = float(vy)
        x = [x_0]
        y = [0]
        i = 0
        t = dt
        while t < tk:
            vx = vx + f(x[i],x[i],y[i])*dt
            vy = vy + f(y[i],x[i],y[i])*dt
            x.append(x[i]+vx*dt)
            y.append(y[i]+vy*dt)
            i = i + 1
            t = t + dt
        ax.set_aspect('equal')
        ax.set_xlim((np.min(x)-10), np.max(x)+10)
        ax.set_ylim((np.min(y)-10), np.max(y)+10)
        circle1 = plt.Circle((0, 0), 1, color='r')
        ax.add_patch(circle1)
        ax.set_title(r'Модель движения космического тела', fontsize=16)

        ax.plot(x, y, color='g')
        canvas.draw()
    except:
        print("err")
        ax.cla()
        return
sg.theme('DefaultNoMoreNagging')
layout = [
    [sg.Canvas(size=(640, 480), key='Canvas')],
    [sg.Text('x'), sg.Input(1.2,enable_events=True,k='-X-',size=(9, 1)),
    sg.Text('vy'), sg.Input(1.3,enable_events=True,k='-VY-',size=(7, 1)),
    sg.Text('tk'),
    sg.Spin([i for i in range(1, 2000)],
            initial_value=40,
            enable_events=True,
            k='-TK-')],
    [[sg.Push(), sg.Button('go'), sg.Push()]]
    ]
window = sg.Window('Движение тела в поле тяжести',
                   layout,
                   finalize=True,
                   resizable=True)

fig = Figure(figsize=(cm_to_inch(16), cm_to_inch(10)))

ax = fig.add_subplot()
canvas = Canvas(fig, window['Canvas'].Widget)
def launch():
    plot_figure(vx,vy,x_0,tk)
while True:
  event, values = window.read()
  # print(event)
  if event in (sg.WIN_CLOSED, 'Exit'):
    break
  elif event == '-X-':
      x_0 = values[event]
  elif event == '-VY-':
      vy = values[event]
  elif event == '-TK-':
      tk = values[event]
  elif event == 'go':
      launch()

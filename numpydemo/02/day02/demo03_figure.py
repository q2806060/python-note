"""
demo03_figure.py 窗口构建 
"""
import matplotlib.pyplot as mp

mp.figure('Figure A', facecolor='lightgray')
mp.figure('Figure B', facecolor='black')
mp.figure('Figure A')
mp.title('Figure A', fontsize=18)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.tight_layout()
mp.show()






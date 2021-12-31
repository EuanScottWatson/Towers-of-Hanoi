# Towers of Hanoi
Simple program to show how towers of hanoi can be solved by counting in binary. The nth bit from the left corresponds to the nth smallest disc and whenever that bit is flipped from a 0 to a 1, the disc is move to the right to the next available slot.
There is a CLI version called `towers.py` and a GUI version called `hanoi.py` run either with a number to represent how many discs (max. is 21), i.e.:
```
python filename.py <number of discs>
```
With the GUI version, you can press `SPACE` bar to run the solution or when the solution is paused, press the `S` key to step through the solution.
# last.fm-Statistics
A GUI Program Showing last.fm Statistics Using PyQt5 and BeautifulSoup

As the title suggests, this litte piece of code helps you get your -or any user's- listening data for the determined time interval. 

Running the file named "datagui.py" on any Python interpreter or running it directly from your terminal will start the program.

In this program, BeautifulSoup and PyQt5 modules are used for fetching the data from last.fm and creating a graphical user interface, respectively.
Therefore one might want to install the modules first, if they're not already installed.

To do this, enter these commands in your terminal:

  pip install bs4
  
  pip install PyQt5
  
The file named "datafetcher.py" contains a function to get the data from last.fm. The function can work without the GUI with a couple of small modifications on its own.
The file named "datagui.py" is the one that creates the GUI for our program. Since it's my first take on PyQt5 it has some flaws, yet works without a problem.
There's also an image named "loveless.jpg". It is the background image for the program and also the cover photo of one of the best and most influential albums ever made. You can change it as well, you just need to put the image you want as a background in the same directory as the program and in datagui.py enter the name of the image into the indicated line.

Enjoy and please inform me about the bugs in the codes.



<h1 align="center">
  <a href="http://sistemas.jf.ifsudestemg.edu.br/graphfilter/home"><img src="/resources/icons/hexagon.png" alt="Graph Filter" width="180"></a>
  <br><br>
  Graph Filter
  <br>
</h1>

<h4 align="center"> Software to help Graph researchers providing filtering and visualization to a given list of graphs.</h4>

<p align="center">
  <a href="#about">About</a> •
  <a href="#features">Features</a> •
  <a href="#used-libraries">Used Libraries</a> •
  <a href="#installation">Installation</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#more">More</a> •
  <a href="#%EF%B8%8F-license">License</a>
</p>

## About
The main goal of this software is to give assistance to Graph Theory and Spectral Graph Theory researchers to establish or refute conjectures quickly and simply,
providing for visualization a filtered list of graphs according to the properties given by the user. 

> This project is a reimplementation in python of [GraphFilter](https://github.com/GraphFilter/GraphFilter-Deprecated) project in order to provide more functionalities to the software, in addition to better performance.
> * Graph Filter v1.1 was published in [Anais of X-ERMAC-RS: Encontro Regional de Matemática Aplicada e Computacional](https://editora.pucrs.br/edipucrs/acessolivre/anais/1501/assets/edicoes/2020/arquivos/105.pdf).
> * Graph Filter v2.0 was submitted to the [Simpósio Brasileiro de Pesquisa Operacional 2021, 53ª edição](https://sbpo2021.galoa.com.br) and is under analysis.

The software has the purpose of filtering a list of graphs through conditions customized by the user, without requiring programming knowledge. After the process, the filtered graphs are returned and the user can analyze them according to his cientific research. This user will have access to plot of the graphs and the calculation of several invariants, at the user's choice.


## Features
+ Filter graphs with conditions customizable by the user;
+ Visualization of filtered graphs, with calculation of invariants.
+ The filtered graphs can be exported to different file formats.
+ Intuitive layout, does not require programming knowledge;
+ Support for several graph invariants;
+ It helps the researcher in Graphs to test conjectures and results.

## Used libraries 

|    Calculations of invariants                   |   GUI development                                           |  Utilities                                               |
| :------------:                                  | :---------:                                                 | :---------:                                              |
| [Networkx](https://networkx.org/)               | [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)  | [Matplotlib](https://matplotlib.org/)                    |
| [Grinpy](https://github.com/somacdivad/grinpy)  |  [PyQtGraph](http://www.pyqtgraph.org/)                     | [network2tikz](https://github.com/hackl/network2tikz)    |
| [Numpy](https://numpy.org/)                     |                                                             | [simpleeval](https://github.com/danthedeckie/simpleeval)  |

## Installation
You can run the program from the source code or from an executable file.

### Source code
To from the source code, you have to:

- Install [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installing/).  
- [Clone this project using git](https://github.com/GraphFilter/GraphFilter/wiki/Setup#cloning) or [Download the source code from the release](https://github.com/GraphFilter/GraphFilter/wiki/Setup#downloading)
- Create and activate a [Virtual Environment](https://github.com/GraphFilter/GraphFilter/wiki/Setup#virtual-environment) (optional)
- [Install the requirements](https://github.com/GraphFilter/GraphFilter/wiki/Setup#install-required-libraries)
- Then, [run the ```app.py```](https://github.com/GraphFilter/GraphFilter/wiki/Setup#running) from the project's source folder

First, install the project from the [Releases](https://github.com/GraphFilter/GraphFilter/releases), download the program of the latest version to your specific Operation System:

### Windows
### Linux
### Mac

## Getting started

When opening the program, at the first page start a new project clicking on the New Project button.
<br/>
<br/>
<image src="/resources/images/welcome_window.png" width="500">

When starting a new project, you will be guided through a wizard to select the filtering conditions.

### First, choose the Project Name and the Project Location.
<image src="/resources/images/wizard_project_info.png">

### At the Equations page, insert the equation you want to use to filter graphs.
You can insert the (in)equations involving the invariants of your choice, using either the keyboard or the buttons to assist in the insertion. You can also leave it empty, but then you will have to choose a least one Condition to filter.
<br/>
<br/>
![](/resources/gif/equation_page.gif)
  
### Choose a condition to the filter
You can check the Boolean conditions you want to impose on your filtering. When you mark TRUE on an invariant, the program will only filter those that satisfy the condition. Respectively check FALSE if you do not want graphs that satisfy that condition. If you are indifferent, just don't check that invariant.
<br/>
<br/>
<image src="/resources/images/wizard_conditions.png">

### Choose the method to filter
The user decides which filtering method: if he wants to filter all the graphs, among his input list, that satisfy the imposed conditions. Or if you prefer, just look if there is a graph that does not satisfy those conditions, useful for trying to refute conjectures.
<br/>
<br/>
<image src="/resources/images/wizard_method.png">


### Input the files with the graphs you want to filter
Here you can load the graphs for filtering. The file format of the entry is .g6 or .txt containing a list of graphs in graph6. Note that the user can insert more than one file.
<br/>
<br/>
<image src="/resources/images/wizard_input_graphs.png">

> Graph6 is a compact format file, created by [D. McKay](https://users.cecs.anu.edu.au/~bdm/data/formats.txt). But you do not have to understand how this fortat works. You can find files in this format for different classes of graphs on the pages: 
> * [House of graphs](https://hog.grinvin.org/MetaDirectory.action)
> * [Database from Brendan D. McKay](http://users.cecs.anu.edu.au/~bdm/data/graphs.html)  
> 
> This pages will let you choose the kind of graphs you want, and then export in Graph6 format for you.

----

After these steps, the program will analyze all the conditions and the filtering will be performed. When finished, a window will open for viewing and analyzing each graph returned in the filtering.

### Project Main Window
Here you can see a visualization of the graph, allowing the movement in the vertices with the mouse cursor. There is also a List of invariants to be calculated in the displayed graph, just mark the desired invariants and they will appear in the Info dock, which can be resized or even seen as a separate window, for a better visualization. In the dictionary tab you can see a short definition of each invariant implemented in the program.

To navigate between the graphs returned from the filtering, you can use the combo box or navigation arrows at the top of the window.

In the "File> Export to" menu, you can export the graphs returned in the filtering to other formats: PDF, PNG, TikZ or graph6.

![](/resources/gif/complete_main_window.gif)

## More
For further information on how to use the program, please go to the [Wiki](https://github.com/GraphFilter/GraphFilter/wiki) page.

## ⚖️ License
[GNU General Public License v3.0](https://github.com/GraphFilter/GraphFilter/blob/main/LICENSE)

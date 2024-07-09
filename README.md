<h1 align="center">
  <a href="http://sistemas.jf.ifsudestemg.edu.br/graphfilter/home"><img src="/resources/icons/graph_filter_logo.png" alt="Graph Filter" width="180"></a>
  <br>
  Graph Filter
  <br>
</h1>

<p align="center">
<a href="https://doi.org/10.5281/zenodo.8208909"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.8208909.svg" alt="DOI"></a>
</p>

<h4 align="center"> Software for manipulating and searching graphs.</h4>

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
> * Graph Filter v2.0 was published in [Anais do LIII Simpósio Brasileiro de Pesquisa Operacional, 2021](https://proceedings.science/sbpo-series/sbpo-2021/papers/graph-filter-2-0--nova-versao-do--software-para-filtragem-de-grafos?lang=pt-br).

The Graph Filter is a software to help graph researchers, with a simple and intuitive interface. It allows you to draw, save and manipulate graphs with the mouse and keyboard. It provides more than 170 invariants (spectral and structural) and some graph operations, which are calculated in a few clicks.

Another purpose of the software is to filter graphs: the user enters conditions and equations, attaches a list of up to thousands of graphs, then the program filters the graphs that meet the conditions. An important tool for drawing up results and finding counterexamples. You can also export the graphs in different formats.

The program is supported by any Windows, Linux and Mac. No installation is required, [just download and run](http://sistemas.jf.ifsudestemg.edu.br/graphfilter/download).

## Features
+ Filter graphs with conditions customizable by the user;
+ Visualization of filtered graphs, with calculation of invariants.
+ The filtered graphs can be exported to different file formats.
+ Intuitive layout, does not require programming knowledge;
+ Support for several graph invariants;
+ It helps the researcher in Graphs to test conjectures and results.
+ Visualize, draw and manipulate Graphs
+ Create well-known Graph layouts
+ Manipulate files with an tree file manager

## Used libraries 

|    Calculations of invariants                   |   GUI development                                           |  Utilities                                               |
| :------------:                                  | :---------:                                                 | :---------:                                              |
| [Networkx](https://networkx.org/)               | [PyQt6](https://www.riverbankcomputing.com/software/pyqt/)  | [Matplotlib](https://matplotlib.org/)                    |
| [Grinpy](https://github.com/somacdivad/grinpy)  | [Netgraph](https://github.com/paulbrodersen/netgraph)       | [network2tikz](https://github.com/hackl/network2tikz)    |
| [Numpy](https://numpy.org/)                     |                                                             | [simpleeval](https://github.com/danthedeckie/simpleeval) |

## Installation
You can run the program from an executable file or from the source code.

### Run from an executable (release)
Download the compact file from the release that matches your Operational System.

- [Windows](https://github.com/GraphFilter/GraphFilter/wiki/Windows-Configurations#executing)
- [Linux](https://github.com/GraphFilter/GraphFilter/wiki/Linux-Configurations#executing)
- [Mac](https://github.com/GraphFilter/GraphFilter/wiki/Mac-Configurations#executing)

### Run from source code
To run from the source code, you have to:

- Install Python and Pip.
- Clone this project using git or Download the source code from the release
- Create and activate a Virtual Environment (optional)
- Install the requirements
- Then, run the ```app.py``` from the project's source folder

You can see more details about these steps clicking [here](https://github.com/GraphFilter/GraphFilter/wiki/Run-project-from-source-code)

## Getting started

When opening the program, at the first page start a new project clicking on the New Project button.
<br/>
<h4 align="center">
<image src="/resources/images/welcome_window.png" width="500">
</h4> 
When starting a new project, you will be guided through a wizard to select the filtering conditions.

### First, choose the Project Name and the Project Location.
<h4 align="center">
<image src="/resources/images/wizard_project_info.png" width="800">
</h4> 

  ### At the Equations page, insert the equation you want to use to filter graphs.
You can insert the (in)equations involving the [invariants](https://github.com/GraphFilter/GraphFilter/wiki/Invariants-and-Operations#numeric-invariants) and [operations](https://github.com/GraphFilter/GraphFilter/wiki/Invariants-and-Operations#operations)of your choice, using either the keyboard or the buttons to assist in the insertion. You can also leave it empty, but in the next step you will have to choose a least one Condition to filter.

<p align="center">
<image src="/resources/gifs/wizard_equations.gif" width="800">
</p> 
  
### Choose a condition to the filter
You can check the [Boolean conditions](https://github.com/GraphFilter/GraphFilter/wiki/Invariants-and-Operations#boolean-invariants) you want to impose on your filtering. When you mark TRUE on an invariant, the program will only filter those that satisfy the condition. Respectively check FALSE if you do not want graphs that satisfy that condition. If you are indifferent, just don't check that invariant.

<h4 align="center">
<image src="/resources/images/wizard_conditions.png" width="800">
</h4> 

### Choose the method to filter
The user decides which filtering method: if he wants to filter all the graphs, among his input list, that satisfy the imposed conditions. Or if you prefer, just look if there is a graph that does not satisfy those conditions, useful for trying to refute conjectures.

<h4 align="center">
<image src="/resources/images/wizard_method.png" width="800">
</h4>

### Input the files with the graphs you want to filter
Here you can load the graphs for filtering. The file format of the entry is .g6 or .txt containing a list of graphs in graph6. Note that the user can insert more than one file.

<p align="center">
<image src="/resources/gifs/wizard_input_graphs.gif" width="800">
</p>

> Graph6 is a compact format file, created by [D. McKay](https://users.cecs.anu.edu.au/~bdm/data/formats.txt). But you do not have to understand how this fortat works. You can find files in this format for different classes of graphs on the pages: 
> * [House of graphs](https://hog.grinvin.org/MetaDirectory.action)
> * [Database from Brendan D. McKay](http://users.cecs.anu.edu.au/~bdm/data/graphs.html)  
> 
> This pages will let you choose the kind of graphs you want, and then export in Graph6 format for you.

----

After these steps, the program will analyze all the conditions and the filtering will be performed. When finished, a window will open for viewing and analyzing each graph returned in the filtering.

### Project Main Window
Here you can visualize, [draw](https://github.com/GraphFilter/GraphFilter/wiki/Features#graph-editing-features) and manipulate the graph on the screen. There is also a List of invariants to be calculated in the displayed graph, just mark the desired invariants and they will appear in the Info dock, which can be resized or even seen as a separate window, for a better visualization. In the [dictionary tab](https://github.com/GraphFilter/GraphFilter/wiki/Dictionary#invariants) you can see a short definition of each invariant implemented in the program.

<p align="center">
<image src="/resources/gifs/project_visualize.gif" width="800">
</p>

  > To navigate between the graphs returned from the filtering or opened from a .g6, .txt file, you can use the combo box or navigation arrows at the top of the window.

#### Tool Bar

The toolbar gives you access to some of the software's features, such as applying certain [operations](https://github.com/GraphFilter/GraphFilter/wiki/Features#operations), exporting, inserting a [universal vertex](https://github.com/GraphFilter/GraphFilter/wiki/Features#operations), saving the edited graph or deleting it. These functions refer to the graph on the screen. You can also create a new well-known used graph to work with the software. In the [dictionary tab](https://github.com/GraphFilter/GraphFilter/wiki/Dictionary#graphs), you can see all the new graphs options with their definitions and parameters.

<p align="center">
<image src="/resources/gifs/project_toolbar.gif" width="800">
</p>
  
#### File Tree
  In the left-hand corner you can see a tree of files, opened in the directory previously selected in Open or New Project. 
In the tree you can double-click with the left button to open the folder or file, or right-click to display the menu with the following options:
- Load File: This will load the file into the window, if they are graphs they will be plotted.
- Export all graphs: Export all the graphs in the file in one of the selected file types.
- Delete: Delete the file or empty folder

<p align="center">
<image src="/resources/gifs/project_tree.gif" width="800">
</p>

#### File Types and Exports
  The software accepts the following file types:
- .g6 and .txt : Responsible for storing a list of graphs.
- .gml: Able to store just one graph, but in more detail, such as the position of the vertices. 
- .json: The result of the old way the software worked, there are still json files that store a list of graphs, but this type will be deprecated.

The software can export graphs in the following file types:
> When export is selected via the tool bar only the open graph will be exported, whereas when the export option is selected via the tree all the graphs in the file will be exported.
- Graph(.gml),
- Graph6(.g6 ou .txt),
- Image(.png ou .pdf),
- Latex Tikz(.tex), or
- Sheets with invariants (.xlsx

> In the case of files exported in .xlsx, the numerical and boolean data from the information dock will be exported to the table.
 
## More
For further information on how to use the program, please go to the [Wiki](https://github.com/GraphFilter/GraphFilter/wiki) page.

## ⚖️ License
[GNU General Public License v3.0](https://github.com/GraphFilter/GraphFilter/blob/main/LICENSE)

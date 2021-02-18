# Introduction
This repository contains the instruction on how to install and use the dfgcompare library.

# Installation 
To install and use dfgcompare, some requirement shall be fulfilled, which is describe in pre-requisite section.
If you already installed the graphviz, you can move to the Installing dfgcompare phase directly.

## Pre-requisite
It is assumed that you have basic knowledge of Python and how to run ipynb files using jupyter lab.
dfgcompare depends on graphviz which is depends on the C++ compiler.
Please note that you need to follow the instruction that is specified in [download instruction for graphviz](https://www.graphviz.org/download/).
Also, graphviz requires custom configuration if it is installed on Windows operating system as described in [configuration](https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224).
The instruction is similar to PM4Py, which is fully described in [installation guideline for PM4Py](https://pm4py.fit.fraunhofer.de/install).

## Installing dfgcompare
If these requirements are fulfilled, the library can be installed using this command:
```
pip install dfgcompare
```

# Example
The provided example shows how dfgcompare can be used. To run the example, you need to install these two libraries on your computer:
```
pip install jupyter jupyterlab
```
The example can be viewed in [sample dfgcompare analysis](./sample_analysis.ipynb).

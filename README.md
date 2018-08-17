LaTeX Templates for SuperMemo-0
===============================

Introduction
------------
The current repository contains LaTeX templates for SuperMemo data- and
schedule books, as described in "Using SuperMemo without a computer" by Dr.
Piotr Wozniak at https://www.supermemo.com/articles/paper.htm (also known as
algorithm SM-0).

Requirements
------------
* LaTeX
* GNU Make (Optional)

Installation
------------
If you have Git installed, executing the following command will create a
directory `supermemo0/`, clone the entire repository therein and checkout the
master branch:
```
git clone https://github.com/arnobastenhof/sm-0.git
``` 
Alternatively, Github offers the possibility to download a ZIP file containing
the sources from whichever branch is being viewed. E.g., to download the
master branch, run
```
wget https://github.com/arnobastenhof/supermemo0/archive/master.zip
unzip master.zip
mv supermemo0-master supermemo0
```
Next, navigate to the project root and run a build:
```
cd supermemo0
make all
```
This should create `databook.pdf` and `schedule.pdf` in the project root.

Usage
-----
To add questions, modify `tex/deck.tex`. For illustrative purposes examples of
questions and answers are already included, taken directly from the aforecited
document. 

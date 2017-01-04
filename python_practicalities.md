# Python for statistics and data analysis

### First, try it out

You can run Python in your browser without installing anything onto
your computer:

* [try.jupyter.org](https://try.jupyter.org) requires no sign-up.
  When the page loads, press the "New" button and select either
  "Python 2" or "Python 3"

* [cloud.sagemath.com](https://cloud.sagemath.com) requires you to
  create an account but provides a few more features


If you want to install Python and a collection of libraries for data
analysis onto your computer, one relatively simple approach is to use
[anaconda](http://continuum.io/downloads).  See below for other
options.


### Learning Python

There are many excellent Python tutorials on the web.  Some of our
favorites are:

* [The official Python tutorial](https://docs.python.org/2/tutorial)

* [Non-Programmer's Tutorial for Python](http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3)

* [Two talks from Google I/O](https://www.youtube.com/watch?v=bDgD9whDfEY)

### About Python

Python is a general-purpose programming language.  It was not
developed specifically as a language for data management and analysis,
but it works very well for that purpose.

In contrast, Matlab, [R](http://cran.org), and
[Julia](http://julialang.org) are "domain specific languages" (DSL's).
They were specifically designed for scientific computing and data
analysis.

Python implementations exist for many platforms and hardware
configurations.  The core language and libraries behave in a highly
consistent way across a variety of platforms (Windows, Linux, MacOS,
many others).

Python is not an exotic or revolutionary language.  It should seem
obvious and natural to anyone familiar with generic "pseudo-code".  It
has a few distinguishing features, most notably, the use of
indentation rather than braces to define code blocks.

### Python libraries

Python itself is not very useful for scientific work.  However by
using Python together with some powerful libraries, many things become
possible.

Here are the libraries that we discuss in our workshops:

* [Pandas](http://pandas.pydata.org): data management

* [Matplotlib](http://matplotlib.org): graphics and plotting

* [Statsmodels](http://statsmodels.sourceforge.net): statistical
  models and data analysis tools

* [Numpy](http://www.numpy.org): array processing and linear algebra,
  provides matrix algebra functionality similar to Matlab and R (but
  with some different syntax)

* [Scipy](http://www.scipy.org): numerical routines such as
  integration, optimization, and special functions

### Numerical performance

Python is an interpreted language like R and Matlab.  It is possible
to write code that runs reasonably quickly, but it is also possible to
write code that performs poorly.  There are many ways to write Python
code that both performs well and is easy to read and maintain.  One
general principle for achieving good performance is to take advantage
of libraries like Numpy that are implemented in C.

It is possible to write C extensions to Python.  This is made
particularly easy by using a tool called [Cython](http://cython.org).
However, most users will rarely if ever need to use Cython.

### Python 2 versus Python 3

The Python community is currently progressing through a transition
from the "2 series" Python implementations to the "[3
series](https://docs.python.org/3.0/whatsnew/3.0.html)" Python
implementations.  Python 3 scripts may not run in Python 2, and Python
2 scripts may not run in Python 3.  Nearly all libraries have been
substantially modified to work in both Python 2 and Python 3, and this
process is now largely complete.

There are many small changes and a few large changes from Python 2 to
Python 3.  Many of these changes are of little consequence to most
users of Python for scientific purposes.

### Tools for working with Python

The base Python interpreter has a simple command-line interface.  Many
powerful tools for working with Python scripts and interacting with
the interpreter have been developed.  These tools are surveyed here.

* [IPython](http://ipython.org) -- a shell for working with Python
  interactively.  This tool provides far more functionality than the
  basic Python command line.  It can be run in a terminal (providing a
  text-only interface), and it is a component of many graphical and
  browser-based environments.

* [Jupyter](http://jupyter.org) (formerly known as the "IPython
  notebook") -- cell-based manipulation of Python code, runs in a
  browser.  This is an ineractive graphical environment that embeds
  the standard text-based IPython command line.

* Integrated Development Environments (IDEs):
    * [Spyder](http://code.google.com/p/spyderlib)
    * [IEP](http://iep-project.org)
    * [Canopy](https://www.enthought.com/products/canopy)
    * [Idle](https://docs.python.org/2/library/idle.html)

* [Pdb](https://docs.python.org/2/library/pdb.html) -- a debugging tool
  built into many Python shells and IDE's

* Automatic code checking:
    * [Pyflakes](https://launchpad.net/pyflakes)
    * [Pylint](http://www.pylint.org)
    * [pep8](https://pypi.python.org/pypi/pep8)
    * [Pychecker](http://pychecker.sourceforge.net)

* Python environments for text editors -- modes for Emacs and Vim
    * [Emacs modes](http://www.emacswiki.org/emacs/PythonProgrammingInEmacs)
    * [Vim modes](https://github.com/klen/python-mode)


# Python installation

## Installing from a distribution

Installing Python and its scientific libraries from scratch is
possible, but is challenging and time consuming.  The easiest way to
get up and running quickly with Python is to either use a cloud
service, or to install a bundled distribution of the entire scientific
Python stack.  Here are some Python distributions that are suitable
for data analytic work:

* [Enthought Canopy](https://www.enthought.com/products/canopy)

* [Continuum Anaconda](http://continuum.io/downloads)

* [Python-xy](https://code.google.com/p/pythonxy/) -- Windows only

* [Pyzo](http://www.pyzo.org)

## Installing Python from source

If you use Linux or MacOS and have a working compiler like gcc in your
system, you can install core Python by first downloading the source
tarball (pythonxxx.tar.gz) from
[www.python.org](https://www.python.org/downloads), then following
these steps (change pythonxxx to the specific file name):

```
tar --xz -xvf pythonxxx.tar.xz
cd pythonxxx
./configure
make
make install
```

Note that you need to have root access on the machine to do this.  If
you do not have root access, it is possible to install everything in
an arbitrary location by replacing the configure step above with

```
./configure --prefix=/path/to/location
```

If you install Python in a non-standard location you will need to use
the full path to the executable to launch it (or make an alias in your
.bashrc or other shell configuration file).

Next you need to install each of the core libraries.  Briefly,
download an archive file for each library, e.g. numpyxxx.tar.gz, then

```
gunzip numpyxxx.tar.gz
tar -xvf  numpyxxx.tar
cd numpyxxx
python setup.py install
```

Note that the gunzip and tar steps may differ depending on the archive
format (.tar.gz, .tar.bz2, .tar.xz, .zip).  The `python` command in
step 4 should invoke whichever Python installation on your system you
want to link to the libraries (i.e. if you have installed several
Pythons, you need to use the right one here).

An alternative way to install the libraries (but not Python itself) is
to use [pip](https://pypi.python.org/pypi/pip).  To install numpy, for
example, using pip, type `pip install numpy` into the command line of
your computer.  Note that you may have several Python distributions
installed on your machine.  Each distribution will have its own
directory tree and libraries, and its own copy of pip.  You need to
use the pip that belongs to the python installation you intend to work
with when installing libraries to be accessed by that installation.

If you are using Anaconda Python, you can use the command `conda` to
install packages, e.g. `conda install numpy`.

`vitualenv` is a utility that allows you to easily maintain multiple
independent Python environments.  It is also useful if you want to
maintain only a single environment in a non-standard location.

## Installing on Windows using binaries

If you use Windows and have administrator access to your system, you
can scour the web for the core language and various libraries in
self-extracting executable (\*.exe) format, and install them by
running them (double click on the \*.exe).

A good resource for up-to-date windows packages for Python is
[here](http://www.lfd.uci.edu/~gohlke/pythonlibs)

# Using Python for data analysis in the cloud

Several services allow you to use Python without installing any
software on your own machine.  These services provide servers on which
the scientific Python stack is installed.  Users connect to these
services through a web interface, so all you need to use them is a
computer with a web browser.  Many people see this approach as the
future of scientific computing, but the current generation of cloud
computing services for scientific Python has some limitations.
Nevertheless, it is usable, especially for training and learning.

* [try.jupyter.org](https://try.jupyter.org) this site requires no
  sign-up but may not include a complete set of libraries.

* [Sage math cloud](https://cloud.sagemath.com) -- this service
  provides both the IPython notebook and their own notebook format.
  In addition to Python, they provide R, C, Fortran, and several other
  tools.  Currently all accounts are free.

* [Wakari](https://www.wakari.io) -- a commercial service provided by
  Continuum Analytics.  They provide free accounts, but these are
  often unusable during busy times of day, and their free system is
  too slow for most real analyses.  However it is quite useful for
  learning, teaching, and training.  The system exclusively uses the
  IPython notebook, and does not support languages other than Python.
  It is fairly easy to configure your own environment (e.g. loading
  non-standard Python libraries).

* The SCS servers (scs.itd.umich.edu) -- a U-M internal service, the
  "old school cloud" is a set of Linux servers.  To use this system,
  you need to learn how to use ssh to connect to a remote machine, and
  use terminal tools like text editors (Emacs or Vim).  These machines
  currently lack an updated Python distribution with all the libraries
  discussed here, but with some work it is possible to install
  everything in "user space".
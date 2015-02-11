## The core Python language

There are many excellent Python tutorials on the web.  Some of our
favorites are:

* [The official Python tutorial](https://docs.python.org/2/tutorial)

* [Non-Programmer's Tutorial for Python](http://en.wikibooks.org/wiki/Non-Programmer's_Tutorial_for_Python)

* [Two talks from Google I/O](https://www.youtube.com/watch?v=bDgD9whDfEY)

### How is Python related to other numerical computing environments?

Python is a general-purpose programming language.  It is used for many
purposes and was not conceived of specifically as a language for data
management and data analysis (or for any other single purpose).

Python implementations exist for many platforms and hardware
configurations.  The core language and libraries behave in a highly
consistent way across a variety of platforms (Windows, Linux, Max,
many others).

Matlab and R are "domain specific languages" (DSL's).  They were
primarily designed for one purpose.  Scientists who like to think of
computer programs simply as sequences of calculations seem to prefer
simple languages that translate mathematical logic directly into
computer code.  Matlab and [Julia](http://julialang.org) reflect this
perspective.  On the other hand, people who have learned some basic
ideas from modern computer science often prefer a language that
incorporates capabilities such as more advanced data structures
(e.g. associative arrays), functions as first-class objects, closures,
and pass-by-reference semantics (most or all of this is available in R
and Matlab in some way, but perhaps not very naturally or as the
default).

### Speed

Python itself has rather poor numerical performance compared to
compiled languages like C and Fortran. However Python has a large
number of excellent libraries that provide very good (even excellent)
numerical performance on many problems.

Due to the huge community of Python users, the core language and
interpreter have been heavily optimized for performance.  Interpreted
Python is generally faster than interpreted [R](http://cran.org).
However, in any interpreted language, complicated operations will be
somewhat slow.  Most generic operations in Python (like sorting a
list) are implemented in C.  These generic operations will take
roughly the same time to execute in any well-implemented language
(e.g. R, Matlab, Python, C, Java).

It is possible to write C extensions to Python.  This is made
particularly easy by using a tool called
"[Cython](http://cython.org)".  However, most users will rarely if
ever need to use Cython.  Due to the availability of excellent Python
libraries such as [Numpy](http://www.numpy/org), it is often possible
to express complex calculations in such a way that most of the work
takes place in the library (where time-critical components will
already have been written in C).

### What is distinctive about Python?

Python is not (and was not intended to be) an exotic or revolutionary
language.  It should seem obvious and natural to anyone familiar with
generic "pseudo-code".  It has a few distinguishing features, most
notably, the use of indentation rather than braces to define code
blocks.

### Python 2 versus Python 3

The Python community is currently progressing through a transition
from the "2 series" Python implementations to the "[3
series](https://docs.python.org/3.0/whatsnew/3.0.html)" Python
implementations.  Changes in the series number (1, 2, and 3 so far)
indicate a major break with backward compatibility.  Python 3 scripts
may not run in Python 2, and Python 2 scripts may not run in Python 3.
Nearly all libraries have been substantially modified to work in
Python 3, and this process is now largely complete.  Version numbers
within a series (e.g. 3.1 versus 3.2) will generally be compatible,
except for bug fixes and introductions of new features.

There are many small changes and a few large changes from Python 2 to
Python 3.  These changes are generally of little consequence to most
users of Python for scientific purposes.

Many general-purpose Python users switched from version 2 to version 3
long ago.  Users of Python for scientific research have been slower to
switch, but as of 2015 are starting to do so in significant numbers.

# Tools for working with Python

The base Python interpreter has a simple command-line interface.  Many
more sophisticated tools for working with Python scripts and
interacting with the interpreter have been developed.  These tools are
surveyed here.

* [IPython](http://ipython.org) -- a shell for working with Python
  interactively.  This tool provides far more functionality than the
  basic Python command line.  It can be run in a terminal (providing a
  text-only interface), and it is a component of many graphical and
  browser-based environments.

* The [IPython notebook](http://ipython.org/notebook.html) --
  cell-based manipulation of Python code, runs in a browser.  This is
  a graphical environment that embeds the standard text-based IPython
  command line.

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


# Python libraries

Python itself is not very useful for scientific work.  However by
using Python together with some powerful libraries, many things become
possible.

The "scientific Python stack" is a loosely coupled association of the
core Python interpreter and a collection of powerful libraries.  This
is in contrast to, say, R and Matlab, where the linear algebra,
graphics, and other domain-specific capabilities are "baked in" to the
core language.

An advantage of the loosely coupled approach is that it is possible,
as needed, to experiment with alternative libraries, even for
fundamental things like array processing.  A disadvantage of this
approach is that sometimes the Python syntax does not allow data
structures to be manipulated in the most natural way.

Here are the libraries we discuss in our workshops:

* __Pandas__ (http://pandas.pydata.org): data management

* __Matplotlib__ (http://matplotlib.org): graphics and plotting

* __Statsmodels__ (http://statsmodels.sourceforge.net): statistical
  models and data analysis tools

* __Numpy__ (http://www.numpy.org): array processing and linear
  algebra, front end to a subset of Lapack, provides matrix algebra
  functionality similar to Matlab and R (but with some different
  syntax).

* __Scipy__ (http://www.scipy.org): numerical routines such as
  integration, optimization, and special functions


# Python installation

### Installing from a distribution

Installing Python and its scientific libraries used from scratch is
possible, but is challenging and time consuming.  The easiest way to
get up and running quickly with Python is to either use a cloud
service, or to install a bundled distribution of the scientific Python
stack.  Here are some Python distributions that are suitable for data
analytic work:

* Enthought Canopy (https://www.enthought.com/products/canopy)

* Continuum Anaconda (http://continuum.io/downloads)

* Python-xy (https://code.google.com/p/pythonxy/) -- Windows only

* Pyzo (http://www.pyzo.org)

### Installing Python from source

If you use Linux or MacOS and have a working compiler like gcc in your
system, you can install core Python by first downloading the source
tarball (pythonxxx.tar.gz) from (https://www.python.org/downloads),
then following these steps (change pythonxxx to the specific file
name):

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
to use pip (https://pypi.python.org/pypi/pip).  To install numpy, for
example, using pip, type `pip install numpy` into the command line of
your computer.  Note that you may have several Python distributions
installed on your machine.  Each distribution will have its own
directory tree and libraries, and its own copy of pip.  You need to
use the pip that belongs to the python installation you intend to work
with when installing libraries to be accessed by that installation.

If you are using Anaconda Python, you can use the command `conda` to
install packages, e.g. `conda install numpy`.

### Installing on Windows using binaries

If you use Windows and have administrator access to your system, you
can scour the web for the core language and various libraries in
self-extracting executable (*.exe) format, and install them by running
them (double click on the *.exe).

A good resource for up-to-date windows packages for Python is:
http://www.lfd.uci.edu/~gohlke/pythonlibs

# Using Python for data analysis in the cloud

Several services allow you to use Python without installing any
software on your own machine.  These services provide servers on which
the scientific Python stack is installed.  Users connect to these
services through a web interface, so all you need to use them is a
computer with a web browser.  Many people see this approach as the
future of scientific computing, but the current generation of cloud
computing services for scientific Python has some limitations.
Nevertheless, it is usable, especially for training and learning.

* [https://cloud.sagemath.com](Sage math cloud) -- this service
  provides both the IPython notebook and their own notebook format.
  In addition to Python, they provide R, C, Fortran, and several other
  tools.  Currently all accounts are free.  We have seen some service
  degradation in mid-day.

* [https://www.wakari.io](Wakari) -- a commercial service provided by
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
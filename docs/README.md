## Sphinx Documentation

### youtube tutorial
    https://www.youtube.com/watch?v=BWIrhgCAae0

### create directory for Sphinx Documentation
    mkdir docs

### move to dir
    cd docs

### install sphinx
    pip install sphinx

### install RTD theme
    pip install sphinx-rtd-theme

### create Sphinx documentation project structure
    sphinx-quickstart
    > Separate source and build directories (y/n) [n]: n
    > Project language [en]: ru

### move to upper folder
    cd ..

### sphinx create minimum folder structure based on __init__.py python packages
    sphinx-apidoc -o docs .

### modify index.rst
    modules

### modify conf.py
    import os
    import sys
    
    sys.path.insert(0, os.path.abspath('..'))

    extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc"]

    # Sphinx may not include docstrings from main.py 
    # if it is not explicitly configured to do so. 
    # By default, Sphinx looks for docstrings in modules and packages, 
    # but the main.py file may not be recognized as a module or package by Sphinx.
    # # To include docstrings from main.py in your Sphinx documentation, 
    # you can explicitly configure Sphinx to include the main.py file 
    # by modifying the conf.py file in your Sphinx project. 
    # You can use the autodoc extension to automatically include docstrings from Python modules
    
    autodoc_mock_imports = ["main"]

    html_theme = 'sphinx_rtd_theme'


### move to dir
    cd docs

### change make.bat (for windows) to make.sh (for linux)
    make.bat -> make.sh

### run make html
    make html

### run index.html
    [index.html](_build%2Fhtml%2Findex.html)

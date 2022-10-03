# gpa_calculator
The Strawberry Patch GPA Calculator App

# Setting up work environment.

- It is recommended to use [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) inside of [VS Code](https://code.visualstudio.com/) to have a consistent work environment.

- Then use CTRL+SHIFT+P (on Windows, should be the same on Mac and Linux) OR go to the menu View->Command Palette…

- Then type in “Remote-Containers: Open Folder in Container”. This will open a folder that you can select with the Dockerfile in it.

- You will be asked a question **"How would you like to create your container configuration?"**

- Choose From **'Docker File'**
    - **NOTE: It may take a few minutes to build the image from the Docker container the first time.**

- You are now working in a Docker Image, a specific one with a Linux environment with Python, Pip, Node.js, and NPM installed. 

- You can open the terminal with hotkey CTRL+SHIFT+` (tilde, not quotation) or by going to the menu and Terminal->New Terminal

- You should see something similar to this in the terminal: `root@214200bcda0c:/workspaces/proj#`
    - The `214200bcda0c` would probably be different because that is generated automatically if you do not explicitly name an image.

- You can test Linux environment by checking it in the terminal with cat /etc/os-release. You should see:

```system
PRETTY_NAME="Debian GNU/Linux 10 (buster)"
NAME="Debian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
VERSION_CODENAME=buster
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@be56144f1bc5:/workspaces/proj_setup/api# 
```

- You can check the Python version, Node.js (JavaScript without the browser) version, where they are installed and start writing code in those languages in the environment.

- To close the project in VS Code, go to menu File->Close Folder
    - If you are running a Docker container, also close the remote connection File->Close Remote Connection

- **NOTE: When you make a remote container from a Docker file in VS Code, it looks like it creates the `WORKDIR /api` but does not put you there. You have to navigate there yourself.**

```system
cd /api
```


# Developer's Documentation

- For Python code, using [Sphinx](https://www.sphinx-doc.org/en/master/) following [The Sphinx docstring format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)
- Can use [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) for VS Code.


## Developer's Documentation - Setting up Sphinx

- Using Sphinx explanation
    - [Part 1](https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-i-5/)
    - [Part 2](https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-ii-6/)

- [Sphinx: list of functions in a module](https://stackoverflow.com/questions/9770756/sphinx-list-of-functions-in-a-module)
    - [Python Sphinx Autosummary: Automated listing of member functions](https://stackoverflow.com/questions/20569011/python-sphinx-autosummary-automated-listing-of-member-functions/30783465#30783465)

- **NOTE:** Some recommend to not push the `build` folder to git or GitHub (i.e. do not put it under source control.) I beg to differ. I want the final rendered documents available. Do not want to recreate the environment just to be able to build it again in the future. In all likelihood, the exact builds won't be available.

- Created a folder in the root of the repo called `docs`
- Installed [Sphinx](https://www.sphinx-doc.org/en/master/) using pip in the Docker environment in the absolute path location `/workspaces/gpa_calculator`. This will make the files in your local repo as well since it is shared between your system and Docker container.
- [Answer on stack overflow by karlson - answered Apr 8 '15 at 11:52](https://stackoverflow.com/questions/7033239/how-to-preserve-line-breaks-when-generating-python-docs-using-sphinx)

- Different style docstring
    - [Support for NumPy and Google style docstrings](https://www.sphinx-doc.org/en/1.3.6/ext/napoleon.html?highlight=sphinx%20style)
    - [Example Google Style Python Docstrings](https://www.sphinx-doc.org/en/1.3.6/ext/example_google.html)
    - [Example NumPy Style Python Docstrings](https://www.sphinx-doc.org/en/1.3.6/ext/example_numpy.html#example-numpy)


```system
pip install sphinx
```
- You can check that it is installed with pip by checking the list

```system
pip list
```

- You should see something like this in the list (version numbers may be different depending when you do this and if you didn't specify the version number.)

```system
Sphinx                        4.1.2
sphinxcontrib-applehelp       1.0.2
sphinxcontrib-devhelp         1.0.2
sphinxcontrib-htmlhelp        2.0.0
sphinxcontrib-jsmath          1.0.1
sphinxcontrib-qthelp          1.0.3
sphinxcontrib-serializinghtml 1.1.5
urllib3                       1.26.6
```

- Now to set up Sphinx, navigate to the `docs` folder created (full absolute path should be `/workspaces/gpa_calculator/docs`)

```system
cd docs
```

- Now type 

```system
sphinx-quickstart
```

- Edit the `source/index.rst` file.
- The command to make a build, go back tot the `docs` folder `/workspaces/gpa_calculator/docs`.

```system
make html
```

- To see the HTML page, go to `build/html/index.html`

- To open it up in the terminal on Mac OSX with Google chrome

```system
open -a "Google Chrome" index.html
```

- Sphinx default theme is called "Alabaster"
    - [Link to themes](https://www.sphinx-doc.org/en/master/usage/theming.html)
    - [Creating your own themes](https://www.sphinx-doc.org/en/master/theming.html)
    - [Installing ReadtheDocs theme](https://pypi.org/project/sphinx-rtd-theme/)
    - [Vim commands](https://www.radford.edu/~mhtay/CPSC120/VIM_Editor_Commands.htm)

- Change theme in `conf.py` file `/workspaces/gpa_calculator/docs/source/conf.py`

- In the `conf.py`, look for the line that says `html_theme = 'alabaster'`, it is around line 50 at the time of this writing.

- Can change it to 'pyramid'

```python
html_theme = 'pyramid'
```

- Build again, go back tot the `docs` folder `/workspaces/gpa_calculator/docs`.

```system
make html
```

- [Link instructions to install third-party themes](https://sphinx-themes.org/) on the same page as [link to themes](https://www.sphinx-doc.org/en/master/usage/theming.html)

- To install the _Read the docs_ theme do

```system
pip install sphinx_rtd_theme
```

- In the `conf.py` file, make sure to import the theme

```system
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
```

### Sphinx - Setting up other .rst files

- Create a `beforeyoubegin.rst` file in the `source` folder
    - Look at this file for formatting info

- Need to add the `beforeyoubegin.rst` to the toctree, in file `index.rst` so that Sphinx will notice it
    - Spacing is _VERY_ important in reStructured text. Make sure the lines are aligned with the previous line.

- To set a hyperlink, you first need to set a target.

```system
Set hyperlink target (for section or page):
.. _uniquename:
```

- Create hyperlink:

```system
:ref: `hyperlink <uniquename>`
```

- To embed YouTube videos:

```system
.. raw:: html
```

- Go to YouTube video, then go to share then embed video
    - Copy the `<iframe>...</iframe>` code in 
        - **NOTE:** REMEMBER SPACES MATTER
            - Look at `index.rst` for example.

- Example of button, put `|<uniquename>|`
    - Look at the example in the file `beforeyoubegin.rst`

```system
.. |button| image:: /images/button_25x25.png
            :scale: 65 %
```

- Can make warning boxes

```system
.. warning::

   Warning!
```

- Make your own title

```system
.. admonition:: Remember!

   It is important to refer to the documentation to understand how the program is structured.

```

### Setting up autodoc

- Need to uncomment in the `conf.py` file
    - **NOTE:** Add the correct path to python modules `sys.path.insert(0, os.path.abspath('../../'))`

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
```

- The behaviour of sphinx-quickstart appears to have changed since this video was posted (where sphinx==1.6.7). Please see comments for updated fix.**
From user Luke Davoli: "append "--ext-autodoc" when running sphinx-apidoc"
From user  jairo ruiz: In order to make it work in the newest version (2.3.1), you will need to enable autodoc in the Sphinx conf.py file, just add 'sphinx.ext.autodoc' to the extensions list. Then you can run 'sphinx-apidoc' and 'make html' as it is explained in the video.

    - In our case, in the `conf.py` file:

```python
extensions = [
'sphinx.ext.autodoc'
]
```

- Add `modules` in the `toctree` in the `index.rst` file.

```system
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   beforeyoubegin
   modules
```

#### To run

- Go into `source` folder and run

```system
sphinx-apidoc -o . ..
```

- If you want to force generate, meaning to overwrite existing files, add `-f`

```system
sphinx-apidoc -f -o . ..
```

- In this case

```system
sphinx-apidoc -f -o . ../../controller
```

- Then navigate to `docs` folder and run

```system
make html
```

### Fixing Sphinx Warnings and errors

- [Sphinx builder how to fix 'WARNING: Definition list ends without a blank line; unexpected unindent.'](https://gist.github.com/hayderimran7/179e0ca33d7c93429ba7)
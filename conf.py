# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import urllib

external_urls = {
                 "rosinstall": "https://raw.githubusercontent.com/smarc-project/rosinstall/master/README.md",
                 "smarc_docs": "https://raw.githubusercontent.com/smarc-project/smarc_docs/master/README.md",
                 "uavcan_ros_bridge": "https://raw.githubusercontent.com/smarc-project/uavcan_ros_bridge/noetic-devel/README.md",
                 "imc_ros_bridge": "https://raw.githubusercontent.com/smarc-project/imc_ros_bridge/noetic-devel/README.md",
                 "bathymetric_slam": "https://raw.githubusercontent.com/smarc-project/bathymetric_slam/master/README.md",
                 "smarc_stonefish_sims": "https://raw.githubusercontent.com/smarc-project/smarc_stonefish_sims/noetic-devel/README.md",
                 "smarc_controllers": "https://raw.githubusercontent.com/smarc-project/smarc_controllers/noetic-devel/README.md",
                 "smarc_missions": "https://raw.githubusercontent.com/smarc-project/smarc_missions/noetic-devel/README.md",
                 "smarc_utils": "https://raw.githubusercontent.com/smarc-project/smarc_utils/noetic-devel/README.md",
                 "smarc_navigation": "https://raw.githubusercontent.com/smarc-project/smarc_navigation/noetic-devel/README.md",
                 "smarc_msgs": "https://raw.githubusercontent.com/smarc-project/smarc_msgs/noetic-devel/README.md",
                 "smarc_base": "https://raw.githubusercontent.com/smarc-project/smarc_base/noetic-devel/README.md",
                 "sam_webgui": "https://raw.githubusercontent.com/smarc-project/sam_webgui/master/README.md",
                 "sam_common": "https://raw.githubusercontent.com/smarc-project/sam_common/noetic-devel/README.md",
                 "lolo_webgui": "https://raw.githubusercontent.com/smarc-project/lolo_webgui/master/README.md",
                 "lolo_common": "https://raw.githubusercontent.com/smarc-project/lolo_common/noetic-devel/README.md",
                 "roswasm_suite": "https://raw.githubusercontent.com/smarc-project/roswasm_suite/master/README.md",
                 "sbg_ros_driver": "https://raw.githubusercontent.com/smarc-project/sbg_ros_driver/noetic-devel/README.md",
                 "stim300": "https://raw.githubusercontent.com/smarc-project/stim300/noetic-devel/README.md",
                 "stonefish_ros": "https://raw.githubusercontent.com/smarc-project/stonefish_ros/noetic-devel/README.md",
                 "smarc_desktop": "https://raw.githubusercontent.com/smarc-project/smarc_desktop/noetic-devel/README.md",
                 "smarc_base": "https://raw.githubusercontent.com/smarc-project/smarc_base/noetic-devel/README.md",
                 "smarc_releases": "https://raw.githubusercontent.com/smarc-project/smarc_releases/noetic-devel/README.md",
                 "test-ros-release-action": "https://raw.githubusercontent.com/smarc-project/test-ros-release-action/noetic-devel/README.md"

                #  "lolo_common": "https://raw.githubusercontent.com/smarc-project/lolo_common/noetic-devel/README.md",
                #  "sam_common": "https://raw.githubusercontent.com/smarc-project/sam_common/noetic-devel/README.md",
                #  "smarc_releases": "https://raw.githubusercontent.com/smarc-project/smarc_releases/noetic-devel/README.md",
                #  "smarc_desktop": "https://raw.githubusercontent.com/smarc-project/smarc_desktop/noetic-devel/README.md",

                 #  "smarc_simulations": "https://raw.githubusercontent.com/smarc-project/smarc_simulations/master/README.md",
                 #  "roslaunch_monitor": "https://raw.githubusercontent.com/nilsbore/roslaunch_monitor/master/README.md",
                 # "roslaunch_monitor": "https://raw.githubusercontent.com/nilsbore/sam_stonefish_sim/master/README.md"

                 } 

if not os.path.exists("external"):
    os.makedirs("external")
for filename, url in external_urls.items():
    urllib.urlretrieve(url, os.path.join("external", filename+".md"))

# -- Project information -----------------------------------------------------

project = u'smarc_project'
copyright = u'2019, Nils Bore'
author = u'Nils Bore'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u'0.1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosummary',
    'm2r'
]

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
#source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme' #'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'smarc_projectdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'smarc_project.tex', u'smarc-project Documentation',
     u'Nils Bore', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'smarc_project', u'smarc-project Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'smarc_project', u'smarc-project Documentation',
     author, 'smarc_project', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

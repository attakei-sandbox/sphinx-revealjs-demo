# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

# -- Project information -----------------------------------------------------
project = "attakei's slides"
copyright = "2021, Kazuya Takei"
author = "Kazuya Takei"
release = "2021.1"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_revealjs",
    "sphinxemoji.sphinxemoji",
]
templates_path = ["_templates"]
language = "ja"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv"]

# -- Options for HTML output -------------------------------------------------
html_static_path = ["_static"]
html_title = project
html_theme = "alabaster"

# -- Options for REVEALJS output -------------------------------------------------
revealjs_static_path = html_static_path
revealjs_css_files = [
    "revealjs4/plugin/highlight/zenburn.css",
]
revealjs_script_plugins = [
    {
        "name": "RevealHighlight",
        "src": "revealjs4/plugin/highlight/highlight.js",
    },
]
revealjs_script_conf = """
{
    hash: true,
}
"""


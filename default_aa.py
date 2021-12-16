# -*- coding: utf-8 -*-
"""
    pygments.styles.default
    ~~~~~~~~~~~~~~~~~~~~~~~

    The default highlighting style.

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class DefaultStyle(Style):
    """
    The default style (inspired by Emacs 22).
    """

    background_color = "#f8f8f8"
    default_style = ""

    styles = {
        Whitespace:                "#707070",
        Comment:                   "italic #3c7a7a",
        Comment.Preproc:           "noitalic #996500",

        #Keyword:                   "bold #AA22FF",
        Keyword:                   "bold #008000",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold #B00040",

        Operator:                  "#666666",
        Operator.Word:             "bold #AA22FF",

        Name.Builtin:              "#008000",
        Name.Function:             "#0000FF",
        Name.Class:                "bold #0000FF",
        Name.Namespace:            "bold #0000FF",
        Name.Exception:            "bold #d03932",
        Name.Variable:             "#19177C",
        Name.Constant:             "#880000",
        Name.Label:                "#737300",
        Name.Entity:               "bold #727272",
        Name.Attribute:            "#6a7823",
        Name.Tag:                  "bold #008000",
        Name.Decorator:            "#AA22FF",

        String:                    "#BA2121",
        String.Doc:                "italic",
        String.Interpol:           "bold #b15279",
        String.Escape:             "bold #ab5e1e",
        String.Regex:              "#b15279",
        #String.Symbol:             "#B8860B",
        String.Symbol:             "#19177C",
        String.Other:              "#008000",
        Number:                    "#666666",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#8f998f",
        Generic.Error:             "#e60000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #000080",
        Generic.Output:            "#707070",
        Generic.Traceback:         "#0044DD",

        Error:                     "border:#FF0000"
    }

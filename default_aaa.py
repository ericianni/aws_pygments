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
        Whitespace:                "#bbbbbb",
        Comment:                   "italic #2a5c5c",
        Comment.Preproc:           "noitalic #714d00",

        #Keyword:                   "bold #AA22FF",
        Keyword:                   "bold #006200",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold #a6003c",

        Operator:                  "#545454",
        Operator.Word:             "bold #7e00cc",

        Name.Builtin:              "#006200",
        Name.Function:             "#0000FF",
        Name.Class:                "bold #0000FF",
        Name.Namespace:            "bold #0000FF",
        Name.Exception:            "bold #9a2922",
        Name.Variable:             "#19177C",
        Name.Constant:             "#880000",
        Name.Label:                "#555500",
        Name.Entity:               "bold #545454",
        Name.Attribute:            "#4e581b",
        Name.Tag:                  "bold #006200",
        Name.Decorator:            "#7e00cc",

        String:                    "#a21b1b",
        String.Doc:                "italic",
        String.Interpol:           "bold #83395c",
        String.Escape:             "bold #7b4512",
        String.Regex:              "#83395c",
        #String.Symbol:             "#B8860B",
        String.Symbol:             "#19177C",
        String.Other:              "#006200",
        Number:                    "#666666",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#005f00",
        Generic.Error:             "#aa0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #000080",
        Generic.Output:            "#525252",
        Generic.Traceback:         "#0042d8",

        Error:                     "border:#FF0000"
    }

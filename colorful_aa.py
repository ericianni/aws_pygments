# -*- coding: utf-8 -*-
"""
    pygments.styles.colorful
    ~~~~~~~~~~~~~~~~~~~~~~~~

    A colorful style, inspired by CodeRay.

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class ColorfulStyle(Style):
    """
    A colorful style, inspired by CodeRay.
    """

    default_style = ""

    styles = {
        Whitespace:                "#bbbbbb",

        Comment:                   "#767676",
        Comment.Preproc:           "#557799",
        Comment.Special:           "bold #cc0000",

        Keyword:                   "bold #008800",
        Keyword.Pseudo:            "#003388",
        Keyword.Type:              "#333399",

        Operator:                  "#333333",
        Operator.Word:             "bold #000000",

        Name.Builtin:              "#007020",
        Name.Function:             "bold #0066BB",
        Name.Class:                "bold #BB0066",
        Name.Namespace:            "bold #0E7EAB",
        Name.Exception:            "bold #EB0000",
        Name.Variable:             "#996633",
        Name.Variable.Instance:    "#3333BB",
        Name.Variable.Class:       "#336699",
        Name.Variable.Global:      "bold #B55F00",
        Name.Constant:             "bold #003366",
        Name.Label:                "bold #8F6F00",
        Name.Entity:               "bold #880000",
        Name.Attribute:            "#0000CC",
        Name.Tag:                  "#007700",
        Name.Decorator:            "bold #555555",

        String:                    "bg:#fff0f0",
        String.Char:               "#0044DD bg:",
        String.Doc:                "#D54220 bg:",
        String.Interpol:           "bg:#eeeeee",
        String.Escape:             "bold #666666",
        String.Regex:              "bg:#fff0ff #000000",
        String.Symbol:             "#AA6600 bg:",
        String.Other:              "#D82100",

        Number:                    "bold #6600EE",
        Number.Integer:            "bold #0000DD",
        Number.Float:              "bold #6600EE",
        Number.Hex:                "bold #005588",
        Number.Oct:                "bold #4400EE",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#008700",
        Generic.Error:             "#EB0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #BC5909",
        Generic.Output:            "#767676",
        Generic.Traceback:         "#0044DD",

        Error:                     "#A00000 bg:#FFAAAA"
    }

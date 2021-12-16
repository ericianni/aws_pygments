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
        Whitespace:                "#585858", # .w

        Comment:                   "#585858", # .c
        Comment.Preproc:           "#3f5978", # .cp
        Comment.Special:           "bold #b30000", # .cs

        Keyword:                   "bold #006500", # .k
        Keyword.Pseudo:            "#003388", # .kp
        Keyword.Type:              "#333399", # .kt

        Operator:                  "#333333", # .o
        Operator.Word:             "bold #000000", # .ow

        Name.Builtin:              "#00661e", # .nb
        Name.Function:             "bold #0057a2", # .nf
        Name.Class:                "bold #ac005d", # .nc
        Name.Namespace:            "bold #0d5c79", # .nn
        Name.Exception:            "bold #b40000", # .ne
        Name.Variable:             "#754d2a", # .nv
        Name.Variable.Instance:    "#3333BB", # .vi
        Name.Variable.Class:       "#2f5a89", # .vc
        Name.Variable.Global:      "bold #884400", # .vg
        Name.Constant:             "bold #003366", # .no
        Name.Label:                "bold #6c5300", # .nl
        Name.Entity:               "bold #880000", # .ni
        Name.Attribute:            "#0000CC", # .na
        Name.Tag:                  "#006300", # .nt
        Name.Decorator:            "bold #555555", # .nd

        String:                    "bg:#fff0f0", # .s
        String.Char:               "#0044DD bg:", # .sc
        String.Doc:                "#9b3313 bg:", # .sd
        String.Interpol:           "bg:#eeeeee", # .si
        String.Escape:             "bold #515151", # .se
        String.Regex:              "bg:#fff0ff #000000", # .sr
        String.Symbol:             "#7d4b00 bg:", # .ss
        String.Other:              "#a11600", # .sx

        Number:                    "bold #6600EE", # .m
        Number.Integer:            "bold #0000DD", # .mi
        Number.Float:              "bold #6600EE", # .mf
        Number.Hex:                "bold #005588", # .mh
        Number.Oct:                "bold #4400EE", # .mo

        Generic.Heading:           "bold #000080", # .gh
        Generic.Subheading:        "bold #800080", # .gu
        Generic.Deleted:           "#A00000", # .gd
        Generic.Inserted:          "#006400", # .gi
        Generic.Error:             "#b40000", # .gr
        Generic.Emph:              "italic", # .ge
        Generic.Strong:            "bold", # .gs
        Generic.Prompt:            "bold #8a4509", # .gp
        Generic.Output:            "#585858", # .go
        Generic.Traceback:         "#0044DD", # .gt

        Error:                     "#690000 bg:#FFAAAA" # .err
    }

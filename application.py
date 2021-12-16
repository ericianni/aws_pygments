import flask
import os
import sys
import dracula
import default_aa
import default_aaa
import colorful_aa
import colorful_aaa
from pygments import highlight
from pygments.lexers import guess_lexer, get_lexer_by_name
from pygments.formatters import HtmlFormatter

application = flask.Flask(__name__)
application.config["DEBUG"] = True

sys.path.insert(0, os.path.abspath('.'))
# dracula = dracula.DraculaStyle


def make_ecampus_happy(code):
    code = code.replace('<pre style="line-height: 125%">', '<strong><pre style="line-height: 125%>')
    code = code.replace('</pre>', '</pre></strong>')
    return code


def set_style(color, wcag):
    if wcag == 'aa':
        if color == 'default':
            style = default_aa.DefaultStyle
        elif color == 'colorful':
            style = colorful_aa.ColorfulStyle
    elif wcag == 'aaa':
        if color == 'default':
            style = default_aaa.DefaultStyle
        elif color == 'colorful':
            style = colorful_aaa.ColorfulStyle
    else:
        style = color
    return style


def hilite_code(code, language, color, lines, hilite, wcag, bold):
    linenos = "inline" if lines is not None else False
    style = color
    if language == "auto":
        lexer = guess_lexer(code)
    else:
        lexer = get_lexer_by_name(language)
    if wcag == 'none':
        formatter = HtmlFormatter(linenos=linenos, noclasses=True, style=style, hl_lines=hilite)
    else:
        style = set_style(color, wcag)
        
        formatter = HtmlFormatter(linenos=linenos, noclasses=True, style=style, hl_lines=hilite)
    code = highlight(code, lexer, formatter)
    if bold is not None:
        code = make_ecampus_happy(code)
    payload = {'code': code,
               'language': lexer.name}
    return payload


@application.route('/', methods=['GET'])
def home():
    return flask.render_template('pygments_web.html')


@application.route('/', methods=['POST'])
def make_pretty():
    code = flask.request.form.get("code")
    lines = flask.request.form.get("lines")
    hilite = flask.request.form.get("hilite")
    language = flask.request.form.get("language")
    color = flask.request.form.get("color")
    wcag = flask.request.form.get("wcag")
    bold = flask.request.form.get("bold")
    response = flask.make_response(hilite_code(code, language, color, lines, hilite, wcag, bold))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@application.route('/file', methods=['POST'])
def upload_file():
    uploaded_file = flask.request.files['file']
    response = flask.make_response(uploaded_file.read())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    application.run(debug=True)
    # application.run()

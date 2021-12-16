import flask
from pygments import highlight
from pygments.lexers import guess_lexer, get_lexer_by_name
from pygments.formatters import HtmlFormatter

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def hilite_code(code, language, color, lines, hilite):
    linenos = "inline" if lines is not None else False
    style = color
    if language == "auto":
        lexer = guess_lexer(code)
    else:
        lexer = get_lexer_by_name(language)
    if style == 'ecampus':
        formatter = HtmlFormatter(linenos=linenos, noclasses=True, style='default', hl_lines=hilite)
    else:
        formatter = HtmlFormatter(linenos=linenos, noclasses=True, style=style, hl_lines=hilite)
    code = highlight(code, lexer, formatter)
    if style == 'ecampus':
        code = make_ecampus_happy(code)
    payload = {'code': code,
               'language': lexer.name}
    return payload


def make_ecampus_happy(code):
    # Make bold
    code = code.replace('<pre style="line-height: 125%">','<pre style="line-height: 125%"><strong>')
    code = code.replace('</pre>','</strong></pre>')
    # Change colors
    code = code.replace('A0A000', '707000')
    code = code.replace('408080', '427474')
    code = code.replace('008000', '007A00')
    code = code.replace('3C7777', '427474')
    return code


@app.route('/', methods=['GET'])
def home():
    return flask.render_template('pygments_web.html')


@app.route('/', methods=['POST'])
def make_pretty():
    code = flask.request.form.get("code")
    lines = flask.request.form.get("lines")
    hilite = flask.request.form.get("hilite")
    language = flask.request.form.get("language")
    color = flask.request.form.get("color")
    response = flask.make_response(hilite_code(code, language, color, lines, hilite))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/file', methods=['POST'])
def upload_file():
    uploaded_file = flask.request.files['file']
    response = flask.make_response(uploaded_file.read())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)

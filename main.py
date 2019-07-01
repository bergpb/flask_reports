from flask import Flask, render_template
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)


@app.route('/')
def index():
    return "<p>Generate report: <a href='/report'>/report</a></p>"


@app.route('/report')
def generate():
    content = render_template('/template_report.html')
    return render_pdf(HTML(string=content), download_filename='report.pdf')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

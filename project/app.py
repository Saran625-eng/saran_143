from flask import Flask,render_template


flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    dic = {"name":"saran","mobile":345721829}
    return render_template('index.html',context=dic)


@flask_app.route('/about')
def about():
    return render_template('about.html')


@flask_app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    flask_app.run(host='127.0.0.1',
                  port=5007,
                  debug=True)
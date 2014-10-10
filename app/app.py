from flask import Flask, flash, jsonify, render_template, request

app = Flask(__name__)
app.secret_key = '42 is the answer'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name'].strip()
        if len(name) == 0:
            flash(u'Please provide a name', 'danger')
        else:
            flash(u'Welcome {0}'.format(request.form['name']), 'success')
    return render_template('index.html')


@app.route('/api/echo', methods=['POST'])
def api():
    name = request.form['name'].strip()
    if len(name) == 0:
        return jsonify(error=u'Please provide a name')
    else:
        return jsonify(response=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

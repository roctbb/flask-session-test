from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'aodjfiosndcoqwrpvbqprub348990'

@app.route('/')
def index():
    if 'color' in session:
        color = session.get('color')
    else:
        color = 'purple'
    return render_template('index.html', color=color)

@app.route('/set')
def set_color():
    session['color'] = request.args.get('color')
    return redirect('/')

app.run(debug=True)
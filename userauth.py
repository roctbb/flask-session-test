from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'aodjfiosndcoqwrpvbqprub348990'

@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')

    return render_template('auth_index.html')

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('auth_login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return render_template('auth_login.html', error="Заполните все поля!")

    if username == "roctbb" and password == "123456":
        session['username'] = 'roctbb'
        return redirect('/')

    return render_template('auth_login.html', error="Неправильный логин или пароль!")

@app.route('/logout', methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect('/')


app.run(debug=True)
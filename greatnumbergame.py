from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'secret' not in session:
        session['secret'] = random.randrange(1,101)
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    try:
        guess = int(request.form['guess'])
    except:
        return redirect('/')
    secret = session['secret']
    session['guess'] = guess

    if guess < secret:
        result = "Too Low"
    elif guess > secret:
        result = "Too High"
    else:
        result = "You Win"

    session['result'] = result

    return redirect('/')


@app.route('/reset')
def reset():
    session.pop('secret')
    session.pop('result')
    session.pop('guess')

app.run(debug=True)

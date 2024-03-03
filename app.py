from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample questions
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'Madrid', 'Rome', 'Berlin'],
        'answer': 'Paris'
    },
    {
        'question': 'What is 2 + 2?',
        'options': ['3', '4', '5', '6'],
        'answer': '4'
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'options': ['Earth', 'Jupiter', 'Mars', 'Saturn'],
        'answer': 'Jupiter'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('exam'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('exam'))
    return render_template('login.html')

@app.route('/exam')
def exam():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('exam.html', questions=questions)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

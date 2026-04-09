from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# generate random number
secret_number = random.randint(1, 10)

html_page = """
<h2>Number Guessing Game</h2>
<form method="POST">
    Enter a number (1-10): <input name="guess">
    <input type="submit">
</form>
<p>{{ message }}</p>
"""

@app.route('/', methods=['GET', 'POST'])
def game():
    message = ""
    
    if request.method == 'POST':
        guess = int(request.form['guess'])
        
        if guess < secret_number:
            message = "Too low!"
        elif guess > secret_number:
            message = "Too high!"
        else:
            message = "Correct!"
    
    return render_template_string(html_page, message=message)

app.run(host='0.0.0.0', port=5000)
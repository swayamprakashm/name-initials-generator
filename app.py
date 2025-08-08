from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    initials = ''
    if request.method == 'POST':
        full_name = request.form['full_name']
        words = full_name.strip().split()
        initials = '.'.join([word[0].upper() for word in words if word]) + '.'
    return render_template('index.html', initials=initials)

if __name__ == '__main__':
    app.run(debug=True)

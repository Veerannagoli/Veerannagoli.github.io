from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        if not name or not email or not password:
            error = "All fields are required."
            return render_template('registration.html', error=error)
        return render_template('success.html', name=name)
    return render_template('registration.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory database (list of users)
users = []

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        users.append({'name': name, 'email': email})
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = users[user_id]
    if request.method == 'POST':
        user['name'] = request.form['name']
        user['email'] = request.form['email']
        return redirect(url_for('index'))
    return render_template('edit.html', user=user, user_id=user_id)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    users.pop(user_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

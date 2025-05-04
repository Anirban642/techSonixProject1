from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Route setup
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = False
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Save to SQLite
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS messages (name TEXT, email TEXT, message TEXT)")
        c.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()
        
        success = True

    return render_template('contact.html', success=success)

if __name__ == '__main__':
    app.run(debug=True)

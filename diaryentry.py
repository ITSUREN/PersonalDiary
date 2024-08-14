from flask import Flask, request, render_template_string
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'add_entry' in request.form:
            content = request.form['content']
            add_entry(content)
        elif 'delete_date' in request.form:
            date = request.form['date']
            delete_entry(date)
    
    entries = get_all_entries()
    return render_template_string("""
        <h1>Diary</h1>
        
        <!-- Form to add a new entry -->
        <form method="post">
            <h2>Add Entry</h2>
            <textarea name="content" rows="10" cols="50" required></textarea><br>
            <button type="submit" name="add_entry">Add Entry</button>
        </form>
        
        <!-- Form to delete entries by date -->
        <form method="post">
            <h2>Delete Entry by Date</h2>
            <input type="date" name="date" required><br>
            <button type="submit" name="delete_date">Delete Entry</button>
        </form>
        
        <!-- Display all entries -->
        <h2>Diary Entries</h2>
        {% for entry in entries %}
            <p><strong>{{ entry[0] }}</strong><br>{{ entry[1]|safe }}</p>
        {% endfor %}
    """, entries=[(date, content.replace('\n', '<br>')) for date, content in entries])

def add_entry(content):
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('INSERT INTO entries (date, content) VALUES (?, ?)', (date, content))
    conn.commit()
    conn.close()

def delete_entry(date):
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM entries WHERE date LIKE ?', (f'{date}%',))
    conn.commit()
    conn.close()

def get_all_entries():
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('SELECT date, content FROM entries')
    entries = cursor.fetchall()
    conn.close()
    return entries

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


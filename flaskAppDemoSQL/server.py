from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def root():
        return render_template('index.html')

@app.route('/show', methods=['POST'])
def show():
        conn = sqlite3.connect('Company.db')
        option = request.form['option']
        if option == "AS":
                res = conn.execute('select * from People order by FullName ASC')
                res = res.fetchall()
        elif option == 'M':
                res = conn.execute('select * from People where Rank = "Manager" order by FullName ASC')
                res = res.fetchall()
        elif option == 'C':
                res = conn.execute('select * from People where Rank = "Clerk" order by FullName ASC')
                res = res.fetchall()
        elif option == 'A':
                res = conn.execute('select * from People where Rank = "Assistant" order by FullName ASC')
                res = res.fetchall()
        conn.close()
        
        return render_template('show.html', data=res)
        
app.run()
#connect and close database inside routes/functions themselves, never connect and close outside.

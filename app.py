from flask import Flask,render_template,redirect,url_for,request
import mysql.connector as c
import re
a=c.connect(host="localhost",user="root",password="12345678")
x=a.cursor()
x.execute("use apps;")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = request.form.get('username')
        p = request.form.get('password')
        if u=="admin@host.com" and p=="admin1234":
            return redirect(url_for('admin'))
        else:
            if u and p:
                x.execute("SELECT * FROM data WHERE Username=%s AND Password=%s;", (u, p))
                y = x.fetchone()
                
                if y:
                    if y[2] == 1:
                        return render_template('login.html', error="You are a blacklisted user")
                    else:
                        return redirect(url_for('user'))
                else:
                    return render_template('login.html', error="Invalid credentials or user not registered.")
            else:
                return render_template('login.html', error="Please provide both username and password.")
    else:
        return render_template('login.html')

def check(email):
    if(re.fullmatch(regex, email)):
        return 0
    else:
        return 1
        
@app.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method=='POST':
        u = request.form['username']
        p = request.form['password']
        if u and p:
            if check(u)==0:
                if len(p)>=8:
                    x.execute("select * from data where Username=%s",(u,))
                    ex=x.fetchone()
                    if ex:
                        return render_template('register.html',error="Username already exists")
                    else:
                        x.execute("INSERT INTO data VALUES(%s,%s,0)",(u,p))
                        a.commit()
                        return redirect(url_for('login'))
                else:
                    return render_template('register.html',error="Password must be minimum of 8 characters")
            else:
                return render_template('register.html',error="Invalid email")
        else:
            return render_template('register.html',error="Fields cannot be empty")
    else:
        return render_template('register.html')

@app.route('/admin')
def admin():
    x.execute("SELECT * FROM data")
    users = x.fetchall()
    return render_template('admin.html', users=users)
@app.route('/blacklist/<username>')
def blacklist(username):
    x.execute("UPDATE data SET black = 1 WHERE Username = %s", (username,))
    a.commit()
    return redirect(url_for('admin'))
@app.route('/revert/<username>')
def revert(username):
    x.execute("UPDATE data SET black = 0 WHERE username = %s", (username,))
    a.commit() 
    return redirect(url_for('admin'))


@app.route('/user')
def user():
    return render_template('user.html')
    
    
if __name__=='__main__':
    app.run(debug=True)
    
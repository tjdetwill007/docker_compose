from flask import Flask, render_template,request,session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your secret key'

#Route to load index page

#Mysql Connection
mydb = mysql.connector.connect(
  host="mysql",
  user="root",
  password="tjdetwill",
  database="logindb"
)

@app.route('/')
def index():
    return render_template("index.html")

#Route to login Check 
@app.route('/login', methods=['POST','GET'])
def login():
    msg=''
    if request.method == 'POST' and 'userEmail' in request.form and 'password' in request.form:
        try:   
            useremail=request.form['userEmail']
            userpasswd=request.form['password']
            mycursor = mydb.cursor()
            mycursor.execute(
                f"SELECT * FROM accounts WHERE email=\"{useremail}\" AND password=\"{userpasswd}\"")
            account = list(mycursor.fetchone())
            account = dict(zip(list(mycursor.column_names),account))
            print(account)
        except Exception as e:
            account=False
        if account:
        
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return render_template('login.html')
        else:
            msg = 'Incorrect username / password !'
    return render_template('index.html', msg=msg)
#Route to signup
@app.route('/signup', methods=['POST','GET'])
def signup():
    if (request.method and 'userEmail' in request.form and 'password' in request.form and 're-password' in 
    request.form and 'username' in request.form):
        username=request.form['username']
        useremail=request.form['userEmail']
        userpassword=request.form['password']
        user_re_password=request.form['re-password']
        if(userpassword==user_re_password):
            try:
                mycursor = mydb.cursor()
                sql = "INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)"
                val = (username, userpassword,useremail)
                mycursor.execute(sql, val)
                mydb.commit()
                return render_template('index.html',checkbox_checked=True,msg="Signed Up!")
            except Exception as e:
                return render_template('index.html',checkbox_checked=True,msg="User already exists")
        else:
            return render_template('index.html',checkbox_checked=True,msg="Password Missmatch")

        


app.run()
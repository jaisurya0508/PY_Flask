from flask import Flask,render_template,url_for,redirect,request,flash
from flask_mysqldb import MySQL

app=Flask(__name__)
#MYSQL CONNECTION
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="12345"
app.config["MYSQL_DB"]="crud"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)


#Loading Home Page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM users"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html",datas=res)
    
#New User
@app.route("/addUsers",methods=['GET','POST'])
def addusers():
    if request.method=='POST':
       
        name=request.form['name']
        age=request.form['age']
        mail=request.form['mail']
        domain=request.form['domain']
        con=mysql.connection.cursor()
        sql="insert into users(NAME, AGE, MAIL, SPECIALIZATION) Value (%s,%s,%s,%s)"
        con.execute(sql,[name,age,mail,domain])
        mysql.connection.commit()
        con.close()
        flash('User Details Added')        
        return redirect(url_for("home"))
    return render_template("addusers.html")
#update User
@app.route("/editUser/<string:id>",methods=['GET','POST'])

def edituser(id):
    con=mysql.connection.cursor() #connection open
    if request.method=='POST' : 
        name=request.form['name']
        age=request.form['age']
        mail=request.form['mail']
        domain=request.form['domain']
        sql="update users set NAME=%s,AGE=%s,MAIL=%s,SPECIALIZATION=%s where ID=%s"
        con.execute(sql,[name,age,mail,domain])
        mysql.connection.commit()
        con.close()
        flash('User Detail Updated')
        return redirect(url_for("home"))
        con=mysql.connection.cursor()
        
    sql="select * from users where ID=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("edituser.html",datas=res)
#Delete User
@app.route("/deluser/<string:id>",methods=['GET','POST'])

def deleteuser(id):
    con=mysql.connection.cursor() #connection open
    sql="delete from users where ID=%s"
    con.execute(sql,[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for("home"))
if (__name__=='__main__'):
    app.run(debug=True)

if(__name__=='__main__'):
    
    app.run(debug=True)
    app.secret_key="abc12345"
    
  #<link rel="stylesheet" href="{{url_for('static',filename='style.css')}}">
#<link rel="stylesheet" href="{{url_for('static',filename='style.css')}}">




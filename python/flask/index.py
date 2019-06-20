from flask import Flask,redirect, url_for, request, render_template
app=Flask(__name__)


# 1 adding function to route
@app.route('/')
def indexfun():
    return "this is root route"
# 2 adding function to route
@app.route('/hello')
def hellp_world():
    return "Hello World"

#adding a function later
def titanFun():
   return "this is a titan function route added to it later"
app.add_url_rule("/titan", "titan", titanFun)

#passing variables to url path
@app.route('/hello/<name>/')
def hello_people(name):
    return "hello %s" % name

# 1 accepting variables other than string
@app.route('/hello/<int:userId>/')
def hello_empid(userId):
    return "hello %d" % userId

# 2 accepting variables other than string
@app.route('/hello/<float:growth>/')
def hello_growth(growth):
    return "hello %f" % growth

#dynamic url building
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

#using different http methods
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user = request.form['nm']
        return "good for posting " + user
    else :
        user = request.args.get('nm') #getting query params
        return "Cant get though getting " + user   



# 1 returning templates
@app.route('/usertemplates/')
def templater():
   return '<html><body><h1>'+  "Hello World" + '</h1></body></html>'

# 2 returning templates
#passing variable to display in template
@app.route('/partial/<int:marks>')
def partialTemplater(marks):
    return render_template("hello.html", marks=marks)

#2 passing json obj
@app.route('/partial/result/')
def result():
    dict={'physics':80, 'chemistry':90, 'maths':89}
    return render_template("result.html", result= dict)

if __name__=='__main__':
    app.run(debug = True)    
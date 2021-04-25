from flask import Flask,render_template,request,redirect
import os
app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/cabinet")
@app.route('/cabinet',methods=["GET","POST"])
def cabinet():
    if request.method=="GET":
        return render_template('index.html')

    file=request.files.get("file")
    print(os.getcwd())
    path =  "./upload/"
    file_path = path +file.filename
    file.save(file_path)
    return redirect("/cabinet")


if __name__ == '__main__':
    app.run()

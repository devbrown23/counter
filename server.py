from flask import Flask, session, render_template, redirect

app = Flask(__name__)
app.secret_key = "Any string you want"  

@app.route("/")
@app.route('/<down>') 
def index(down = None):
    if "Count" not in session:
        session ["Count"] = 0
    elif down:
        session ['Count'] -= 1
    else:    
        session ["Count"]+=1
    return render_template("index.html")


        

if __name__=="__main__":      
    app.run(debug=True)  
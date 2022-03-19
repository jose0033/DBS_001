import joblib
from flask import Flask, request,render_template
app = Flask(__name__)
@app.route("/", methods = ["GET","POST"])
def index():
  if request.method =="POST":
    rates = request.form.get("rates")
    print(rates)
    model = joblib.load("DBS_Reg")
    pred = model.predict([float[rates]])
    s = "The predicted DBS share price is " + str(pred)
    return(render_template("index.html",results=s))
  else:
    return(render_template("index.html",results="2"))
print("hits")
if __name__ == "__main__":
  app.run()






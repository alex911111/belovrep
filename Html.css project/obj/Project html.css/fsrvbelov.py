from flask import Flask, render_template, request
from test import insert_to_table


app = Flask(__name__)

@app.route("/reg", methods = ["GET","POST"])
def reg():
 if request.method == "POST":
    data = request.form
    insert_to_table(data["Логин"],data["Почта"],data["Пароль"],data["Телефон"])
    return "Спасибо"
 else:
    return render_template("html1(registr).html")



app.run(host = "0.0.0.0", port = "8080", debug=True)
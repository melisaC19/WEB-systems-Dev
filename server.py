from flask import Flask, render_template

app = Flask(__name__)

product = {
    '1': "Mouse",
    '2': "Keyboard",
    '3': "Monitor"   
}

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/product/<id>")
def product(id):
    if id in product:
        return render_template("product.html", id=id, name=product[id])
    else:
        return "product not found"
    
@app.route("/login")
def login():
    return render_template("login.html")
           
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/register")
def register():
    return render_template("register.html")

from flask import Flask, render_template
from pymongo import MongoClient
from forms import login, regForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "PER ASPERA AD ASTRA"


client = MongoClient(
        "mongodb://rchatbots:dexterous4221@rchatbots0-shard-00-00.rkfzl.mongodb.net:27017,"
        "rchatbots0-shard-00-01.rkfzl.mongodb.net:27017,rchatbots0-shard-00-02.rkfzl.mongodb.net:27017/"
        "myFirstDatabase?ssl=true&replicaSet=atlas-5yvpk9-shard-0&authSource=admin&retryWrites=true&w=majority"
    )
db = client["testDatabase"]
users = db["users"]
orders = db["orders"]
closed_orders = db["closedOrders"]
products = db["products"]


@app.route("/")
def index():

    total_users = users.count_documents({})
    total_orders = orders.count_documents({})
    total_closedOrders = closed_orders.count_documents({})

    return render_template("index.html",
                           activeOrders = total_orders,
                           closedOrders=total_closedOrders,
                           users=total_users)


@app.route("/users")
def usersPage():
    users1 = users.find({})
    users_list = []

    for x in users1:
        users_dict = {}
        users_dict["id"] = x["senderID"]
        users_dict["phone"] = x["phone"]
        users_dict["age"] = x["userage"]
        print(users_dict)
        users_list.append(users_dict)
        print(users_list)
            
    return render_template("users.html", users_list=users_list)


@app.route("/orders")
def ordersPage():
    orders1 = orders.find({})
    orders_list = []

    for x in orders1:
        users_dict = {}
        users_dict["id"] = x["senderID"]
        users_dict["products"] = x["products"]
        print(users_dict)
        orders_list.append(users_dict)
        print(orders_list)
    return render_template("orders.html", orders_list=orders_list)


@app.route("/sales")
def salesPage():

    return render_template("sales.html")


@app.route("/closedOrders")
def closedOrdersPage():
    orders1 = closed_orders.find({})
    orders_list = []

    for x in orders1:
        users_dict = {}
        users_dict["id"] = x["senderID"]
        users_dict["products"] = x["products"]
        print(users_dict)
        orders_list.append(users_dict)
        print(orders_list)
    return render_template("closedOrders.html", orders_list=orders_list)


@app.route("/login.html")
def loginPage():

    # create the form instance to be used on our login page
    form = login()
    return render_template("login.html", form=form)

@app.route("/reg.html")
def regPage():
    form = regForm()
    return render_template("reg.html", form=form)

if __name__=='__main__':
    app.run(debug=True)
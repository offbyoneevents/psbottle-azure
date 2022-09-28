import os

from bottle import Bottle, request, redirect, template, response

from pymongo import MongoClient

from pygecko.crypto_prices import simple_single_price

mongo_routes = Bottle()

client = MongoClient(os.environ["MONGO_CONNECTION_STRING"])
db = client.crypto_tracker
portfolios = db.portfolios
users = db.users

def _user_logged_in():
    return request.cookies.current_user != ""

def _check_login():
    if not _user_logged_in():
        redirect("/mongo/login")

@mongo_routes.get("/mongo")
def mongo_index():
    if _user_logged_in():
        redirect("/mongo/portfolio")
    return template("mongo/index")

@mongo_routes.get("/mongo/login")
@mongo_routes.post("/mongo/login")
def mongo_login():
    if request.method == "POST":
        username = request.forms["username"]
        password = request.forms["password"]
        user = users.find_one({"username": username})
        if user is None or user["password"] != password:
            redirect("/mongo/login")
        response.set_cookie("current_user", username)
        redirect("/mongo/portfolio")
    return template("mongo/login")

@mongo_routes.get("/mongo/register")
@mongo_routes.post("/mongo/register")
def mongo_register():
    if request.method == "POST":
        username = request.forms["username"]
        password = request.forms["password"]
        password2 = request.forms["password2"]

        if users.find_one({"username": username}) is not None or password != password2:
            redirect("/mongo/register")

        users.insert_one({"username": username, "password": password})
        redirect("/mongo/login")
    return template("mongo/register")

@mongo_routes.get("/mongo/logout")
def mongo_logout():
    if request.cookies.current_user:
        response.delete_cookie("current_user")
    redirect("/mongo")

@mongo_routes.get("/mongo/portfolio")
def mongo_portfolio():
    _check_login()
    portfolio = portfolios.find_one({"username": request.cookies.current_user})
    investments = [
        {
            "coin_id": coin_id,
            "value": simple_single_price(coin_id, "usd") * quantity
        } for coin_id, quantity in portfolio["investments"].items()
    ]
    return template("mongo/portfolio", investments=investments, current_user=request.cookies.current_user)

@mongo_routes.get("/mongo/buy")
@mongo_routes.post("/mongo/buy")
def mongo_buy():
    _check_login()
    if request.method == "POST":
        coin_id = request.forms["coin_id"]
        quantity = float(request.forms["quantity"])
        portfolio = portfolios.find_one({"username": request.cookies.current_user})
        if coin_id in portfolio["investments"]:
            portfolio["investments"][coin_id] += quantity
        else:
            portfolio["investments"][coin_id] = quantity
        portfolios.replace_one({"username": request.cookies.current_user}, portfolio)
        redirect("/mongo/portfolio")
    return template("mongo/buy", current_user=request.cookies.current_user)

@mongo_routes.get("/mongo/sell")
@mongo_routes.post("/mongo/sell")
def mongo_sell():
    _check_login()
    portfolio = portfolios.find_one({"username": request.cookies.current_user})
    if request.method == "POST":
        coin_id = request.forms["coin_id"]
        quantity = float(request.forms["quantity"])
        portfolio["investments"][coin_id] -= quantity
        if portfolio["investments"][coin_id] <= 0:
            del portfolio["investments"][coin_id]
        portfolios.replace_one({"username": request.cookies.current_user}, portfolio)
        redirect("/mongo/portfolio")
    owned_coins = sorted(list(portfolio["investments"].keys()))
    return template("mongo/sell", owned_coins=owned_coins, current_user=request.cookies.current_user)

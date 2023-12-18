from sanic import Blueprint, Request
from sanic.response import redirect
from sanic_ext import openapi

bp = Blueprint(name="myblueprint")

list_of_userdetails = []


@bp.route("/")
@openapi.summary("This is the homepage endpoint")
@openapi.description("This endpoint displays the homepage")
async def homepage(request):
    return redirect("http://127.0.0.1:5500/index.html")


@bp.route("/signin", methods=['POST'])
@openapi.summary("This is the SignIn endpoint")
@openapi.description(
    "It accepts a post request, get's the value or data from a form input and saves the value or data into a database")
async def hello_world(request: Request):
    if request.method == 'POST':
        username = request.form.get('username')
        for names in username:
            names.split(",")
            list_of_userdetails.append(names)
        print(list_of_userdetails)
        return redirect("/qchat")


@bp.route("/qchat")
@openapi.summary("This is the chat application endpoint")
@openapi.description("Redirects user to the chat application page")
async def qchat(request):
    return redirect("http://127.0.0.1:5500/chat.html")

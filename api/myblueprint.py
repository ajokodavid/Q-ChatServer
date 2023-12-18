from sanic import Blueprint, Request
from sanic.response import redirect

bp = Blueprint(name="myblueprint")

list_of_userdetails = []


@bp.route("/")
async def homepage(request):
    return redirect("http://127.0.0.1:5500/index.html")


@bp.route("/signin", methods=['POST'])
async def hello_world(request: Request):
    if request.method == 'POST':
        username = request.form.get('username')
        for names in username:
            names.split(",")
            list_of_userdetails.append(names)
        print(list_of_userdetails)
        return redirect("/qchat")


@bp.route("/qchat")
async def qchat(request):
    return redirect("http://127.0.0.1:5500/chat.html")

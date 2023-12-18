# import asyncio

import socketio
from sanic import Sanic
from sanic_ext import Extend

from api.myblueprint import bp

app = Sanic(__name__)
app.config.CORS_ORGINS = "*"
Extend(app)
sio = socketio.AsyncServer(async_mode="sanic", cors_allowed_origins="*", logger=True)
sio.attach(app)
app.blueprint(bp)


@sio.on(event="connect", namespace="/chat")
async def chat(sid, data):
    print("Connected")


@sio.on(event="disconnect", namespace="/chat")
async def disconnected_user(sid, msg):
    print("disconnected")


@sio.on(event="hello", namespace="/chat")
async def get_msg(sid, msg):
    print(f"Message: from {sid}:{msg}")
    await sio.emit(event="take", data=msg)


if __name__ == "__main__":
    app.run(auto_reload=True, fast=True, debug=False, access_log=False, single_process=False)

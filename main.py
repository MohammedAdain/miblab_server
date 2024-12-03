
from typing import Union

from fastapi import FastAPI, Request

from datetime import datetime

from math import pi, sin

app = FastAPI()

position = {}

scale = 3


@app.get("/")
def read_root():

    return {"Hello": "World"}



@app.get("/items/{item_id}")

def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}


def get_x_coordinate():
    # x = sin(2*pi*(datetime.now().timestamp()%10))
    x = position["x"]
    print(f"x: {x}")
    return x

def get_y_coordinate():
    # y = datetime.now().timestamp()%10
    y = position["y"] * scale
    print(f"y: {y}")
    return y

def get_z_coordinate():
    # z = datetime.now().timestamp()%10
    # z = 5.7
    z = position["z"]
    print(f"z: {z}")
    return z

@app.get("/getPosition")
def read_root():
    # print(f'{"x": str(get_x_coordinate()),"y": str(get_y_coordinate()),"z": str(get_z_coordinate())}')
    return {
        "x": get_x_coordinate(),
        "y": get_y_coordinate(),
        "z": get_z_coordinate()
    }

@app.post("/postPosition")
async def post_position(request: Request):
    global position
    body = await request.json()
    # print(body)
    position = body
    return {"received": body}

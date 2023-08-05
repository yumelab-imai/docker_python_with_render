# for FastAPI
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def index():
#     return {"Hello": "World"}


# for Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return jsonify({"Hello": "World"})

if __name__ == "__main__":
    app.run()
from flask import Flask

app = Flask("test")

@app.route("/")
def index():
  return ("test")


app.run(host="0.0.0.0", port=3904)

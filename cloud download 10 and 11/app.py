from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<div style='background-color:yellow'><marquee><h1>Hello people this is shubham this side!</h1></marquee></div>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

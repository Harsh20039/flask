from flask import Flask

app = Flask(__name__)

@app.route('/')
def simple():
    return "Hello, Azure Web Apps!"
 
if __name__ == '__main__':
    app.run(debug=True)
    
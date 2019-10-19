# Before running the application, you need to set an env varibale that you want to be the flask application
# In terminal, run ---> export FLASK_APP = basic_flask_rest_api.py
# To run deg mode (so you don't have to refresh connection on every change) run ---> export FLASK_DEBUG=1

from flask import Flask, render_template, jsonify, request

# __name__ is so Flask knows where to look for templates and static files
app = Flask(__name__)

posts = [
    {
        'author': 'Alan Tong',
        'title': 'Blog post 1',
        'comment': 'First blog post',
        'date': '20 January 2019'
    },
    {
        'author': 'Ben Tomkins',
        'title': 'Blog post 2',
        'comment': 'Second blog post',
        'date': '21 January 2019'
    }
]


# You can add keys to the html template to pass props to be accessed and rendered on the webpage
@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def index():
    if request.method == 'POST':
        some_json = request.get_json()
        return jsonify({'you_sent': some_json}), 201
    else:
        return jsonify({'about': 'home'})


@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({'result': num * 10})


# @app.route('/about')
# def about():
#     return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

# curl -H "Content-Type: application/json" -X POST -d '{"name":"xyz", "address":"address xyz"}'

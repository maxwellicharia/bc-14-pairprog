import pyrebase

config = {
  "apiKey": "AIzaSyAfOOxETfH1E3Tv7_6wsFevjG0ijDMyXWI",
  "authDomain": "pairprog-d067f.firebaseapp.com",
  "databaseURL": "https://pairprog-d067f.firebaseio.com/",
  "storageBucket": "gs://pairprog-d067f.appspot.com",
  "serviceAccount": "Pairprog-cb2ee89dd605.json"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

#authenticate a user

user = auth.sign_in_with_email_and_password("maxwellicharia.com", "mySuperStrongPassword")

# Was to implement pyrebase
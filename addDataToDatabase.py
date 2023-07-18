import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://faceattendancerealtime-73b72-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "167234" :
        {
            "name" : "Anirudh Chakravarty K",
            "major" : "Computer Science",
            "starting_year" : 2019,
            "total_attendance" : 7,
            "standing" : "G",
            "year" : 4,
            "lase_attendance_time" : "2022-12-11 00:54:34"
        },
    "321654" :
        {
            "name" : "Murtaza Hassan",
            "major" : "Robotics",
            "starting_year" : 2017,
            "total_attendance" : 6,
            "standing" : "G",
            "year" : 3,
            "lase_attendance_time" : "2022-12-10 03:54:34"
        },
    "432675" :
        {
            "name" : "Ben Affleck",
            "major" : "Acting",
            "starting_year" : 2016,
            "total_attendance" : 8,
            "standing" : "G",
            "year" : 3,
            "lase_attendance_time" : "2022-11-11 00:54:34"
        },

    "963852" :
        {
            "name" : "Elon Musk",
            "major" : "Physics",
            "starting_year" : 2020,
            "total_attendance" : 7,
            "standing" : "G",
            "year" : 1,
            "lase_attendance_time" : "2023-12-11 00:54:34"
        },
    "534671" :
        {
            "name" : "Margot Robbie",
            "major" : "Acting",
            "starting_year" : 2018,
            "total_attendance" : 3,
            "standing" : "G",
            "year" : 4,
            "lase_attendance_time" : "2022-10-11 05:54:34"
        },
    "852741" :
        {
            "name" : "Emly Blunt",
            "major" : "Economics",
            "starting_year" : 2021,
            "total_attendance" : 12,
            "standing" : "B",
            "year" : 1,
            "lase_attendance_time" : "2021-12-11 00:54:34"
        },

}

for key,value in data.items():
    ref.child(key).set(value)
import firebase_admin
from firebase_admin import credentials, db
import datetime


class FirebaseStream:
    key, path, type, pathD, data, child = str, str, str, str, str, str

    @staticmethod
    def initialize_app(path: str, database_url: str):
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': database_url
        })

    def __init__(self, path: str, debug: bool = True) -> object:
        self.path = path
        self.debug = debug
        ref = db.reference(path)
        self.request_count = 0
        self.stream = ref.listen(self.listener)

    def listener(self, event):
        self.request_count += 1
        if self.request_count != 1 and "last_updated" not in event.data:  # "Updated" when starts
            print("REQUEST INDEX: {}".format(self.request_count))
            now = str(datetime.datetime.now())
            self.type = (event.event_type.upper())  # can be 'put' or 'patch'
            self.pathD = event.path  # relative to the reference, it seems
            self.data = event.data  # new data at /reference/event.path. None if deleted
            self.child = db.reference(self.path + event.path.rsplit('/', 1)[0]).get()
            self.key = (event.path.split('/', 2)[1])

            if self.debug:
                db.reference(self.path + event.path.rsplit('/', 1)[0]).update({
                    "last_updated": now
                })
                print({
                    "type": self.type,
                    "path": self.pathD,
                    "data": self.data,
                    "child": self.child,
                    "key": self.key
                })

    def get_path(self):
        return self.pathD

    def get_type(self):
        return self.type

    def get_key(self):
        return self.key

    def get_data(self):
        return self.data


FirebaseStream.initialize_app("serviceAccountKey.json", "https://adminhbeg.firebaseio.com/")
stream = FirebaseStream("blogs/")

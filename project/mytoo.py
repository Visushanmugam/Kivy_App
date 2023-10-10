from kivy.app import App
from jnius import autoclass, cast, PythonJavaClass, java_method

PythonActivity = autoclass('org.kivy.android.PythonActivity')
currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
context = cast('android.content.Context', currentActivity.getApplicationContext())

Firebase = autoclass('com.google.firebase.FirebaseApp')

FirebaseFirestore = autoclass('com.google.firebase.storage.FirebaseStorage')

HashMap = autoclass('java.util.HashMap')

Firebase.initializeApp(context)

instance = FirebaseFirestore.getInstance()

APP_INSTANCE = App.get_running_app()

# Writing

def Write_data():
    instance.download('Administrator/first.jpg', 'first.jpg')


def read_data():
    task = instance.collection("weather").document("today").get()
    task.addOnSuccessListener(TodaySuccessListenr())

class TodaySuccessListenr(PythonJavaClass):
    __javainterfaces__= ['com/google/android/gms/tasks/OnSuccessListener']

    __javacontext__= "app"

    @java_method('(Ljava/lang/Object;)V')
    def onSuccess(doc):
        data = doc.getData()
        for key in data.keyset():
            APP_INSTANCE.weather_data[key] = data.get(key)

lis = None

def listen_data():
    global lis
    tasklive = instance.collection("weather").document("today").get()
    if lis is None:
        lis = tasklive.addSnapshotListener(TodaySnapshotListenr())

def remove_listen_data():
    global lis
    if lis is not None:
        lis.remove()

class TodaySnapshotListenr(PythonJavaClass):
    __javainterfaces__= ['com/google/firebase/firestore/EventListener']

    __javacontext__= "app"

    @java_method('(Ljava/lang/Object;Lcom/google/firebase/firestore/FirebaseFirestoreException;)V')
    def onEvent(self, doc, error):
        try:
            data = doc.getData()
            for key in data.keyset():
                APP_INSTANCE.weather_data[key] = data.get(key)
        except Exception as e:
            print(e)
            


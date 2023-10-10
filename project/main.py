
from kivymd.app import MDApp
from kivy.core.window import WindowBase
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from multiprocessing.dummy import Process
from time import sleep
import webbrowser
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.list import OneLineIconListItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDTextButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivy.properties import DictProperty
import json
from twilio.rest import Client
from pyrebase import pyrebase
import firebase_admin
import numpy
import requests



Window.keyboard_anim_args = {'d':.2,'t':'in_out_expo'}
Window.softinput_mode = "below_target"

class Manager(MDScreenManager):
    pass


class Imagestart(MDScreen):
    pass


class Login(MDScreen):
    pass


class Password(MDScreen):
    pass


class Signup1(MDScreen):
    pass


class Signup2(MDScreen):
    pass


class Signup3(MDScreen):
    pass


class Otpverify(MDScreen):
    pass


class Appscren(MDScreen):
    pass


class Bookingpage(MDScreen):
    pass


class CustomOneLineIconListItemtest(OneLineIconListItem):
    text = StringProperty()


class Viewreport(MDScreen):
    pass


class History(MDScreen):
    pass


class Bookingteststatus(MDScreen):
    pass


class Profile(MDScreen):
    pass


class Costomize(MDScreen):
    pass


class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 33


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 33


class Chatbot(MDScreen):
    pass


class Reportanissue(MDScreen):
    pass


class Faq(MDScreen):
    pass


class Termsandcondition(MDScreen):
    pass


class Editprofile(MDScreen):
    pass

config = {
  "apiKey": "AIzaSyBcjERWF0ZGfPAuaNxlCMeFA4wlMtLG3CY",
  "authDomain": "android-kivyapp-c32f8.firebaseapp.com",
  "projectId": "android-kivyapp-c32f8",
  "storageBucket": "android-kivyapp-c32f8.appspot.com",
  "messagingSenderId": "507352190111",
  "appId": "1:507352190111:web:014b7a910ab9a4ee4866aa",
  "measurementId": "G-WMX81B165N",
  "databaseURL": "https://android-kivyapp-c32f8.appspot.com",
  "serviceAccount": "key.json",
}


class BalaLab(MDApp):
    title = "Bala Lab" 
    icon = "Logo_Final.jpg"
    weather_data = DictProperty(rebind=True)
    def build(self):
        self.theme_cls.material_style = "M3"
        self.login_url = "https://android-kivyapp-c32f8-default-rtdb.firebaseio.com/.json"
        self.strng = Builder.load_file("main.kv")
        return self.strng
    
    def on_start(self):
        Process(target=self.load_image).start()
        Clock.schedule_interval(self.carousel_auto_scroll, 5)

    def load_image(self):
        sleep(2)
        self.store = JsonStore("user_data.json")
        try:
            img = ["first.jpg", "secound.jpg", "third.jpg"]
            for i in img:
                self.firebase = pyrebase.initialize_app(config)
                self.storage = self.firebase.storage()
                self.storage.download(f"Administrator/{i}", i)
        except:
            pass
        #try:
        #    self.cred = firebase_admin.credentials.Certificate("./key.json")
        #    self.stro = firebase_admin.initialize_app(self.cred, {'storageBucket':'fireapp-53cfa.appspot.com'})
        #    img = ["first.jpg", "secound.jpg", "third.jpg"]
        #    for i in img:          
        #        buck = bucket()
        #        blob = buck.get_blob(f'Administrator/{i}')
        #        arr = numpy.frombuffer(blob.download_as_string(), numpy.uint8)
        #        fi = open(f'assets/{i}', 'wb')
        #        fi.write(arr)
        #        fi.close()
        #except:
        #    pass
        try:
            if self.store.get('userInfo')['Phone'] != "":
                auth = "oZqcaCdK4nBsj12P2TfuG909gQYEHxcpA8FcJbHe"
                r = requests.get(self.login_url+'?auth'+auth)
                data = r.json()
                phones = set()
                for key,value in data.items():
                    phones.add(key)
                if self.store.get('userInfo')['Phone'] in phones:
                    if self.store.get('userInfo')['Password'] == data[self.store.get('userInfo')['Phone']]["Password"]:
                        self.data_value_set()
                        self.root.current = "appscreen"
            else:
                self.root.current = "login"
        except:
            self.root.current = "login"

    def data_value_set(self):
        self.strng.get_screen('appscreen').ids.titlename.title = f"Hi, {self.store.get('userInfo')['Name']}"
        self.strng.get_screen('profile').ids.name_profile.text = self.store.get('userInfo')["Name"]
        self.strng.get_screen('profile').ids.mail_profile.text = self.store.get('userInfo')["Mail"]
        self.strng.get_screen('profile').ids.phone_profile.text = self.store.get('userInfo')['Phone']
        self.strng.get_screen('profile').ids.gender_profile.text = self.store.get('userInfo')["Gender"]
        self.strng.get_screen('profile').ids.brith_profile.text =  self.store.get('userInfo')["Dateofbrith"]  
        self.strng.get_screen('appscreen').ids.nav_details.title = self.store.get('userInfo')["Name"]
        self.strng.get_screen('appscreen').ids.nav_details.text = self.store.get('userInfo')['Phone']

    def user_login(self):
        #self.cred = firebase_admin.credentials.Certificate("./key.json")
        #self.stro = firebase_admin.initialize_app(self.cred, {'storageBucket':'android-kivyapp-c32f8.appspot.com'})
        #img = ["first.jpg", "secound.jpg", "third.jpg"]
        #for i in img:          
        #    buck = storage.bucket()
        #    blob = buck.get_blob(f'Administrator/{i}')
        #    arr = numpy.frombuffer(blob.download_as_string(), numpy.uint8)
        #    fi = open(i, 'wb')
        #    fi.write(arr)
        #    fi.close()
        try:
            auth = "vOsdRbirqNi3h1Kfg0rWLJ6c96dguMfF67AlO2Ht"
            r = requests.get(self.login_url+'?auth'+auth)
            data = r.json()
            phones = set()
            for key,value in data.items():
                phones.add(key)
            if self.strng.get_screen('login').ids.phone_login.text in phones:
                if self.strng.get_screen('login').ids.password_login.text == data[self.strng.get_screen('login').ids.phone_login.text]["Password"]:
                    self.store.put('userInfo', Phone=str(self.strng.get_screen('login').ids.phone_login.text), Password=str(data[self.strng.get_screen('login').ids.phone_login.text]['Password']), Name=str(data[self.strng.get_screen('login').ids.phone_login.text]['Name']), Gender=str(data[self.strng.get_screen('login').ids.phone_login.text]['Gender']), Mail=str(data[self.strng.get_screen('login').ids.phone_login.text]['Mail']), Dateofbrith=str(data[self.strng.get_screen('login').ids.phone_login.text]['Dateofbrith']))
                    self.data_value_set()
                    self.root.transition.direction = 'left'
                    self.root.current = "appscreen"
                else:
                    self.strng.get_screen('login').ids.password_login.text =  ""
                    self.strng.get_screen('login').ids.password_login.helper_text =  "Incorrect password"
                    self.strng.get_screen('login').ids.password_login.line_color_normal =  "red"
                    self.strng.get_screen('login').ids.password_login.hint_text_color_normal =  "red"
            else:
                self.strng.get_screen('login').ids.phone_login.text =  ""
                self.strng.get_screen('login').ids.password_login.text =  ""
                self.no_account_dialog()
        except:
            self.strng.get_screen('login').ids.phone_login.text =  ""
            self.strng.get_screen('login').ids.password_login.text =  ""
    
    def register_account(self):
        signupname = str(self.strng.get_screen('signup1').ids.name_signup.text)
        signupgender = ""
        if f"{self.strng.get_screen('signup1').ids.male.md_bg_color}" == "[0.38823529411764707, 0.42745098039215684, 0.7764705882352941, 1.0]":
            signupgender = "Male"
        elif f"{self.strng.get_screen('signup1').ids.female.md_bg_color}" == "[0.38823529411764707, 0.42745098039215684, 0.7764705882352941, 1.0]":
            signupgender = "Female"
        elif f"{self.strng.get_screen('signup1').ids.male_female.md_bg_color}" == "[0.38823529411764707, 0.42745098039215684, 0.7764705882352941, 1.0]":
            signupgender = "Others"
        signupage = str(self.strng.get_screen('signup2').ids.brith_signup.text)
        signupphone = str(self.strng.get_screen('signup3').ids.phone_signup.text)
        signupmail = str(self.strng.get_screen('signup3').ids.mail_signup.text)
        signuppassword = str(self.strng.get_screen('signup3').ids.password_signup.text)
        if str(self.strng.get_screen('otpverify').ids.otp_signup.text) == "123":
            info = str({f'\"{signupphone}\":{{"Name":\"{signupname}\","Gender":\"{signupgender}\","Dateofbrith":\"{signupage}\","Mail":\"{signupmail}\","Password":\"{signuppassword}\"}}'})
            info = info.replace("\'","")
            to_database = json.loads(info)
            requests.patch(url = self.login_url, json=to_database)
            self.root.current = "login"
        else:
            self.strng.get_screen('create').ids.otp_signup.helper_text = "Otp is invalid"

    def carousel_auto_scroll(self, o):
        self.strng.get_screen('appscreen').ids.caro.load_next(mode='next')

    def back_screen(self):
        self.root.current = "appscreen"
        self.root.transition.direction = 'right'
        self.strng.get_screen('appscreen').ids.main_manage.switch_tab("home")   

    def replay(self, *args):
        if self.strng.get_screen('chatbot').ids.client_send.text == "Hello" or self.strng.get_screen('chatbot').ids.client_send.text == "hello":
            val = "Hello. I'm your helping chatbot"
        elif self.strng.get_screen('chatbot').ids.client_send.text == "1" or self.strng.get_screen('chatbot').ids.client_send.text == "Couldn't do it booking test":
            val = "Please restart your app.\n If not resolve contact 9597287503"
        elif self.strng.get_screen('chatbot').ids.client_send.text == "2" or self.strng.get_screen('chatbot').ids.client_send.text == "Couldn't do it view reports":
            val = "Please restart your app.\n If not resolve contact 9597287503"
        elif self.strng.get_screen('chatbot').ids.client_send.text == "3" or self.strng.get_screen('chatbot').ids.client_send.text == "Couldn't do it test status":
            val = "Please restart your app.\n If not resolve contact 9597287503"
        else:
            val = "Sorry, Don't understand\n\n You try to say following options.\n\n1. Couldn't do it booking test\n2. Couldn't do it view reports\n3. Couldn't do it test status"
        self.strng.get_screen('chatbot').ids.chat_message.add_widget(Response(text=val, size_hint_x=.77, halign="center"))

    def send_message(self):
        global size, halign, val
        if self.strng.get_screen('chatbot').ids.client_send.text != "":
            val = self.strng.get_screen('chatbot').ids.client_send.text
            if len(val) < 6:
                size = .22
                halign = "center"
            elif len(val) < 11:
                size = .32
                halign = "center"
            elif len(val) < 16:
                size = .45
                halign = "center"
            elif len(val) < 21:
                size = .58
                halign = "center"
            elif len(val) < 26:
                size = .72
                halign = "center"
            else:
                size = .77
                halign = "left"
            self.strng.get_screen('chatbot').ids.chat_message.add_widget(Command(text=val, size_hint_x=size, halign=halign))
            self.replay()
            self.strng.get_screen('chatbot').ids.client_send.text = ""

    def dialog_logout_app(self):
        logout_cancel = MDFlatButton(text='cancel', on_release= self.cancel_logout_dialog)
        meual_btn_logout = MDFlatButton(text='ok', on_release= self.logout_app)
        self.dialog_logout = MDDialog(title='Logout', text="Logout for this device", size_hint=(0.7, 0.2), buttons=[logout_cancel,meual_btn_logout])
        self.dialog_logout.open()

    def cancel_logout_dialog(self, op):
        self.strng.get_screen('appscreen').ids.nav_drawer.set_state("close")
        self.dialog_logout.dismiss()

    def logout_app(self, op):
        self.strng.get_screen('login').ids.phone_login.text = ""
        self.strng.get_screen('login').ids.password_login.text = ""
        self.root.transition.direction = 'right'
        self.root.current = "login"
        self.strng.get_screen('appscreen').ids.nav_drawer.set_state("close")
        self.store.delete("userInfo")
        self.dialog_logout.dismiss()

    def test_info(self, scren):
        self.root.current = f"{scren}"
        self.root.transition.direction = 'left'
        self.strng.get_screen('appscreen').ids.nav_drawer.set_state("close")

    def gender_test(self, value):
        if "male" == value:
            self.strng.get_screen('bookingpage').ids.female.md_bg_color = "ffffff"
            self.strng.get_screen('bookingpage').ids.male.md_bg_color = "636dc6"
            self.strng.get_screen('bookingpage').ids.male_female.md_bg_color = "ffffff"
        elif "female" == value:
            self.strng.get_screen('bookingpage').ids.female.md_bg_color = "636dc6"
            self.strng.get_screen('bookingpage').ids.male.md_bg_color = "ffffff"
            self.strng.get_screen('bookingpage').ids.male_female.md_bg_color = "ffffff"
        elif "male_female"== value:
            self.strng.get_screen('bookingpage').ids.female.md_bg_color = "ffffff"
            self.strng.get_screen('bookingpage').ids.male.md_bg_color = "ffffff"
            self.strng.get_screen('bookingpage').ids.male_female.md_bg_color = "636dc6"

    def gender_re(self, value):
        if "male" == value:
            self.strng.get_screen('bookingpage').ids.female.md_bg_color = "ffffff"
            self.strng.get_screen('bookingpage').ids.male.md_bg_color = "636dc6"
            self.strng.get_screen('bookingpage').ids.male_female.md_bg_color = "ffffff"
        elif "female" == value:
            self.strng.get_screen('bookingpage').ids.female.md_bg_color = "636dc6"
            self.strng.get_screen('bookingpage').ids.male.md_bg_color = "ffffff"
            self.strng.get_screen('bookingpage').ids.male_female.md_bg_color = "ffffff"
        elif "male_female"== value:
            self.strng.get_screen('bookingpage').ids.female.md_bg_color = "ffffff"
            self.strng.get_screen('bookingpage').ids.male.md_bg_color = "ffffff"
            self.strng.get_screen('bookingpage').ids.male_female.md_bg_color = "636dc6"


    def gender_edit(self, value):
        if "male" == value:
            self.strng.get_screen('editprofile').ids.female.md_bg_color = "ffffff"
            self.strng.get_screen('editprofile').ids.male.md_bg_color = "636dc6"
            self.strng.get_screen('editprofile').ids.male_female.md_bg_color = "ffffff"
        elif "female" == value:
            self.strng.get_screen('editprofile').ids.female.md_bg_color = "636dc6"
            self.strng.get_screen('editprofile').ids.male.md_bg_color = "ffffff"
            self.strng.get_screen('editprofile').ids.male_female.md_bg_color = "ffffff"
        elif "male_female"== value:
            self.strng.get_screen('editprofile').ids.female.md_bg_color = "ffffff"
            self.strng.get_screen('editprofile').ids.male.md_bg_color = "ffffff"
            self.strng.get_screen('editprofile').ids.male_female.md_bg_color = "636dc6"


    def add_icon_item(self, name_icon):
        self.strng.get_screen('bookingpage').ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItemtest",
                    "id":name_icon,
                    "text": name_icon,
                    "on_release": lambda x=name_icon: self.select_testname(x),
                }
            )
    def set_list_md_icons(self, text="", search=False):
        self.strng.get_screen('bookingpage').ids.rv.data = []
        testdata = ["SUGAR (F,PP)", "SUGAR (R)", "SUGAR (CBG)", "BLOOD GROUPING", "HAEMOGLOBIN (HB)", "CBC", "BLEEDING TIME CLOTTING TIME", "ESR", "AEC (Absolute Eosinophil Count )", "HBA1C", "BLOOD PIPICTURE (Peripheral smear)", "BLOOD PARASITES MP, BLOOD PARASITES MF", "PLASMA PROTHROMBIN TIME (PTINR)", "BLOOD UREA", "S. CREATININE", "S.URIC ACID", "S.CALCIUM", "S.PHOSPHORUS", "TOTAL CHOLESTEROL", "TRYGLYCERIDES", "LIPID PROFILE", "ELECTROLYTES", "S.SODIUM", "S.POTTASIUM", "S.BIOCORBANATE", "S.CHLORIDE", "LIVER FUNTION TEST", "S.BILLIRUBIN", "S.ALBUMIN", "SGOT", "SGPT", "S.AMYLASE,LYPASE", "RENAL FUNTION TEST", "WIDAL", "CRP", "TPHA", "HIV", "HBsAG", "ANTI HCV", "DEMGUE IgM & IgG", "ASO", "RA FACTOR", "VDRL", "RTPCR (COVID 19 )", "MALARIAL CARD", "PREGNENCY CARD", "MANTOUX", "URINE CULTURE ( MANNUAL)", "GCT", "STOOL ROUTINE", "STOOL OCCULT BLOOD", "THYROID FUNTION TEST (T3.T4,TSH,FT3,FT4 )", "T3,T4,TSH", "TSH", "LH,FSH,PROLACTINE", "ANTI CCP", "LDH (LACTATE DEHYDROGENASE )", "D-DIMER", "FERRTIN", "VITAMIN B12", "VITAMIN D3", "TOTAL IgE", "VITAMIN D", "FREE TESTOSTERAN", "CA125", "PROGESTERON", "B-HCG", "LH", "FSH", "SEMEN ANALYSIS", "SEMEN ANALYSIS - CASA", "URINE CULTURE (AUTOMACHINE)", "DENGUE (RTPCR)", "RTPCR (COVID 19) EMERGENCY", "STOOL C/S", "URINE COMPLETE EXAMINATION", "URINE ROUTINE EXAMINATION", "URINE PILESALT, PILEPIGMENTS"]
        for name_icon in testdata:
            if search:
                if text in name_icon:
                    self.add_icon_item(name_icon)
            else:
                self.add_icon_item(name_icon)
    
    def select_testname(self, data):
        self.strng.get_screen('bookingpage').ids.search_field.text = data
        self.strng.get_screen('bookingpage').ids.rv.data = []

    def colse_search(self):
        if self.strng.get_screen('bookingpage').ids.search_field.focus == False:
            self.strng.get_screen('bookingpage').ids.rv.data = []
        elif self.strng.get_screen('bookingpage').ids.search_field.focus == True:
            self.set_list_md_icons("", True)
 
    def profile_change_home(self):
        self.strng.get_screen('appscreen').ids.nav_drawer.set_state("close")
        self.root.transition.direction = 'left'
        self.root.current = "profile"

    def nav_close(self):
        self.strng.get_screen('appscreen').ids.nav_drawer.set_state("close")

    def open_map(self):
        webbrowser.open_new_tab("https://www.google.co.in/maps/@12.1617281,78.2248267,14z?entry=ttu")

    def change_theme(self):
        pass

    def active(self):
        self.strng.get_screen('profile').ids.field.disabled = False

    def go_test_info(self):
        webbrowser.open_new_tab("https://firebasestorage.googleapis.com/v0/b/fireapp-53cfa.appspot.com/o/Administrator%2FPRIZE.pdf?alt=media&token=3f404e2f-ad9f-4784-bbdb-afcbd180f422")


if __name__ == "__main__":
    BalaLab().run()


__version__ = "1.11.0"
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.uix.boxlayout import BoxLayout

kvfile = Builder.load_string('''
#:kivy 1.11.0
<MainMenu>:
    name: "main"
    string: string

    FloatLayout:
#        background_color : (0.5, 0.7, 0.5, 1.0)
        Label:
            text:"Search"
            font_size: (root.width**2 + root.height**2) / 13**4
            pos_hint: {"x":0.1, "top":0.9}
            size_hint: 0.35, 0.15


        TextInput:
            id: string
            font_size: (root.width**2 + root.height**2) / 13**4
            multiline: False
            pos_hint: {"x": 0.45 , "top":0.9}
            size_hint: 0.4, 0.15

        Button:
            pos_hint:{"x":0.2,"y":0.5}
            size_hint: 0.6, 0.1
            font_size: (root.width**2 + root.height**2) / 13**4
            text: "Search"
            on_press:
                root.manager.transition.direction = "up"
                root.search()

        Button:
            pos_hint:{"x":0.2,"y":0.30}
            size_hint: 0.6, 0.1
            font_size: (root.width**2 + root.height**2) / 13**4
            text: "Add"
            on_press:
                root.manager.transition.direction = "left"
                root.addbtn()

        Button:
            pos_hint:{"x":0.2,"y":0.1}
            size_hint: 0.6, 0.1
            font_size: (root.width**2 + root.height**2) / 13**4
            text: "Delete"
            on_press:
                root.manager.transition.direction = "left"
                root.delbtn()

<AddElement>
    name: "add"
    namee:namee
    types:types
    location:location

    FloatLayout:
        Label:
            text:"Add Your Product"
            pos_hint:{"top":1, "x": 0.22}
            size_hint:0.6, 0.1
            font_size: (root.width**1 + root.height**2.16) / 12.5**4
            color:0.9, 0.2, 0.3, 1.0
        Label:
            text:"Name: "
            pos_hint:{"x":0.01, "y":0.76}
            size_hint:0.6, 0.1
            font_size: (root.width**1 + root.height**2.16) / 14**4
            color:0.3, 0.6, 0.9, 1.0
        TextInput:
            id: namee
            font_size: (root.width**1 + root.height**2.16) / 14**4
            multiline: False
            pos_hint: {"x": 0.45 , "top":0.9}
            size_hint: 0.4, 0.15
        Label:
            text:"Group: "
            pos_hint:{"x":0.01, "y":0.56}
            size_hint:0.6, 0.1
            font_size: (root.width**1 + root.height**2.16) / 14**4
            color:0.3, 0.6, 0.9, 1.0
        TextInput:
            id: types
            font_size: (root.width**1 + root.height**2.16) / 14**4
            multiline: False
            pos_hint: {"x": 0.45 , "top":0.7}
            size_hint: 0.4, 0.15
        Label:
            text:"Location: "
            pos_hint:{"x":0.01, "y":0.36}
            size_hint:0.6, 0.1
            font_size: (root.width**1 + root.height**2.16) / 14**4
            color:0.3, 0.6, 0.9, 1.0
        TextInput:
            id: location
            font_size: (root.width**1 + root.height**2.16) / 14**4
            multiline: True
            pos_hint: {"x": 0.45 , "top":0.5}
            size_hint: 0.4, 0.15

        Button:
            pos_hint:{"center_x":0.50, "center_y":0.13}
            size_hint: 0.6, 0.1
            font_size: (root.width**2 + root.height**2) / 14**4
            text: "MainMenu"
            on_press:
                app.root.current = "main"
                root.manager.transition.direction = "down"
        Button:
            text:"Add"
            size_hint:0.6,0.1
            font_size: (root.width**2 + root.height**2) / 14**4
            pos_hint:{"center_x":0.50, "center_y":0.25}
            background_color: 0.6, 0.6, 0.6
            on_press:
                root.manager.transition.direction = "up"
                root.submit()




<DeleteElement>
    name: 'del'
#    number:number
    del_data:del_data


    BoxLayout:

        orientation:"vertical"
        size_hint:1,0.7
        FloatLayout:
            Label:
                text:"Search"
                font_size: (root.width**2 + root.height**2) / 13**4
                pos_hint: {"x":0.1, "top":0.9}
                size_hint: 0.35, 0.15

            TextInput:
                id: del_data
                font_size: (root.width**2 + root.height**2) / 15**4
                multiline: False
                pos_hint: {"x": 0.45 , "top":0.9}
                size_hint: 0.4, 0.15

            Button:
                size_hint:0.35,0.25
                font_size: (root.width**2 + root.height**2) / 15**4
                pos_hint:{"center_x":0.5, "center_y":0.2}
                text: 'Search'
                on_press:
                    root.del_el_btn()
                    app.root.current = "seldel"
                    root.manager.transition.direction = "right"


        FloatLayout:
            Button:
                size_hint:0.35,0.25
                pos_hint:{"center_x":0.5, "center_y":0.2}
                font_size: (root.width**2 + root.height**2) / 15**4
                text: 'Delete All'
                on_press:
                    root.del_ev_btn()
                    root.manager.transition.direction = "down"
            Button:
                text:"Main Menu"
                size_hint:0.35,0.25
                pos_hint:{"center_x":0.50, "center_y":0.55}
                font_size: (root.width**2 + root.height**2) / 15**4
                background_color: 0.6, 0.6, 0.6
                on_press:
                    root.manager.transition.direction = "down"
                    app.root.current = "main"

<DeleteSelected>:
    name:"seldel"
    product:product
    types:types
    location:location

    number:number


    BoxLayout:
        orientation: 'vertical'
        size_hint:1, 0.8
        pos_hint:{"x":0.1, "y":0.1}





        ScrollView:
            size_hint: 1.2,2.9
            pos_hint:{"x":-0.20}
            GridLayout:
                size_hint: 1.0,None
                height: self.minimum_height
                cols: 4
                Label:
                    id:product

                    font_size:(root.width**1 + root.height**2.16) / 16**4
                    size_hint_x:1
                    size_hint_y:None

                    height: self.texture_size[1]
                    multiline:True


                Label:
                    id:location
                    font_size:(root.width**1 + root.height**2.16) / 16**4
                    size_hint_x:1
                    size_hint_y:None

                    height: self.texture_size[1]
                    multiline:True
                Label:
                    id:types

                    font_size:(root.width**1 + root.height**2.16) / 16**4
#                    font_size:(root.width**2 + root.height**2) / 16**4
                    size_hint_x:1
                    size_hint_y:None

                    height: self.texture_size[1]
                    multiline:True


        FloatLayout:
            size_hint: 1.0,1.29
            Label:
                text:"Enter Number To Delete :"
                font_size: (root.width**1 + root.height**2.16) / 16**4
                size_hint:0.25,0.35
                pos_hint:{"center_x":0.28, "center_y":0.70}
                color: 1.0,0.0,0.0,1.0


            TextInput:
#                size_hint:0.065,0.225
                id:number
                size_hint:(None, None)
                height:30
                width:50
#                text: str(root.value)
#                on_text_validate:
#                    root.value = int(self.text)
                pos_hint:{"center_x":0.53, "center_y":0.70}

                font_size: (root.width**2 + root.height**2) / 16**4
                color:1.0,0.1,0.1,1.0
#                background_color: 0.1,0.8,0.8,0.8
#                opacity:0.2


                multiline:False


            Button:
#                height:dp(30)
                text:"Submit"
                size_hint:0.65,0.255
                font_size:(root.width**1 + root.height**2.16) / 15**4
                pos_hint:{"center_x":0.40, "y":0.29}
                background_color: 0.6, 0.6, 0.6
                on_press:
                    root.manager.transition.direction = "down"
                    root.del_sel_el()
                    app.root.current = "main"

            Button:
#                height:dp(30)

                text:"Main Menu"
                size_hint:0.65,0.225
                font_size:(root.width**1 + root.height**2.16) / 15**4
                pos_hint:{"center_x":0.40, "center_y":0.12}
                background_color: 0.6, 0.6, 0.6
                on_press:
                    app.root.current = "main"
                    root.manager.transition.direction = "down"

            Button:
                text:"Back"
                size_hint:0.65,0.225
#                height:dp(30)
                font_size:(root.width**1 + root.height**2.16) / 15**4
                pos_hint:{"center_x":0.40, "center_y":-0.15}
                background_color: 0.6, 0.6, 0.6
                on_press:
                    app.root.current = "del"
                    root.manager.transition.direction = "right"












<SearchOut>:
    name: "out"

    product:product
    types:types
    location:location


    FloatLayout:
        Label:
            bold: True
            color: (1, .8, .2, 1)
            font_size: (root.width**1 + root.height**2.16) / 14**4
            text:"Product"
            pos_hint:{"x": -0.21, "top": 1.031}
            size_hint: 0.8,0.2
        Label:
            bold: True
            color: (1, .8, .2, 1)
            font_size: (root.width**1 + root.height**2.16) / 14**4
            text:"Location"
            pos_hint:{"x": 0.14, "top": 1.031}
            size_hint: 0.8,0.2
        Label:
            bold: True
            color: (1, .8, .2, 1)
            font_size: (root.width**1 + root.height**2.16) / 14**4
            text:"Group"
            pos_hint:{"x": 0.45, "top": 1.031}
            size_hint: 0.8,0.2



        ScrollView:
            size_hint: 1.0,0.7
            pos_hint:{"x":0.0, "y":0.15}
            GridLayout:
                size_hint: 1.0,None
                height: self.minimum_height
                cols: 4
                Label:
                    id:product

                    font_size:(root.width**1 + root.height**2.16) / 16**4
                    size_hint_x:2.0
                    size_hint_y:None

                    height: self.texture_size[1]
                    multiline:True
                Label:
                    id:location
                    font_size:(root.width**1 + root.height**2.16) / 16**4
                    size_hint_x:1.8
                    size_hint_y:None

                    height: self.texture_size[1]
                    multiline:True
                Label:
                    id:types

                    font_size:(root.width**1 + root.height**2.16) / 16**4
#                    font_size:(root.width**2 + root.height**2) / 16**4
                    size_hint_x:1.5
                    size_hint_y:None

                    height: self.texture_size[1]
                    multiline:True



        Button:
            size_hint:0.65,0.085
            font_size: (root.width**2 + root.height**2) / 15**4
            pos_hint:{"center_x":0.50, "center_y":0.08}
            text: "Back"
            on_press:
                app.root.current = "main"
                root.manager.transition.direction = "down"
''')

class MainMenu(Screen):
    string = ObjectProperty(None)

    def search(self):
        a = db.get_data(self.string.text)
        # print (a)
        if a:
            # for aq in a:
                SearchOut.current = self.string.text
                self.reset()
                sm.current = "out"

        else:
            invalidForm()
            self.reset()

    def reset(self):
        self.string.text = ""


    def addbtn(self):
        # print("hello")
        sm.current = "add"

    def delbtn(self):
        sm.current = "del"


class SearchOut(Screen):

    product = ObjectProperty(None)
    types = ObjectProperty(None)
    location = ObjectProperty(None)

    current = ""
    out = None
    def on_enter(self, *args):
        self.out = db.get_data(self.current)
        # self.data.text = "".join(f'{n+1}. {el[0]}{el[1]}{el[2]}{el[3]}\n' for n,el in enumerate(out))
        self.product.text = "".join(f'{n+1}. {el[0]}\n\n' for n, el in enumerate(self.out))
        self.types.text = "".join(f' {el[1]}\n\n' for n, el in enumerate(self.out))
        self.location.text = "".join(f'{el[2]}\n\n' for n, el in enumerate(self.out))



class AddElement(Screen):
    namee = ObjectProperty(None)
    types = ObjectProperty(None)
    location = ObjectProperty(None)
    def reset(self):
        self.namee.text = ""
        self.types.text = ""
        self.location.text = ""
    def submit(self):
        db.add_data(self.namee.text, self.types.text, self.location.text)
        SubmitForm()
        self.reset()
        sm.current = "main"


class DeleteElement(Screen, BoxLayout):

    del_data = ObjectProperty(None)

    def on_enter(self, *args):
        self.reset()
        # pass
    def del_ev_btn(self):
        db.delete_everything()
        all_deleted()
        sm.current = "main"

    def del_el_btn(self):
        a = db.get_data(self.del_data.text)
        # print (a)
        if a:
            # for aq in a:
            DeleteSelected.current = self.del_data.text
            self.reset()
            sm.current = "seldel"

        else:
            invalidForm()
            self.reset()

    def reset(self):
        self.del_data.text = ""


class DeleteSelected(Screen):

    product = ObjectProperty(None)
    types = ObjectProperty(None)
    location = ObjectProperty(None)
    number = ObjectProperty(None)
    current = ""

    out = None

    def on_enter(self, *args):
        # print(DeleteElement.del_data)
        self.out = db.get_data(self.current)
        if self.out:
            # self.recv_data.text = "".join(f'{n+1}. {el[0]}{el[1]}{el[2]}{el[3]}\n' for n, el in enumerate(out))
            self.product.text = "".join(f'{n + 1}.  {el[0]}\n\n' for n, el in enumerate(self.out))
            self.types.text = "".join(f' {el[1]}\n\n' for n, el in enumerate(self.out))
            self.location.text = "".join(f'{el[2]}\n\n' for n, el in enumerate(self.out))


        else:
            invalidForm()

            sm.current = "main"

    def del_sel_el(self):
        print("Hello")
        sel_del_data = self.out
        sel_del_data = "".join(f'{el[0]};{el[0]};{el[1]};{el[2]};{el[3]}|' for n, el in enumerate(sel_del_data))
        sel_del_data = sel_del_data.split('|')
        r = self.number.text
        r = int(r.lower()) - 1
        if r < 1:
            invalidForm()
        else:
            db.delete_Product(sel_del_data[r])
            deleted()
            sm.current = "main"


class WindowManager(ScreenManager):
    pass


def invalidForm():
    pop = Popup(title='Invalid Form', content=Label(text='No Item Found With This Name'), size_hint=(None, None), size=(400, 400))

    pop.open()


def SubmitForm():
    pop = Popup(title='Details Added',
                  content=Label(text='All Details about the Products is Saved'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


def all_deleted():
    pop = Popup(title='Products Deleted', content=Label(text='All Products are Deleted'), size_hint=(None, None), size=(400, 400))

    pop.open()


def deleted():
    pop = Popup(title='Products Deleted', content=Label(text='Selected Product Deleted'), size_hint=(None, None), size=(400, 400))

    pop.open()




# KV = Builder.load_file("main.txt")
sm = WindowManager()

db = DataBase("user.txt")
screens = [MainMenu(name="main"), AddElement(name="add"), SearchOut(name="out"), DeleteElement(name="del"), DeleteSelected(name='seldel')]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()

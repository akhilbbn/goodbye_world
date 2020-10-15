import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image, AsyncImage
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside=GridLayout()
        self.inside.cols=3

        self.add_widget(Label(text="Select Your Choice "))


        self.hi = Button(text="Industry Setup", font_size=40)
        self.hi.bind(on_press=self.hii)
        self.inside.add_widget(self.hi)
        
        self.bye = Button(text="Cinema", font_size=40)
        self.bye.bind(on_press=self.byee)
        self.inside.add_widget(self.bye)

        self.hey = Button(text="Warehouse",font_size=40)
        self.hey.bind(on_press=self.heyy)
        self.inside.add_widget(self.hey)

        self.sub = Button(text="Complex",font_size=40)
        self.sub.bind(on_press=self.subb)
        self.inside.add_widget(self.sub)

        self.submi = Button(text="Office",font_size=40)
        self.submi.bind(on_press=self.submit)
        self.inside.add_widget(self.submi)

        self.su = Button(text="Institution",font_size=40)
        self.su.bind(on_press=self.susu)
        self.inside.add_widget(self.su)

        self.add_widget(self.inside)

        

    def hii(self, obj):
        info = f"You have selected Industry Setup"

        loca_minor.info_page.update_info(info)
        
        loca_minor.screen_manager.current = "Info"

    def byee(self, obj):
        info = f"hello world"
        loca_minor.info_page.update_info(info)
        
        loca_minor.screen_manager.current = "Info"
        
    def subb(self, obj):
        info = f"hello world"
        loca_minor.info_page.update_info(info)
        
        loca_minor.screen_manager.current = "Info"


       

    def susu(self, obj):
        info = f"hello world"
        loca_minor.info_page.update_info(info)
        
        
        loca_minor.screen_manager.current = "Info"
   
        
    def submit(self, obj):
        info = f"hello world"
        loca_minor.info_page.update_info(info)
        
        loca_minor.screen_manager.current = "Info"
    def heyy(self, obj):
        info = f"hello world"
        loca_minor.info_page.update_info(info)
        
        loca_minor.screen_manager.current = "Info"
      

        

class InfoPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1
        self.message = Label(halign="center",valign="middle",font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)


class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        self.mygrid=MyGrid()
        screen=Screen(name="Loca")
        screen.add_widget(self.mygrid)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen=Screen(name="Info")
        screen.add_widget(self.info_page)
        
        self.screen_manager.add_widget(screen)

        
        return self.screen_manager


if __name__=="__main__":
    loca_minor = MyApp()
    loca_minor.run()


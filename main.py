import pyautogui
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from KivyOnTop import register_topmost
from kivy.config import Config
from pynput import keyboard

Window.size = (400,200)


class Panel(FloatLayout):

	slider = ObjectProperty(None)
	btn = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(Panel, self).__init__(**kwargs)
		Panel.create_listener(self)
		self.on = False

	def activate_autoclicker(self):
		self.slider.disabled = True
		pyautogui.PAUSE = 1 / self.slider.value
		Clock.schedule_interval(self.click, 0.001)

	def stop_autoclicker(self):
		self.slider.disabled = False
		Clock.unschedule(self.click)

	def change_button(self):
		print("sono stato cliccato.")
		if self.on:
			self.btn.background_color = (.157, .455, .753, 1)
			self.btn.text = "START"
			self.stop_autoclicker()
		else:
			self.btn.background_color = (1, .4, 0, 1)
			self.btn.text = "STOP"
			self.activate_autoclicker()		
		self.on = not self.on

	def click(self, *args):
		pyautogui.click()

	def on_release(self, key, *args):
		if keyboard.Key.f4 in args:
			self.change_button()

	def create_listener(self):
		listener = keyboard.Listener(
	    	on_release=lambda key, *args: self.on_release(self, key, *args)
	    )
		listener.start()


kv = Builder.load_file("kv.kv")


class MyApp(App):
	App.title = "AutoClicker"
	def build(self):
		return kv
	def on_start(self, *args):
		Window.set_title("ULTRA CLICKER")
		register_topmost(Window, "ULTRA CLICKER")


if __name__ == "__main__":
	MyApp().run()
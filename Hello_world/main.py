import kivy
kivy.require('2.3.1') # replace with your current kivy version !

from kivy.app import App

from kivy.uix.label import Label
# One important thing to note here is the way packages/classes are laid out. 
# The uix module is the section that holds the user interface elements like layouts and widgets.



class MyApp(App):
    """
    It’s required that the base Class of your App inherits from the App class. 
    It’s present in the kivy_installation_dir/kivy/app.py.
    Kivy is based on Python and uses Sphinx for documentation, so the documentation for each class is in the actual file.
    """
    
    def build(self):
        """
        this is the function where you should initialize and return your Root Widget.
        """

        # Here we initialize a Label with text ‘Hello World’ and return its instance. 
        # This Label will be the Root Widget of this App.
        return Label(text='Hello world')


if __name__ == '__main__':
    # Here the class MyApp is initialized and its run() method called. 
    # This initializes and starts our Kivy application.
    MyApp().run()

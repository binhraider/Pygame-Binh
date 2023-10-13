from framework.framework import *
from src.states.menu import Menu
from src.states.setting import Setting

app = Application()
app.init_state(Menu())
app.run()


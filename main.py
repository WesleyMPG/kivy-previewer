from os.path import dirname, sep
from kivy import require
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from functools import partial

KV_FILE = dirname(__file__) + sep + 'code.kv'

try:
  with open(KV_FILE, 'r') as arq:
    pass
except (FileNotFoundError):
  with open(KV_FILE, 'w') as arq:
    pass


Window.size = (650, 710)

class RootWidget(FloatLayout):
  pass


root = Builder.load_string("""
<RootWidget>:
  size_hint: 1, 1

  FloatLayout:
    id: preview
    size_hint: 1, 1
    pos_hint: {'x': 0, 'y': 0}

  BoxLayout:
    size_hint: 1, .01
    pos_hint: {'x': 0, 'y': 0}

    Splitter:
      id: h_split
      sizable_from: 'top'
      min_size: 0
    
      TextInput:
        id: output
        disabled: True


RootWidget:
""")


def replace_with_updated(root, update):
  root.ids['preview'].clear_widgets()
  Builder.unload_file('cod.kv')
  child = Builder.load_string(update, filename='cod.kv')
  root.ids['preview'].add_widget(child)
  root.ids['output'].text = ''


old_state = ''
def add_dinamyc(root, *idk):
  global old_state
  try:
    with open(KV_FILE, 'r') as arq:
      readed = str(arq.read())
    if readed != old_state:
      old_state = readed
      replace_with_updated(root, readed)
  except Exception as exc:
    root.ids['output'].text = str(exc)


class TesteApp(App):
  def build(self):
    global root
    root.size[0] = Window.size[0]
    Clock.schedule_interval(partial(add_dinamyc, root), 1)
    return root


if __name__ == '__main__':
  TesteApp().run()
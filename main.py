from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder


class MainWidget(GridLayout):
    board = [['bc', 'bh', 'br', 'bq', 'bk', 'br', 'bh', 'bc'],
             ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
             ['nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl'],
             ['nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl'],
             ['nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl'],
             ['nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl'],
             ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
             ['wc', 'wh', 'wr', 'wq', 'wk', 'wr', 'wh', 'wc']]
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if (i+j) % 2 == 0:
                    b = Button(background_color="green", text = self.board[i][j])
                    self.add_widget(b)
                else:
                    b = Button(background_color="white",  text = self.board[i][j])
                    self.add_widget(b)
                    

class ChessGame(App):
    def build(self):
        Builder.load_file("./visual.kv")
        return MainWidget()

ChessGame().run()

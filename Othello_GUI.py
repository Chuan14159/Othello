# Changchuan Shen 83371717. Lab assignment 5. Lab sec 14.

from Othello_GameLogic import *
import tkinter



DEFAULT_FONT = ('Helvetica', 11)

class Window_info:

    def __init__(self):        
        self._dialog_window = tkinter.Tk()
        self._dialog_window.title('SETTINGS')
        
        self.row = tkinter.IntVar()
        self.column = tkinter.IntVar()
        self.firstturn = tkinter.IntVar()
        self.topleft = tkinter.IntVar()
        self.winning = tkinter.StringVar()
        self.row.set(4)
        self.column.set(4)
        self.firstturn.set(BLACK)
        self.topleft.set(BLACK)
        self.winning.set('>')
        self.game = False
        
        self._title = tkinter.Label(
            master = self._dialog_window, text = 'FULL', font = DEFAULT_FONT)
        self._title.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = tkinter.W + tkinter.N)

        self._row = tkinter.Label(
            master = self._dialog_window, text = 'ROW', font = DEFAULT_FONT)
        self._row.grid(
            row = 1, column = 0, columnspan = 2, padx = 20, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.S)

        self._rowenter = tkinter.Scale(
            master = self._dialog_window, from_ = 4, to = 16, resolution = 2, orient = tkinter.HORIZONTAL, variable = self.row)
        self._rowenter.grid(
            row = 2, column = 0, columnspan = 2, padx = 20, pady = 0, sticky = tkinter.W + tkinter.N + tkinter.E)

        self._column = tkinter.Label(
            master = self._dialog_window, text = 'COLUMN', font = DEFAULT_FONT)
        self._column.grid(
            row = 3, column = 0, columnspan = 2, padx = 20, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.S)

        self._columnenter = tkinter.Scale(
            master = self._dialog_window, from_ = 4, to = 16, resolution = 2, orient = tkinter.HORIZONTAL, variable = self.column)
        self._columnenter.grid(
            row = 4, column = 0, columnspan = 2, padx = 20, pady = 0, sticky = tkinter.W + tkinter.N + tkinter.E)

        self._firstturn = tkinter.Label(
            master = self._dialog_window, text = 'FIRST TURN', font = DEFAULT_FONT)
        self._firstturn.grid(
                row = 5, column = 0, columnspan = 2, padx = 20, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.S)
        self._blackturn = tkinter.Radiobutton(
            variable = self.firstturn, text = 'BLACK', value = BLACK).grid(
                row = 6, column = 0, padx = 20, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.N)
        self._whiteturn = tkinter.Radiobutton(
            variable = self.firstturn, text = 'WHITE', value = WHITE).grid(
                row = 6, column = 1, padx = 20, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.N)

        self._topleft = tkinter.Label(
            master = self._dialog_window, text = 'TOP-LEFT COLOR', font = DEFAULT_FONT)
        self._topleft.grid(
                row = 7, column = 0, columnspan = 2, padx = 20, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.S)
        self._blacktopleft = tkinter.Radiobutton(
            variable = self.topleft, text = 'BLACK', value = BLACK).grid(
                row = 8, column = 0, padx = 20, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.N)
        self._whitetopleft = tkinter.Radiobutton(
            variable = self.topleft, text = 'WHITE', value = WHITE).grid(
                row = 8, column = 1, padx = 20, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.N)

        self._winning = tkinter.Label(
            master = self._dialog_window, text = 'RULE', font = DEFAULT_FONT)
        self._winning.grid(
                row = 9, column = 0, columnspan = 2, padx = 20, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.S)
        self._high = tkinter.Radiobutton(
            variable = self.winning, text = 'More Discs Win', value = '>').grid(
                row = 10, column = 0, padx = 20, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.N)
        self._low = tkinter.Radiobutton(
            variable = self.winning, text = 'Fewer Discs Win', value = '<').grid(
                row = 10, column = 1, padx = 20, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.N)

        self._ok_button = tkinter.Button(
            master = self._dialog_window, text = 'OK', font = DEFAULT_FONT, command = self._on_ok_button)
        self._ok_button.grid(
                row = 11, column = 0, padx = 30, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.S)
            
        self._cancel_button = tkinter.Button(
            master = self._dialog_window, text = 'CANCEL', font = DEFAULT_FONT, command = self._on_cancel_button)
        self._cancel_button.grid(
                row = 11, column = 1, padx = 30, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.S)

        
        for row in range(11):
            self._dialog_window.rowconfigure(row, weight = 1)
            
        self._dialog_window.columnconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._dialog_window.mainloop()

    def _on_ok_button(self):
        '''takes all the parameters and distroy the window.'''
        self.row = self.row.get()
        self.column = self.column.get()
        self.firstturn = self.firstturn.get()
        self.topleft = self.topleft.get()
        self.winning = self.winning.get()
        self._dialog_window.destroy()
        self.game = True

    def _on_cancel_button(self):
        '''simply close the window'''
        self._dialog_window.destroy()



class Window_game:

    def __init__(self, info):
        self._info = info
        self._game = Gamestate(info.row, info.column, info.firstturn)
        self._game.gamestart(info.topleft)
        
        self._game_window = tkinter.Tk()
        self._game_window.title('OTHELLO')

        self._game_window.protocol('WM_DELETE_WINDOW', self._on_close_click)

        self.valid = 'PLEASE MOVE'
        self.turn = self._game.printturn()

        self._canvas = tkinter.Canvas(
            master = self._game_window, width = info.column * 40, height = 40 * info.row, background = 'light blue')
        self._canvas.grid(
                row = 1, column = 0, rowspan = 2, padx = 10, pady = 10,
                sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        self._back_button = tkinter.Button(
            master = self._game_window, text = 'BACK', font = DEFAULT_FONT, command = self._on_back_button)
        self._back_button.grid(
            row = 3, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E + tkinter.S)

        self._reset_button = tkinter.Button(
            master = self._game_window, text = 'RESTART', font = DEFAULT_FONT, command = self._on_reset_button)
        self._reset_button.grid(
            row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E + tkinter.S)

        self._on_board_redraw()

        self._game_window.rowconfigure(0, weight = 1)
        self._game_window.columnconfigure(0, weight = 10)
        self._game_window.rowconfigure(1, weight = 10)
        self._game_window.columnconfigure(1, weight = 1)
        self._game_window.rowconfigure(2, weight = 10)
        self._game_window.rowconfigure(3, weight = 1)
        
        self._game_window.mainloop()

    def _on_close_click(self):
        '''keep the window open if the game is not end'''
        try:
            if self._game.gameover():
                self._game_window.destroy()
            else:
                if tkinter.messagebox.askokcancel("Quit?", "Game is not over. Are you sure you want to quit?"):
                    self._game_window.destroy()
        except:
            self._game_window.destroy()
        

    def _on_reset_button(self):
        '''restart the game'''
        try:
            if self._game.gameover():
                self._game_window.destroy()
                self = Window_game(self._info)
            else:
                if tkinter.messagebox.askokcancel("Restart?", "Game is not over. Are you sure you want to restart?"):
                    self._game_window.destroy()
                    self = Window_game(self._info)
        except:
            self._game_window.destroy()
            self = Window_game(self._info)
    
    def _on_back_button(self):
        '''go back to setting menu and destroy the game window.'''
        try:
            if self._game.gameover():
                self._game_window.destroy()
                self._restart = Window_info()
                if self._restart.game:
                    self = Window_game(self._restart)
            else:
                if tkinter.messagebox.askokcancel("Quit?", "Game is not over. Are you sure you want to quit?"):
                    self._game_window.destroy()
                    self._restart = Window_info()
                    if self._restart.game:
                        self = Window_game(self._restart)
        except:
            self._game_window.destroy()
            self._restart = Window_info()
            if self._restart.game:
                self = Window_game(self._restart)
        
    def _on_canvas_resized(self, event):
        '''redraw the canvas when the size of the window changes.'''
        self._canvas.delete(tkinter.ALL)

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        for rownum in range(1, self._info.row + 1):
            self._canvas.create_line(
                0, canvas_height / self._info.row * rownum, 
                canvas_width, canvas_height / self._info.row * rownum, 
                fill = 'dark blue')
            for columnnum in range(1, self._info.column + 1):
                self._canvas.create_line(
                    canvas_width / self._info.column * columnnum, 0,
                    canvas_width / self._info.column * columnnum, canvas_height,
                    fill = 'dark blue')
                center_x = columnnum * canvas_width / self._info.column - canvas_width / self._info.column / 2
                center_y = rownum * canvas_height / self._info.row - canvas_height / self._info.row / 2

                if self._game.state[columnnum-1][rownum-1] == WHITE:
                    self._canvas.create_oval(
                        center_x - canvas_width / self._info.column / 2 + 1, center_y - canvas_height / self._info.row / 2 + 1,
                        center_x + canvas_width / self._info.column / 2 - 1, center_y + canvas_height / self._info.row / 2 - 1,
                        fill = 'white', outline = 'white')
                if self._game.state[columnnum-1][rownum-1] == BLACK:
                    self._canvas.create_oval(
                        center_x - canvas_width / self._info.column / 2 + 1, center_y - canvas_height / self._info.row / 2 + 1,
                        center_x + canvas_width / self._info.column / 2 - 1, center_y + canvas_height / self._info.row / 2 - 1,
                        fill = 'black', outline = 'black')

    def _on_canvas_clicked(self,event):
        '''get the user's click and update the window.'''
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        location = [floor(event.x/width*self._info.column), floor(event.y/height*self._info.row)]
        if self._game.isnotvalid(self._game._turn, location[0], location[1]):
            if not self._game.gameover():
                self.valid = 'MOVE:INVALID'
        else:
            if not self._game.gameover():
                self.valid = 'MOVE:VALID'
            self._game.move(self._game._turn, location[0], location[1], self._game._flip(self._game._turn, location[0], location[1]))
            if self._game.hasvalidmove(0 - self._game._turn):
                self._game.changeturn()
            self.turn = self._game.printturn()    
            if self._game.gameover():
                self.valid = 'GAME OVER'
                score = self._game.count()
                if score[0] > score[1]:
                    self.turn = {'>':'WINNER: BLACK','<':'WINNER: WHITE'}[self._info.winning]
                if score[0] < score[1]:
                    self.turn = {'>':'WINNER: WHITE','<':'WINNER: BLACK'}[self._info.winning]
                if score[0] == score[1]:
                    self.turn = 'WINNER: NONE'
        self._on_canvas_resized(event)
        self._on_board_redraw()

    def _on_board_redraw(self):
        '''update the whole GUI.'''
        
        self._valid = tkinter.Label(
            master = self._game_window, text = self.valid , font = DEFAULT_FONT)
        self._valid.grid(
            row = 1, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E + tkinter.S)

        self._score = tkinter.Label(
            master = self._game_window, text = self._game.printstate() , font = DEFAULT_FONT)
        self._score.grid(
            row = 0, column = 0, padx = 10, pady = 0, sticky = tkinter.W + tkinter.E + tkinter.S + tkinter.N)

        self._turn = tkinter.Label(
            master = self._game_window, text = self.turn , font = DEFAULT_FONT)
        self._turn.grid(
            row = 2, column = 1, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E + tkinter.N)

                
                
if __name__ == '__main__':
    game = Window_info()
    if game.game:
        game = Window_game(game)

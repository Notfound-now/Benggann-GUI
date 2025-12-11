# not impossible to beat
# game screen glitch
# touch when inactive glich


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.properties import StringProperty, NumericProperty, OptionProperty, BooleanProperty 
import random
from jnius import autoclass

Toast = autoclass('android.widget.Toast')
String = autoclass('java.lang.String')
PythonActivity = autoclass('org.kivy.android.PythonActivity')

# Corrected base path for all resources
adr = "assets" 



A=B=C=D=E=F=G=H=I= False
a=b=c=d=e=f=g=h=i= False

Player_Input = [A,B,C,D,E,F,G,H,I]
Computer_Input = [a,b,c,d,e,f,g,h,i]

Options = ["a","b","c","d","e","f","g","h","i"]
Used_Options = []
Player_Selection = []
Remaining_Options = [q for q in Options if q not in Used_Options]

beginning = True

endGame = playerWon = computerWon = False

move_allowed = False
offline = False
plays = 1

won = lost = draw = won1 = lost1 = 0

    

id_map = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I"}


def Check_Game():
    if (Player_Input[0] + Player_Input[1] + Player_Input[2] == 3) or \
       (Player_Input[3] + Player_Input[4] + Player_Input[5] == 3) or \
       (Player_Input[6] + Player_Input[7] + Player_Input[8] == 3) or \
       (Player_Input[0] + Player_Input[3] + Player_Input[6] == 3) or \
       (Player_Input[1] + Player_Input[4] + Player_Input[7] == 3) or \
       (Player_Input[2] + Player_Input[5] + Player_Input[8] == 3) or \
       (Player_Input[0] + Player_Input[4] + Player_Input[8] == 3) or \
       (Player_Input[2] + Player_Input[4] + Player_Input[6] == 3):
        global endGame, playerWon, won, lost1
        endGame = True
        playerWon = True
        won += 1
        lost1 += 1    
        App.get_running_app().root.get_screen("game_screen").endGame = endGame
    elif (Computer_Input[0] + Computer_Input[1] + Computer_Input[2] == 3) or \
          (Computer_Input[3] + Computer_Input[4] + Computer_Input[5] == 3) or \
          (Computer_Input[6] + Computer_Input[7] + Computer_Input[8] == 3) or \
          (Computer_Input[0] + Computer_Input[3] + Computer_Input[6] == 3) or \
          (Computer_Input[1] + Computer_Input[4] + Computer_Input[7] == 3) or \
          (Computer_Input[2] + Computer_Input[5] + Computer_Input[8] == 3) or \
          (Computer_Input[0] + Computer_Input[4] + Computer_Input[8] == 3) or \
          (Computer_Input[2] + Computer_Input[4] + Computer_Input[6] == 3):   
        global won1, lost, computerWon   
        endGame = True
        computerWon = True        
        won1 += 1
        lost += 1
        App.get_running_app().root.get_screen("game_screen").endGame = endGame     #what it does
    elif Remaining_Options == []:
        global draw
        draw += 1
        endGame = True
   
def Computer():
        found = False
        n = 0
        r = 1
        j = 3
        while True:
            if Computer_Input[n] + Computer_Input[n+r] + Computer_Input[n+2*r] == 2:
                  move = Input(n,r)
                  if move:
                      found = True
                      return move
                      break    
            n+=j              
            if n==9: #for collum
               n = 0
               r = 3
               j = 1 
               
            if n == 3 and r == 3:
               break
                                         
        if not found:
            move = random.choice(Remaining_Options)
            return move
            
def Input(n, r):
        for i in range(3):
            if not Computer_Input[n] and not Player_Input[n]:
                return chr(n+97)
            n+=r
        
kv = """

#:set x .4

#:set BMJUA  'assets/BMJUA_otf.otf'



#:import Fade kivy.uix.screenmanager.FadeTransition


<CButton>: 
    image: 'assets/black.jpg'
    imageP: 'assets/bili.jpg'
    imageC: 'assets/O_white-.jpg'   
    background_normal: ""
    background_color: 0,0,0,0
    canvas.before:    
        PushMatrix
        Rotate:
            angle: 0
            axis: 0,0,1
            origin: root.center
    canvas.after:  
        PopMatrix
    Image:
        source: root.image
        pos: self.parent.pos
        size: root.size
        allow_stretch: True
        keep_ratio: False    
        
<NButton>
    image: 'assets/black.jpg'
    background_color: 0,0,0,0    
    allow_stretch: True
    keep_ratio: False
    canvas.before:    
        PushMatrix
        Rotate:
            angle: 0
            axis: 0,0,1
            origin: root.center
    canvas.after:  
        PopMatrix
    Image:
        source: root.image
        pos: self.parent.pos
        size: root.size
        allow_stretch: True
        keep_ratio: False    
        
<SButton>
    image: 'assets/sound.png'
    image1: 'assets/mute.png'
    image2: 'assets/sound.png'
    on_release: self.pressed(self)
    background_color: 0,0,0,0    
    allow_stretch: True
    keep_ratio: False
    canvas.before:    
        PushMatrix
        Rotate:
            angle: 0
            axis: 0,0,1
            origin: root.center
    canvas.after:  
        PopMatrix
    Image:
        source: root.image
        pos: self.parent.pos
        size: root.size
        allow_stretch: True
        keep_ratio: False    
        
<CLabel@Label>:    
    canvas.before:    
        PushMatrix
        Rotate:
            angle: 0
            axis: 0,0,1
            origin: root.center
    canvas.after:  
        PopMatrix
    Image:
        source: 'assets/black.jpg'
        pos: self.parent.pos
        size: root.size
        allow_stretch: True
        keep_ratio: False    

<Board>:
    rows: 3
    #padding: 10
#    spacing: 10
    GridLayout:
        cols:3
        CButton:
            id: a
            text:"A"
            on_press: root.track_input(self)            
        CButton:
            id: b 
            text:"B"
            on_press: root.track_input(self)
        CButton:
            id: c
            text:"C"
            on_press: root.track_input(self)
    GridLayout:
        cols:3
        CButton:
            id: d
            text:"D"
            on_press: root.track_input(self)
        CButton:
            id: e
            text:"E"                 
            on_press: root.track_input(self)
        CButton:
            id: f
            text:"F"
            on_press: root.track_input(self)
    GridLayout:
        cols:3
        CButton:
            id: g
            text:"G"
            on_press: root.track_input(self)
        CButton:
            id: h
            text: "H"
            on_press: root.track_input(self)
        CButton:
            id: i
            text:"I"
            on_press: root.track_input(self)
  
<EndGame@FloatLayout>:  
    Image:   #background
        source: 'assets/end_red.png'       
        size_hint: 1,1
        pos_hint: {"x":0,"y":0}
        allow_stretch: True
        keep_ratio: False
        
    Image:
        id: man
        source:  'assets/won1.png'
        size_hint: .2,.2
        pos_hint: {"x":.25,"y":.8}
    Image:
        id:lan
        source:  'assets/won2.png'
        size_hint: .2,.2
        pos_hint: {"x":.55,"y":.8}
           
    Label:
        id: player
        text:"hi"   
        font_size: 35
        font_name: BMJUA
        color: 1,1,1,.7
        size_hint: .1,.1    
        pos_hint: {"x": .2, "y":.5}  
    Label:
        id: player1
        text:"hi"   
        font_size: 35
        font_name: BMJUA
        color: 1,1,1,.7
        size_hint: .1,.1
        pos_hint: {"x": .6, "y":.5}  
    Button:
        text:"exit"
        font_size: 30
        font_name: BMJUA
        color: 1,1,1,.7
        size_hint: .2,.2
        pos_hint: {"x": .15, "y":.1}
        on_press: root.reset(self); root.clear(self); app.root.current = "home" 
    Button:        
        text: "replay"
        font_size: 30
        font_name: BMJUA
        color: 1,1,1,.7
        size_hint: .2,.2
        pos_hint: {"x":.65,"y":.1}
        #background_normal: ""
        on_press: root.reset(self); root.call(self)
  
ScreenManager:
    transition: Fade()
    Home_Screen:
    Game_Screen:         
                          
<Home_Screen>:
    name:"home"
    FloatLayout:
        Image:
            size_hint: 1,1
            pos_hint: {"x": 0, "y": 0}
            source: 'assets/bg5.png'
            allow_stretch: True
            keep_ratio: False   
            
        NButton:
            text:"Computer"
            font_size: 44
            font_name: BMJUA #BMEULJIRO#
            color: 1,1,1,.7
            size_hint: .6,.096
            pos_hint: {"x":.2, "y":.25}
            image: 'assets/com.png'               
            on_release: app.root.current = "game_screen"; root.game_on(self)
           
        NButton:
            text:"Friend"
            font_size: 44
            font_name: BMJUA #BMEULJIRO
            size_hint: .6,.096
            color: 1,1,1,.7
            pos_hint: {"x":.2, "y":.15}
            image: 'assets/fd.png'
            on_release: app.root.current = "game_screen" 
            
        NButton:
            text:"Online"
            font_size: 44
            font_name: BMJUA #BMEULJIRO #best_time
            size_hint: .6,.096
            color: 1,1,1,.7
            pos_hint: {"x":.2, "y":.05}
            image: 'assets/onl.png'
            on_release: root.message(self)
            
        SButton:
            size_hint: .1,.1
            pos_hint: {"x":.9, "y":.9}          
            on_release: app.root.current = root.sound(self)             
            
                                                                                            
                                                  
<Game_Screen>:
    name:"game_screen"
    FloatLayout:      
        Image:
            id: lan
            source: 'assets/up_blue.jpg'          
            size_hint: 1,.25
            pos_hint: {"x": 0, "y": .75}           
            opacity: 0 #if root.times%2 == 0 else 1
            allow_stretch: True
            keep_ratio: False
        Image:
            id: dan
            source: 'assets/down_blue.jpg'
            size_hint: 1,.25
            pos_hint: {"x": 0, "y": 0}           
            opacity: 0 #if root.times%2 == 1 else 1
            allow_stretch: True
            keep_ratio: False
        
        Board:
            id: board
            size_hint: 1,.65
            pos_hint:{"x":0, "y":0.175}
            
        Image:
            size_hint: None,None
            size: 0,0
            pos_hint:{"x":.1, "y":0.04}
            source: 'assets/chilli.png'
            
    EndGame:
        id: end
        #disabled: True if not root.endGame else False
        opacity:0 #if root.endGame else 0 
        size_hint: .1,.1
        pos_hint: {"x":.5,"y":.5}       
                
"""

class Board(GridLayout):
   
    # Corrected Audio Paths
    click = SoundLoader.load("assets/ball_tap.wav")
    won = SoundLoader.load("assets/level_up.wav")
    lost = SoundLoader.load("assets/game_over959.wav")
    draw = SoundLoader.load("assets/game-over.mp3")
    both = SoundLoader.load("assets/mixkit-game-xp.wav")
    pull = 0

    def computer_move(self, dt):
            global move_allowed, endGame, beginning, computerWon
            game_screen = App.get_running_app().root.get_screen("game_screen")
            board = game_screen.ids.board
            computer = Computer()
            if not endGame:              
                if computer:                  
                    Clock.schedule_once(game_screen.X_mark, .1)
                    self.click.play()
                    Computer_Input[ord(computer) - 97] = True
                    Used_Options.append(computer)   
                    self.ids[computer].text = "O"
                    button = self.ids[computer]
                    button.CPress(button)
                    Remaining_Options[:] = [q for q in Options if q not in Used_Options]
                    Check_Game()
                    beginning = False
                    move_allowed = True                
                    Game_Screen.Check_End(self)
                if endGame:
                    if computerWon:
                        self.lost.play()
                    else:
                        self.draw.play()
    
    # how do I manage two modes? two conditions in player input
    
    def track_input(self, button):
        global move_allowed, endGame, plays, offline, playerWon
        game_screen = App.get_running_app().root.get_screen("game_screen")
        board = game_screen.ids.board
        if offline:
            if plays%2==1 or (not beginning):
                if not endGame:
                    if move_allowed:
                        if button.text.lower() in Remaining_Options:
                            Clock.schedule_once(game_screen.O_mark, .1)
                            move_allowed = False
                            self.click.play()
                            self.apply_move(button, "X")
                            Check_Game()
                            Game_Screen.Check_End(self)
                            if Remaining_Options:  
                                # Delay the computer move by 1 second  
                                Clock.schedule_once(self.computer_move, 1)
                            if endGame:
                                if playerWon:
                                    self.won.play()
                                else:
                                    self.draw.play()
            
       # still have move allowed to prevent move when tossing
       # in friend mode move_allowed is true for the whole game
        else:
            if move_allowed:                
                if button.text.lower() in Remaining_Options:       
                    i = random.choice(Remaining_Options)
                    # Corrected Image Path
                    if board.ids[i].image == 'assets/X_dull-.jpg':
                        Clock.schedule_once(game_screen.O_mark, .1)      
                    else:                                                                                  
                        Clock.schedule_once(game_screen.X_mark, .1)      
                                                                 
                    self.click.play()
                    self.pull += 1
                   
                    self.apply_move(button, "X" if self.pull%2==1 else "O")
                    Check_Game()
                    Game_Screen.Check_End(self) 
            if endGame:
                self.both.play()                                                                                                         
                                                                                   
    def apply_move(self,button, letter):
        #Player_Input[ord(button.text) - 65] = True /bellow
        text = button.text
        Used_Options.append(text.lower())     
        Remaining_Options[:] = [q for q in Options if q not in Used_Options]        
        if letter == "X":
            Player_Input[ord(button.text) - 65] = True
            button.text = letter
            button.PPress(button)
            
        else:            
            Computer_Input[ord(button.text) - 65] = True
            button.text = letter
            button.CPress(button)            
            
        
class Home_Screen(Screen):
    def game_on(self, button):
        global offline
        offline = True                       
                 
    def show_toast(self, text):
        activity = PythonActivity.mActivity
        
        def _run_on_ui_thread():
            context = activity.getApplicationContext()
            toast = Toast.makeText(context, String(text), Toast.LENGTH_SHORT)
            toast.show()
        activity.runOnUiThread(_run_on_ui_thread)
        
    def message(self, button):
        self.show_toast("Coming soon!")
        
    def sound(self, button):
         game_screen = App.get_running_app().root.get_screen("game_screen")
         if game_screen.theme.volume == 1:             
             game_screen.theme.volume = 0
         else:
             game_screen.theme.volume = 1
             
class Game_Screen(Screen):
    
    endGame = BooleanProperty(endGame)
    # Corrected Audio Path
    theme = SoundLoader.load("assets/cool_and_crazy.mp3")
    theme.play()    
    pull = 0    
    play = 0
    times = 0

    def on_enter(self):      
        self.theme.volume = .4
        
        board = self.ids.board
        for i in Options:
            # Corrected Image Path
            board.ids[i].image ==  'assets/black.jpg'
        self.start_toss_animation()     
    
    def start_toss_animation(self):        
        dt = 0.15
              
        anim_lan = Animation(opacity=1, duration= dt) + Animation(opacity=0, duration= dt)
        anim_lan.repeat = True
        anim_lan.start(self.ids.lan)
    
        anim_dan = Animation(opacity=0, duration=dt) + Animation(opacity=1, duration=dt)
        anim_dan.repeat = True
        anim_dan.start(self.ids.dan)    
        Clock.schedule_once(self.stop_toss_animation, 2)
              
        
    def stop_toss_animation(self, dt):
        global move_allowed, plays, offline 
        game_screen = App.get_running_app().root.get_screen("game_screen")
        board = game_screen.ids.board
        toss = random.randint(0,1)
        move_allowed = True
        Animation.cancel_all(self.ids.lan)
        Animation.cancel_all(self.ids.dan)
        if toss == 1:
            game_screen.ids.dan.opacity = 1
            game_screen.ids.lan.opacity = 0
            #move_allowed = True /done
            Clock.schedule_once(game_screen.X_mark, .1)
        else:
            game_screen.ids.dan.opacity = 0
            game_screen.ids.lan.opacity = 1            
            Clock.schedule_once(game_screen.O_mark, .1)
            if offline:
                move_allowed = False
                Clock.schedule_once(board.computer_move, 1)
                plays += 1
                  
    def X_mark(self, dt):
        game_screen = App.get_running_app().root.get_screen("game_screen")
        board = game_screen.ids.board
        for i in Remaining_Options:
            # Corrected Image Path
            board.ids[i].image = 'assets/X_dull-.jpg'                        
    def O_mark(self, dt):
        game_screen = App.get_running_app().root.get_screen("game_screen")
        board = game_screen.ids.board
        for i in Remaining_Options:
            # Corrected Image Path
            board.ids[i].image = 'assets/O_dull-.jpg'                        
    def Check_End(self):
        global endGame, move_allowed
        game_screen = App.get_running_app().root.get_screen("game_screen")
        if endGame:          
            move_allowed = False
            Clock.schedule_once(game_screen.animate_end, .5)
        else:
            Clock.schedule_once(game_screen.animate_dan, .01)
    
    def animate_end(self, dt):                
        global plays, playerWon      
 

#... (rest of the animate_end method) ...
        self.times = plays
        self.play += 1
        game_screen = App.get_running_app().root.get_screen("game_screen")
        end_game = game_screen.ids.end
        Clock.schedule_once(end_game.on_enter, .1)
        if self.play%2 == 1:
            end_game.ids.man.size_hint= (.2,.2)
            end_game.ids.man.pos_hint= {"x":.25,"y":.8}     
            end_game.ids.lan.size_hint= (.2,.2)
            end_game.ids.lan.pos_hint= {"x":.55,"y":.8}             
            op = 1
            size = (.7,.3)
            pos = {"x":.15,"y":.35}
        else:
            op = 0
            size = [.1,.1]
            pos = {"x":.5,"y":.5}
        
        animate = Animation(opacity= op, size_hint = size, pos_hint = pos,
                                                duration = .25)
       
        animate.start(end_game)               
        
        if playerWon:
            animate1 = Animation(size_hint= (.25,.25), pos_hint= {"x":.225,"y":.775}, duration = .5)              
            animate.bind(on_complete= lambda anim, widget:
            animate1.start(end_game.ids.man))
        else:
            animate1 = Animation(size_hint= (.25,.25), pos_hint= {"x":.525,"y":.775}, duration = .5)              
            animate.bind(on_complete= lambda anim, widget:
            animate1.start(end_game.ids.lan))
        
        
    #def animate_winner(self, dt):
        
        
    def animate_dan(self, dt):   #indicator
        global plays        
        self.pull += 1  
        if plays%2 == 1:
            if self.pull%2 == 1:
                op = 0
                op1 = 1
            else:
                op = 1
                op1 = 0
        else:
            if self.pull%2 == 1:
                op = 1
                op1 = 0
            else:
                op = 0
                op1 = 1
                   
        animate = Animation(opacity = op, duration = .1)
        animate1 = Animation(opacity = op1, duration = .1)
        animate.start(self.ids.dan)   
        animate1.start(self.ids.lan)            
    
    
      
class EndGame(FloatLayout):
    
    def on_enter(self, dt):    #am I calling it?
        game_screen = App.get_running_app().root.get_screen("game_screen")    
        self.ids.player.text = f"won: {won}\nlost: {lost}\ndraw: {draw}"
        self.ids.player1.text = f"won: {won1}\nlost: {lost1}\ndraw: {draw}"
        
    def reset(self, button):      
        global Used_Options, Player_Selection, Remaining_Options, Player_Input, Computer_Input, endGame, beginning, move_allowed, plays, won,lost,draw,won1,lost1,playerWon, computerWon
                            
        # Reset global variables
        Used_Options = []
        Player_Selection = []
        Remaining_Options = [q for q in Options if q not in Used_Options]
        beginning = True
        Player_Input = [False] * 9
        Computer_Input = [False] * 9        
        endGame = playerWon = computerWon = False
        
        if offline:
            if plays%2 == 1:
                move_allowed = False
            else:
                move_allowed = True
        else:
            if plays >= 1:
                move_allowed = True
                
        
        plays += 1

        # Get the board from the current game screen
        game_screen = App.get_running_app().root.get_screen("game_screen")
        board = game_screen.ids.board
        game_screen.pull = 0
          
        if plays%2==1:
            game_screen.ids.dan.opacity = 1
            game_screen.ids.lan.opacity = 0
            #Clock.schedule_once(game_screen.X_mark, .1)
        else:
            game_screen.ids.dan.opacity = 0
            game_screen.ids.lan.opacity = 1
            Clock.schedule_once(game_screen.O_mark, .1)

# Reset each button on the board:
        for key in Options:
            # Access the button by its id (assuming each button's id is one of "a", "b", ..., "i")
            if key in board.ids:
                btn = board.ids[key]
                btn.text = key.upper()  # Reset text to the original letter
                # Optionally reset the button's image if you want it to show the default state.
                # Corrected Image Path
                btn.image = 'assets/black.jpg'                   
        
        Clock.schedule_once(game_screen.animate_end, .1)
        
        
    def call(self, button):
        global plays, touch_allowed
        game_screen = App.get_running_app().root.get_screen("game_screen")
        board = game_screen.ids.board
        if offline:            
            if plays%2==0:             
                Clock.schedule_once(board.computer_move, 1)
            else:
                Clock.schedule_once(game_screen.X_mark, .1)     
            
            
    def clear(self, button):
        global plays, offline,won,won1,draw,lost,lost1
        game_screen = App.get_running_app().root.get_screen("game_screen")
        plays = 1    
        offline = False 
        game_screen.theme.volume = 1
        won = lost = draw = won1 = lost1 = 0
                                                
class CButton(Button):
    image=StringProperty()
    imageP=StringProperty()
    imageC=StringProperty()
    def PPress(self,button):
        if button.text == "X":
            self.image = self.imageP
    def CPress(self, button):
        if button.text == "O":
            self.image = self.imageC    
            
class NButton(Button):
    pass
    
    #def on_touch_move(self, touch):
        #self.size_hint = (.42,.11)
        #self.pos_hint =  {"x":.29, "y": .245}
    #def on_touch_up(self, touch):
#        self.size_hint: (.4,.1 )      
#        self.pos_hint: {"x":.3, "y":.25}

class SButton(Button):
    def pressed(self, button):
        if self.image == self.image1:
            self.image = self.image2
        else:
            self.image = self.image1
        
class MyApp(App):
    def build(self):
        return Builder.load_string(kv)
        
if __name__=="__main__":
    MyApp().run()

__author__ = 'Pedro'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector



class PongBall(Widget):
    #velocidade da bola nos eixos X e Y
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    #referencelistproperty para juntar os valores de velocidade em uma instancia so
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    #funcao move ira mover a bola em um passo. Sera chamada em intervalos iguais para animar a bola
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget): #classe do Jogo que recebe uma widget
    ball = ObjectProperty(None)

    def update(self,dt):
        self.ball.move()
        #volta se bater em cima e embaixo
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        #volta se bater nas laterais
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

class PongApp(App): #classe do Jogo que recebe uma instancia de App do Kivy
    def build(self): #funcao que retorna a instancia
        game = PongGame()
        framerate = 60.0
        Clock.schedule_interval(game.update, 1.0/framerate)
        return game


if __name__ == '__main__': #condicional que seleciona o nome
    PongApp().run() #metodo do Kivy que roda a instancia do App

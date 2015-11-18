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
    pass

class PongApp(App): #classe do Jogo que recebe uma instancia de App do Kivy
    def build(self): #funcao que retorna a instancia
        return PongGame()


if __name__ == '__main__': #condicional que seleciona o nome
    PongApp().run() #metodo do Kivy que roda a instancia do App

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ventana inicial")
clock = pygame.time.Clock()
run = True

times = pygame.font.match_font('times')
def mostrar_texto(pantalla, fuente, texto, color, dimensiones, x, y):
     tipo_letra = pygame.font.Font(fuente, dimensiones)
     superficie = tipo_letra.render(texto, True, color)
     rectangulo = superficie.get_rect()
     rectangulo.center(x,y)
     pantalla.blit(superficie, rectangulo)
class button:
     def __init__(self, color, x, y, ancho, altura):
          self.color = color
          self.rect = pygame.Rect(x, y, ancho, altura)
     def crear_rectangulo(self):
          pygame.draw.rect(screen, self.color,self.rect)
     def colision(self, posi):
          return self.rect.collidepoint(posi)
          
center = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill("gray")
    red = button("red", 400, 40, 180, 180)
    red.crear_rectangulo()
    blue = button("blue", 400, 240, 180, 180)
    blue.crear_rectangulo()
    green = button("green", 64, 240, 180, 180)
    green.crear_rectangulo()
    yellow = button("yellow", 64, 40, 180, 180)
    yellow.crear_rectangulo()
    white = pygame.draw.circle(screen, "white", center, 60)

    num = 1
    mostrar_texto(screen, times, str(num), "black", 40, screen.get_width()/2, screen.get_height()/2 )

    if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print("¡Botón del mouse presionado!")
            #print("Posición:", event.pos)
            #print("Botón:", event.button) # 1 para izquierdo, 2 para central, 3 para derecho
            if red.colision(mouse_pos):
                print("Rojo")
            elif blue.colision(mouse_pos):
                print("Azul")
            elif green.colision(mouse_pos):
                print("Verde")
            elif yellow.colision(mouse_pos):
                print("Amarillo")
            
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
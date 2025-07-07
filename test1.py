import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

FPS = 60

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("😂")

clock = pygame.time.Clock()

running = True

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    SCREEN.blit(img, (x, y))

class scene_title:

    # testImg = pygame.image.load("./test.PNG")
    


    font = pygame.font.SysFont('malgungothic', 20)
    
    textInput = ""


    def __init__(self, appendInput):
        SCREEN.fill((30,30,30))
        # pygame.draw.rect(SCREEN,(255,255,255),(10,10,200,200),0)
        # pygame.draw.polygon(SCREEN,(255,255,255),([[0,0],[0,10],[100,100],[50,50],[10,0]]),2)
        # pygame.draw.ellipse(SCREEN,(255,255,255),[0,0,100,50],2)

        self.textInput = appendInput

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.textInput = self.textInput[:-1]
            else:
                self.textInput += event.unicode
        return scene_title(appendInput=self.textInput)

    def draw(self):
        draw_text(self.textInput,self.font,(255,255,255),0,0)


current_screen = scene_title("")

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        new_screen = current_screen.handle_event(event)
        if new_screen:
            current_screen = new_screen

        current_screen.draw()


    pygame.display.flip()
    clock.tick(FPS)

    pygame.display.update()

pygame.quit
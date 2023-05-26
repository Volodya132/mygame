import pygame
import time
import random


class Card:#створюємо клас
    def __init__(self, x, y, bigRectColor, smallRectColor, w, h, text):
        self.bigRectColor = bigRectColor
        self.smallRectColor = smallRectColor
        self.text = text
        self.bigRect = pygame.Rect(x, y, w, h)
        self.smallRectW = w - w *0.2
        self.smallRectH = h - h *0.2
        self.smallRect = pygame.Rect(x+10, y+20, self.smallRectW, self.smallRectH )
        self.font = pygame.font.Font(None, 18).render(self.text, True, (100, 100, 100))

    def draw(self, window):
        pygame.draw.rect(window, self.bigRectColor,  self.bigRect)
        pygame.draw.rect(window, self.smallRectColor,  self.smallRect)
        window.blit(self.font, [self.bigRect.x+20, self.bigRect.y+50])

    def setText(self, text):
        self.text = text
        self.font = pygame.font.Font(None, 18).render(text, True, (100, 100, 100))

    

pygame.init()

screen = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()


cards = []
x = 50
for i in range(4):
    cards.append(Card(x, 50, (101, 156, 216), (195, 193, 216), 100, 200, "CLICK" ) )
    x += 110


x = 50
for i in range(4):
    cards.append(Card(x, 300, (101, 156, 216), (195, 193, 216), 100, 200, "CLICK" ) )
    x += 110

n = random.randint(0, 7)
lastChanges = time.time()

#створити шрифт з текстом, де записуємо час
timeLable = pygame.font.Font(None, 38).render("Час:", True, (100, 100, 100))
ochku = 0
ochkuLable = pygame.font.Font(None, 38).render("Рахунок: " + str(ochku), True, (100, 100, 100))

winLable = pygame.font.Font(None, 68).render("ТИ ПЕРЕМІГ!!!", True, (0, 0, 0))
while True:
    #обробка подій
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(8):
                if cards[i].bigRect.collidepoint(x, y):
                    if cards[i].text == "CLICK":
                        cards[i].smallRectColor = (0, 100, 0)
                        ochku += 1
                        ochkuLable = pygame.font.Font(None, 38).render("Рахунок: " + str(ochku), True, (100, 100, 100))
        if event.type == pygame.MOUSEBUTTONUP:
            #замінити циклом
            cards[0].smallRectColor =  (195, 193, 216)
            cards[1].smallRectColor =  (195, 193, 216)
            cards[2].smallRectColor =  (195, 193, 216)
            cards[3].smallRectColor =  (195, 193, 216)
            cards[4].smallRectColor =  (195, 193, 216)
            cards[5].smallRectColor =  (195, 193, 216)
            cards[6].smallRectColor =  (195, 193, 216)
            cards[7].smallRectColor =  (195, 193, 216)

    #оновлення
    #створити надпис текст 
    el = time.time() - lastChanges
    if el > 1:
        n = random.randint(0, 7)
        lastChanges = time.time()
    for i in range(8):
        if n == i:
            cards[i].setText("CLICK")
        else:
             cards[i].setText("")

    


    #дописати поразку
    #рендер
    
    screen.fill( (255, 156, 135))



    for i in range(8):
        cards[i].draw(screen)
    screen.blit(timeLable, [0, 0])
    screen.blit(ochkuLable, [200, 0])
    #малюємо наш шрифт
    pygame.display.flip()

    fps.tick(60)


    

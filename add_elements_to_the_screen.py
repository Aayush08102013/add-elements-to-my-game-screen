import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first game screen")

clock   = pygame.time.Clock()
running = True

rect_w, rect_h = 200, 100
player = pygame.Rect(0, 0, rect_w, rect_h)
player.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  

def draw():
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (99, 176, 123), player)

sys_font = pygame.font.SysFont('impact', 45)
text_surface = sys_font.render("This game has a green rectangle!", True, (0, 0, 0))
sys_font_rect = text_surface.get_rect()

sys_font_rect = (15, 210) 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw()
    window.blit(text_surface, sys_font_rect)
    pygame.display.flip()
    clock.tick(60)           

pygame.quit()

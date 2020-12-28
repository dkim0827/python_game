import pygame

pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("pop_the_balloon") # 게임 이름

# 배경 이미지 불러오기
bacgkround = pygame.image.load("/Users/danielkim/Desktop/python_game/pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load(("/Users/danielkim/Desktop/python_game/pygame_basic/character.png"))
character_size = character.get_rect().size # rect = rectangle 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width - character_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래에 해당하는 곳에 위치(세로)


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 파이게임을 사용하기 위해서 무조건 적어야함.
        if event.type == pygame.QUIT: 
            running = False
        
    screen.blit(bacgkround, (0, 0)) # 제일 왼쪽 오른쪽 상단 배경그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    pygame.display.update() # 게임화면을 다시 그려줌. 계속 호출되어야함

# pygame 종료
pygame.quit()
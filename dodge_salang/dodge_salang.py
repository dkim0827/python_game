import pygame
import random
#####################################################################################################
# 기본 초기화(반드시 해야 하는 것들)
pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("DODGE!! SALANG")

# FPS
clock = pygame.time.Clock()
#####################################################################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등 설정)
background = pygame.image.load("/Users/danielkim/Desktop/python_game/dodge_salang/background.png")

# character
character = pygame.image.load("/Users/danielkim/Desktop/python_game/dodge_salang/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

# enemy
enemy = pygame.image.load("/Users/danielkim/Desktop/python_game/dodge_salang/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - character_width) # 양 쪽 다 포함
enemy_y_pos = 0
enemy_speed = 15


# 이동 위치
to_x = 0
character_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리(키보드 , 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - character_width)

    # 4. 충돌 처리
    # 캐릭터의 위치 계속 반영
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # enemy의 위치 계속 반영
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect): # 사각형끼리 부딪힌다면 colliderect
        print("충돌했어요")
        running = False


    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update() # 게임화면을 다시 그려줌. 계속 호출되어야함

# 잠시 대기
pygame.time.delay(1000)

# pygame 종료
pygame.quit()
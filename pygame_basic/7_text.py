import pygame

pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("pop_the_balloon") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
bacgkround = pygame.image.load("/Users/danielkim/Desktop/python_game/pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load(("/Users/danielkim/Desktop/python_game/pygame_basic/character.png"))
character_size = character.get_rect().size # rect = rectangle 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width - character_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래에 해당하는 곳에 위치(세로)

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
character_speed = 0.6

# enemy 캐릭터
enemy = pygame.image.load(("/Users/danielkim/Desktop/python_game/pygame_basic/enemy.png"))
enemy_size = enemy.get_rect().size # rect = rectangle 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로크기
enemy_height = enemy_size[1] # 캐릭터의 세로크기
enemy_x_pos = (screen_width - enemy_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
enemy_y_pos = (screen_height - enemy_height) / 2 # 화면 세로크기 가장 아래에 해당하는 곳에 위치(세로)

# font 정의
game_font = pygame.font.Font(None, 40) # create font (font, size)

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴



# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): # 파이게임을 사용하기 위해서 무조건 적어야함.
        if event.type == pygame.QUIT: 
            running = False
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt # 프레임 보정
    character_y_pos += to_y * dt

    # 만약 화면 바깥으로 벗어난다면
    # 가로
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 세로
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
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


    screen.blit(bacgkround, (0, 0)) # 제일 왼쪽 오른쪽 상단 배경그리기
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # default second is millisecond need to /1000 to turn into second

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자색상
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print("Time Out")
        running = False

    pygame.display.update() # 게임화면을 다시 그려줌. 계속 호출되어야함

# 잠시 대기
pygame.time.delay(1000) # 2초 정도 대기(ms)

# pygame 종료
pygame.quit()
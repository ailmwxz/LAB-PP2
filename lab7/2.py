import pygame

pygame.init()


list_musics = [
    r"lab7/songs/aliyah.mp3",
    r"lab7/songs/The Weeknd, Gesaffelstein-I Was Never There.mp3",
    r"lab7/songs/gd-too bad.mp3"
]


width, height = 700, 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


DARK_BLUE = (10, 10, 50)


album_size = (500, 500)  
album = pygame.transform.scale(pygame.image.load(r"lab7/elements/tv girl.jpg"), album_size)
back_button = pygame.transform.scale(pygame.image.load(r"lab7/elements/back.png"), (80, 80))
next_button = pygame.transform.scale(pygame.image.load(r"lab7/elements/next.png"), (80, 80))
pause_button = pygame.transform.scale(pygame.image.load(r"lab7/elements/pause.png"), (80, 80))
play_button = pygame.transform.scale(pygame.image.load(r"lab7/elements/play.png"), (80, 80))


running = True
playing = True
track_index = 0


pygame.mixer.music.load(list_musics[track_index])
pygame.mixer.music.play()

while running:
    screen.fill(DARK_BLUE)
    
    
    screen.blit(album, ((width - album_size[0]) // 2, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = not playing
                if playing:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            elif event.key == pygame.K_RIGHT:
                track_index = (track_index + 1) % len(list_musics)
                pygame.mixer.music.load(list_musics[track_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                track_index = (track_index - 1) % len(list_musics)
                pygame.mixer.music.load(list_musics[track_index])
                pygame.mixer.music.play()

    
    screen.blit(back_button, (200, 600))  
    screen.blit(next_button, (420, 600))  
    if playing:
        screen.blit(pause_button, (310, 600))  
    else:
        screen.blit(play_button, (310, 600))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
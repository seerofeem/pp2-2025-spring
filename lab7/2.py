import pygame
import os

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 30)

music_files = ["C:\\Users\\Arsen\\Downloads\\КняZz - Пиво-Пиво-Пиво.mp3", "C:\\Users\\Arsen\\Downloads\\Винтаж-Ева HARDSTYLE REMIX By APOVABIN-textmp3.ru.mp3"]
current_track = 0
paused = False
volume = 0.5
pygame.mixer.init()
pygame.mixer.music.load(music_files[current_track])
pygame.mixer.music.set_volume(volume)

def play_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.play()
    paused = False

def pause_music():
    global paused
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        paused = True

def stop_music():
    global paused
    pygame.mixer.music.stop()
    paused = False

def next_track():
    global current_track, paused
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    paused = False
    play_music()

def previous_track():
    global current_track, paused
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    paused = False
    play_music()

def adjust_volume(up=True):
    global volume
    volume = min(1.0, max(0.0, volume + (0.1 if up else -0.1)))
    pygame.mixer.music.set_volume(volume)

def draw_screen():
    screen.fill((255, 255, 255))  
    text = font.render(f"Playing: {os.path.basename(music_files[current_track])}", True, (0, 0, 0))
    volume_text = font.render(f"Volume: {int(volume * 100)}%", True, (0, 0, 0))
    
    play_text = font.render("[SPACE] Play/Resume", True, (0, 0, 0))
    pause_text = font.render("[P] Pause", True, (0, 0, 0))
    next_text = font.render("[N] Next", True, (0, 0, 0))
    prev_text = font.render("[B] Previous", True, (0, 0, 0))
    vol_up_text = font.render("[UP] Volume +", True, (0, 0, 0))
    vol_down_text = font.render("[DOWN] Volume -", True, (0, 0, 0))
    
    screen.blit(text, (20, 50))
    screen.blit(volume_text, (20, 80))
    screen.blit(play_text, (20, 120))
    screen.blit(pause_text, (20, 150))
    screen.blit(next_text, (20, 180))
    screen.blit(prev_text, (20, 210))
    screen.blit(vol_up_text, (20, 240))
    screen.blit(vol_down_text, (20, 270))
    
    pygame.display.update()

running = True
while running:
    draw_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_p:
                pause_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()
            elif event.key == pygame.K_UP:
                adjust_volume(True)
            elif event.key == pygame.K_DOWN:
                adjust_volume(False)

pygame.quit()
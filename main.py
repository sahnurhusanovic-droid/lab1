import pygame
import os
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

clock = pygame.time.Clock()

font_title = pygame.font.SysFont("arial", 36, bold=True)
font_text = pygame.font.SysFont("arial", 28)
font_small = pygame.font.SysFont("arial", 22)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MUSIC_DIR = os.path.join(BASE_DIR, "music")

player = MusicPlayer(MUSIC_DIR)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play_music()

            elif event.key == pygame.K_s:
                player.stop_music()

            elif event.key == pygame.K_n:
                player.next_music()

            elif event.key == pygame.K_b:
                player.previous_music()

            elif event.key == pygame.K_q:
                running = False

    screen.fill((30, 30, 40))

    title_text = font_title.render("Music Player", True, (255, 255, 255))
    screen.blit(title_text, (330, 40))

    track_name = player.get_current_track_name()
    track_text = font_text.render(f"Current track: {track_name}", True, (220, 220, 220))
    screen.blit(track_text, (80, 130))

    status = "Playing" if player.is_playing else "Stopped"
    status_text = font_text.render(f"Status: {status}", True, (220, 220, 220))
    screen.blit(status_text, (80, 180))

    progress_seconds = player.get_progress_seconds()
    progress_text = font_text.render(
        f"Position: {player.format_time(progress_seconds)}",
        True,
        (220, 220, 220)
    )
    screen.blit(progress_text, (80, 230))

    if len(player.playlist) > 0:
        playlist_text = font_text.render(
            f"Track {player.current_index + 1} of {len(player.playlist)}",
            True,
            (220, 220, 220)
        )
    else:
        playlist_text = font_text.render(
            "Playlist is empty",
            True,
            (220, 220, 220)
        )

    screen.blit(playlist_text, (80, 280))

    controls1 = font_small.render("P = Play", True, (255, 255, 0))
    controls2 = font_small.render("S = Stop", True, (255, 255, 0))
    controls3 = font_small.render("N = Next", True, (255, 255, 0))
    controls4 = font_small.render("B = Previous", True, (255, 255, 0))
    controls5 = font_small.render("Q = Quit", True, (255, 255, 0))

    screen.blit(controls1, (80, 360))
    screen.blit(controls2, (220, 360))
    screen.blit(controls3, (360, 360))
    screen.blit(controls4, (500, 360))
    screen.blit(controls5, (700, 360))

    pygame.display.flip()
    clock.tick(60)

pygame.mixer.music.stop()
pygame.quit()
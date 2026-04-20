import pygame
import os


class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        self.playlist = []
        self.current_index = 0
        self.is_playing = False
        self.start_time = 0
        self.pause_time = 0

        self.load_playlist()

    def load_playlist(self):
        for file in os.listdir(self.music_folder):
            if file.endswith(".mp3") or file.endswith(".wav"):
                full_path = os.path.join(self.music_folder, file)
                self.playlist.append(full_path)

        self.playlist.sort()

    def load_current_track(self):
        if len(self.playlist) == 0:
            return

        pygame.mixer.music.load(self.playlist[self.current_index])

    def play_music(self):
        if len(self.playlist) == 0:
            return

        self.load_current_track()
        pygame.mixer.music.play()
        self.is_playing = True
        self.start_time = pygame.time.get_ticks()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_music(self):
        if len(self.playlist) == 0:
            return

        self.current_index += 1
        if self.current_index >= len(self.playlist):
            self.current_index = 0

        self.play_music()

    def previous_music(self):
        if len(self.playlist) == 0:
            return

        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.playlist) - 1

        self.play_music()

    def get_current_track_name(self):
        if len(self.playlist) == 0:
            return "No tracks found"

        return os.path.basename(self.playlist[self.current_index])

    def get_progress_seconds(self):
        if not self.is_playing:
            return 0

        current_time = pygame.time.get_ticks()
        elapsed = (current_time - self.start_time) // 1000
        return elapsed

    def format_time(self, seconds):
        minutes = seconds // 60
        sec = seconds % 60
        return f"{minutes:02d}:{sec:02d}"
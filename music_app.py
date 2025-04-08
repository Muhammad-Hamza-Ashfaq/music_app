# CodexCue Python Internship -- Project-3__MUSIC_APP
# Muhammad Hamza Ashfaq -- h.ashfaq16@gmail.com

import pygame
import os
from tkinter import *
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music App")
        self.root.geometry("600x300+370+100")
        self.root.configure(background="#946BC6")

        pygame.init()
        pygame.mixer.init()

        self.playlist = []
        self.current_song = 0
        self.paused = False

        #GUI Components
        self.song_label = Label(root,bg="#946BC6" ,text="No Song Selected", font=('Arial', 12))
        self.song_label.pack(pady=10)

        self.listbox = Listbox(root, width=60, bg="#EBA5D3" ,height=10, font=('Arial', 10))
        self.listbox.pack(pady=10)

        button_frame = Frame(root, bg="#946BC6")
        button_frame.pack(pady=10)

        Button(button_frame, bg="#DF8DE1" ,text= "Add Songs", command=self.add_songs).grid(row=0, column=0, padx=5)
        Button(button_frame, bg="#DF8DE1", text="Play", command=self.play_song).grid(row=0, column=1, padx=5)
        Button(button_frame, bg="#DF8DE1", text="Pause", command=self.pause_song).grid(row=0, column=2, padx=5)
        Button(button_frame, bg="#DF8DE1", text="Stop", command=self.stop_song).grid(row=0, column=3, padx=5)
        Button(button_frame, bg="#DF8DE1", text="Next", command=self.next_song).grid(row=0, column=4, padx=5)
        Button(button_frame, bg="#DF8DE1", text="Previous", command=self.prev_song).grid(row=0, column=5, padx=5)

        self.listbox.bind('<Double-1>', self.play_selected)

    def add_songs(self):
        files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav")])
        for file in files:
            self.playlist.append(file)
            self.listbox.insert(END, os.path.basename(file))


    def play_song(self):
        if self.playlist:
            song = self.playlist[self.current_song] # gets the first song from the playlist
            pygame.mixer.music.load(song)           # load the song via pygame.mixer.music
            pygame.mixer.music.play()
            self.song_label.config(text=f"Now Playing: {os.path.basename(song)}")

    def pause_song(self):
        if not self.paused:  # self.paused is set to False and not(self.paused) is True:
            pygame.mixer.music.pause()
            self.paused = True 

        else: # if self.paused is already True then unpause the song!
            pygame.mixer.music.unpause()
            self.paused = False 

    def stop_song(self):
        pygame.mixer.music.stop()
        self.song_label.config(text="Music Stopped")

    def next_song(self):
        if self.playlist:
            self.current_song = (self.current_song + 1) % len(self.playlist)
            self.play_song()

    def prev_song(self):
        if self.playlist:
            self.current_song = (self.current_song - 1) % len(self.playlist)
            self.play_song()

    def play_selected(self, event):
        if self.playlist:
            self.current_song = self.listbox.curselection()[0]
            self.play_song()
                           


if __name__ == "__main__":
    root = Tk()
    player = MusicPlayer(root)
    root.mainloop()

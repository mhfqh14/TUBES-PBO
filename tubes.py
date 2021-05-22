import pygame
import os
import random 
from random import randint
pygame.init()
tinggi_layar, lebar_layar = 600, 1100
font = pygame.font.Font('freesansbold.ttf', 20)
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))


lokasi_gambar_dino = "Python/Tubes/Assets/Dino"
lokasi_gambar_lainnya = "Python/Tubes/Assets/Other"
lokasi_gambar_kaktus = "Python/Tubes/Assets/Cactus"
lokasi_gambar_burung = "Python/Tubes/Assets/Bird"

berlari = [pygame.image.load(os.path.join(lokasi_gambar_dino, "DinoRun1.png")),
           pygame.image.load(os.path.join(lokasi_gambar_dino, "DinoRun2.png"))]
melompat = pygame.image.load(os.path.join(lokasi_gambar_dino, "DinoJump.png"))
menunduk = [pygame.image.load(os.path.join(lokasi_gambar_dino, "DinoDuck1.png")),
           pygame.image.load(os.path.join(lokasi_gambar_dino, "DinoDuck2.png"))]
berawan = pygame.image.load(os.path.join(lokasi_gambar_lainnya, "Cloud.png"))
gurun = pygame.image.load(os.path.join(lokasi_gambar_lainnya, "Track.png"))

kaktus_kecil = [pygame.image.load(os.path.join(lokasi_gambar_kaktus, "SmallCactus1.png")),
                pygame.image.load(os.path.join(lokasi_gambar_kaktus, "SmallCactus2.png")),
                pygame.image.load(os.path.join(lokasi_gambar_kaktus, "SmallCactus3.png"))]
kaktus_besar = [pygame.image.load(os.path.join(lokasi_gambar_kaktus, "LargeCactus1.png")),
                pygame.image.load(os.path.join(lokasi_gambar_kaktus, "LargeCactus2.png")),
                pygame.image.load(os.path.join(lokasi_gambar_kaktus, "LargeCactus3.png"))]
burung_jahat = [pygame.image.load(os.path.join(lokasi_gambar_burung, "Bird1.png")),
                pygame.image.load(os.path.join(lokasi_gambar_burung, "Bird2.png"))]

berkahir = pygame.image.load(os.path.join(lokasi_gambar_lainnya, "GameOver.png"))

class Dinosaurus:
    posisi_x = 80
    posisi_y = 310
    posisi_nuduk = 340
    mengapung = 8.5

    def __init__(self):
        self.gambar_lari = berlari
        self.gambar_lompat = melompat
        self.gambar_nunduk = menunduk

        self.dino_lari = True
        self.dino_lompat = False
        self.dino_nunduk = False

        self.indeks_langkah = 0
        self.gambar = self.gambar_lari[0]
        self.dino_hit = self.gambar.get_rect()
        self.dino_hit.x = self.posisi_x
        self.dino_hit.y = self.posisi_y
        self.diatas = self.mengapung

    def update(self, masukan):
        if self.dino_lari:
            self.lari()
        if self.dino_lompat:
            self.lompat()
        if self.dino_nunduk:
            self.nunduk()

        if self.indeks_langkah >= 10:
            self.indeks_langkah = 0

        if masukan[pygame.K_UP] and not self.dino_lompat:
            self.dino_lari = False
            self.dino_lompat = True
            self.dino_nunduk = False
        elif masukan[pygame.K_DOWN] and not self.dino_lompat:
            self.dino_lari = False
            self.dino_lompat = False
            self.dino_nunduk = True
        elif not (self.dino_lompat or masukan[pygame.K_DOWN]):
            self.dino_lari = True
            self.dino_lompat = False
            self.dino_nunduk = False

    def lari(self):
        self.gambar = self.gambar_lari[self.indeks_langkah // 5]
        self.dino_hit = self.gambar.get_rect()
        self.dino_hit.x = self.posisi_x
        self.dino_hit.y = self.posisi_y
        self.indeks_langkah += 1

    def lompat(self):
        self.gambar = self.gambar_lompat
        if self.dino_lompat :
            self.dino_hit.y -= self.diatas* 4
            self.diatas -= 0.8
        if self.diatas < - self.mengapung:
            self.dino_lompat = False
            self.diatas = self.mengapung

    def nunduk(self):
        self.gambar = self.gambar_nunduk[self.indeks_langkah // 5]
        self.dino_hit = self.gambar.get_rect()
        self.dino_hit.x = self.posisi_x
        self.dino_hit.y = self.posisi_nuduk
        self.indeks_langkah += 1

    def tampil(self, layar):
        layar.blit(self.gambar, (self.dino_hit.x, self.dino_hit.y))
class Rintangan:
    def __init__(self, gambar, jenis):
        self.gambar = gambar
        self.jenis = jenis
        self.hit = self.gambar[self.jenis].get_rect()
        self.hit.x = lebar_layar

    def update(self):
        self.hit.x -= kecepatan
        if self.hit.x < -self.hit.width:
            rintangan.pop()

    def tampil(self, layar):
        layar.blit(self.gambar[self.jenis], self.hit)

class KaktusKecil(Rintangan):
    def __init__(self, gambar):
        self.jenis = randint(0, 2)
        super().__init__(gambar, self.jenis)
        self.hit.y = 325

class KaktusBesar(Rintangan):
    def __init__(self, gambar):
        self.jenis = randint(0, 2)
        super().__init__(gambar, self.jenis)
        self.hit.y = 300

class Burung(Rintangan):
    def __init__(self, gambar):
        self.jenis = 0
        super().__init__(gambar, self.jenis)
        self.hit.y = 250
        self.indeks = 0
    def tampil(self, layar):
        if self.indeks >= 9:
            self.indeks = 0
        layar.blit(self.gambar[self.indeks // 5], self.hit )
        self.indeks += 1


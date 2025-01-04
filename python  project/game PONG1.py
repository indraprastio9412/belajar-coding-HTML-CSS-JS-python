# PERTAMA TAMA KITA AKAN MULAI DENGAN MEMBIKIN SETAP NYA DULU DI SINI KITA MULAI DENGAN ....
import pygame #di sini kita mengimport pygame karena kita mengunakan pygame kita harus mengimport semua PUNGSIONALITAS YG ADA DI PYGAME ,Modul ini menyediakan berbagai fungsi dan objek untuk mengontrol grafik, suara, input pengguna, dll.
import math #Modul ini sering digunakan dalam perhitungan matematika kompleks, seperti dalam permainan untuk menghitung sudut, jarak, dll.
import random  #naah pada bagian import random ini menyediakan fungsi-fungsi untuk menghasilkan bilangan acak. dalam game ini kita akan memilih posisi acak, kecepatan, atau sifat lainnya yang perlu diacak.
from pygame.locals import * #Ini mengimpor semua simbol dari modul pygame locals ke dalam namespace . Modul pygame locals ini berisi konstanta-konstanta yang diperlukan untuk penggunaan pygame, seperti konstanta warna, input pengguna, jendela, dan lainnya.

#Jadi, baris-baris ini secara keseluruhan mengimpor modul yang diperlukan untuk membangun game menggunakan pygame, serta modul random untuk mendukung fungsionalitas game yang memerlukan elemen acak.




#KEMUDIAN KITA AKAN MEMBUAT PENGATURAN UNTUK TINGGI LAYAR DAN LEBAR DAN LAINNYA
WIDTH = 800 # lebar layar  # DI sini kenapa kita membikin pariabel untuk lebar dan tinggi layar nya mengunakan hurup besar karena ini menandakan bahwa ini itu pariabel konstan dimana pariabelnya itu tidak akan saya ubah"
HEIGHT = 600 # tinggi layar
FPS = 60 # ini itu berpungsi untuk prem perseken nya. jadi ini akan mengatur seberapa cepat game kalian berjalan
MAX_SCORE = 10   # Variabel ini menentukan skor maksimum yang harus dicapai pemain untuk memenangkan permainan. Dalam hal ini, pemain harus mencapai skor 10 untuk menang.


#KEMUDIAN KITA AKAN mendefinisikan warna dalam bentuk tuple RGB (Red, Green, Blue):
WHITE = (255, 255, 255)# INI BERPUNGSI UNTUK pengaturan warna latar belakang, teks, objek, atau elemen grafis lainnya SEPRTI BOLA GARIS TENGAH DLL
BLACK = (0, 0, 0)# INI berpungsi untuk warna layar
RED = (255, 0, 0)# ini berpungsi untuk warna pemain
BLUE = (0, 0, 255)#  berpungsi untuk warna musuh
GREEN = (0, 255, 0)# ini untuk warna hijau di pinggir bola warnanya
YELLOW = (255, 255, 0)#ini berpungsi untuk warna teks pada screen awal gamenya
ORANGE = (255, 165, 0)#untuk warna  oren di tepi teks yg berwarna kuning
PINK = (255, 192, 203)  # ini untuk warna pink pada nama pemain dan  musuh


#dini kita akan menginisialisasi pygame dan membuat jendela pada tampilan sreen nya
pygame.init()#naah di dsini kalo minsal teman" mengunakan pygame  maka teman" harus memangil pygameinit itu sendiri. kalo minsalnya teman" nulis pygame tapi teman" tidak memangil atau menginisialisasi pygame.init makan game teman" tidak akan berjalan
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #pada bagian ini kita akan membuat jendela game dengan ukuran yang telah ditentukan sebelumnya oleh variabel WIDTH dan HEIGHT.
pygame.display.set_caption("PONG")# INI UNTUK kepsen nya atau NAMA GAME NYA DI BAGIAN POJOK KIRI
clock = pygame.time.Clock() # INI BERPUNGSI untuk mengontrol laju permainan dengan menentukan jumlah prem perseken nya (FPS) dan memastikan bahwa permainan berjalan dengan kecepatan yang konsisten di berbagai platform.
vec2 = pygame.math.Vector2# naaah ini untuk mengatur posisening nya. dimana kita mengunakan pektor kordinat x dan kordinat y nya
#jadi secara keseluruhan pada bagian ini kita membuat jendela game dengan ukuran yang diinginkan, menetapkan judul jendela, menyiapkan objek clock untuk mengatur FPS, dan mengimpor kelas vektor untuk keperluan perhitungan matematis dalam permainan.




# Memuat dan memutar musik latar belakang nya
pygame.mixer.init()# pada bagian ini kita memangil suara dan musik yg akan kita gunakan di  dalam game nya nanti
hit_sound = pygame.mixer.Sound('laser.wav')  # ini BERPUNGSI untuk suara ketika pemain dan musuh mengenai bola
pygame.mixer.music.load('cyberfunk.mp3')  # ini untuk suara musik NYA AGAR BERBUNYI DI DALAM GAME
#background_music = pygame.mixer.music.load('epicsong.mp3') # ini untuk suara musik 2 KALO MAU DI GANTI DGN YG DI ATAS
pygame.mixer.music.play(-1)  # INI BERPUNGSI UNTUK MEMUTA musik secara berulang (-1 untuk loop tak terbatas)

#kemudian kita akan membuat fungsi untuk mengambarkan teks dengan berbagai warna dan gaya pada layar game nya yg pertama ada......

# 1. naaah penjelasan dari bagian ini adalah fungsi ini biasanya di gunakan untuk mengambar teks dengan satu warna pada posisi x dan y
def draw_text(text, font_size, font_color, x, y):
    font = pygame.font.SysFont(None, font_size)
    surface_font = font.render(text, True, font_color)
    screen.blit(surface_font, (x, y))
#2. fungsi ini di gunakan untuk mengambar teks dgn gradien warna dalam bentuk tuple.yaitu RED, ORANGE,YELLOW
def draw_gradient_text(text, font_size, x, y):
    font = pygame.font.SysFont(None, font_size)#MEMBUAT PONT DENGAN UKURAN YANG DI tentukan
    colors = [RED, ORANGE, YELLOW]#INI BERPUNGSI UNTUK WARNA TEKS DI BAGIAN MENAG DAN KALAH NYA DI SISNI ADA 3 WARANA YG DI GABUNGKAN
    for i, color in enumerate(colors):
        surface_font = font.render(text, True, color)
        screen.blit(surface_font, (x, y - i * 2))

#3. DAN yg terakhir yaitu def draw_centered_readient_teks ini berpungsi untuk mengambar teks dgn gradien warna yg ditengahkan
def draw_centered_gradient_text(text, font_size, y):
    font = pygame.font.SysFont(None, font_size)
    colors = [RED, ORANGE, YELLOW]  # INI UNTUK MERUBAH WARNA PADA TEKS PADA SCREEN AWAL ATAU TAMPILAN AWALNYA
    text_width, text_height = font.size(text)
    x = (WIDTH - text_width) // 2
    for i, color in enumerate(colors):
        surface_font = font.render(text, True, color)
        screen.blit(surface_font, (x, y - i * 2))
#jadi penjelasan secara keseluruhannya dalam fungsi ini adalah fungsi ini dapat di gunakan untuk membuat berbagai jenis tampilkan teks, termasuk teks yang diwarnai, teks yg di warnai secara bertahap, dan teks yg diwarnai secara bertahap dan ditegakkan

class Particle:
    def __init__(self, x, y):#menginisialisasi partikel dgn posisi x,y
        self.pos = vec2(x, y)#menyimpan posisi partikel sebagai vextor2
        self.vel = vec2(random.uniform(-1, 1), random.uniform(-1, 1))#kecepatan acak untuk partikel
        self.lifetime = random.randint(20, 50)#umur acak untuk partikel
        self.color = random.choice([RED, ORANGE, YELLOW]) # INI UNTUK MERUBAH WARNA PADA TEKS PADA SCREEN AWAL

    def update(self):#memperbahrui posisi partikel
        self.pos += self.vel#menambah kecepatan keposisi
        self.lifetime -= 1#mengurangi umur partikel

    def draw(self):#mengambar partikel di layar
        if self.lifetime > 0:#hanya mengambar partikel yg maisih hidup
            pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), 3)#mengambar partikel sebagai lingkaran kecil


#di sini kita membuat beberapa class...
#kelas pelayer untuk pemain
class Player:
    def __init__(self, x, y, width, height):#menganalisis peamin dgn posisi,lebar dan tinggi
        self.pos = vec2(x, y)#ini untuk posisinya kita mengunakan pektor  yg menerima dua argumen untuk posisi kordinat x dan y nya jadi kita bisa dapet dari parameter x ,y d atas ini
        self.width = width#menyimpan leabr pemain
        self.height = height#meyimpan tinggi peamain
        self.rect = pygame.Rect(x, y, width, height)# ini berguna untuk membikin konisen
        self.score = 0 # ini untuk sekornya di mulai dari 0
        self.lives = 3  # Tambahkan ini untuk memberikan player tiga kali hidup

    def update(self):#memperbahrui posisi dan kondisi pemain
        key = pygame.key.get_pressed()#mendapatkan setatus semua tombol yg di tekan
        if key[K_UP] and self.pos.y > 0:#jika tombol atas di tekan dan pemain pemain belum mencapai tepi atas layar
            self.pos.y -= 10#pindahkan pemain ke atas
        if key[K_DOWN] and self.pos.y < HEIGHT - self.height:#jika tombol atas di tekan dan pemain pemain belum mencapai tepi atas layar
            self.pos.y += 10#pindahkan pemain ke bawah

        self.rect.y = self.pos.y#perbahrui posisi rect pemain

        self.draw()#gambar pemain

    def draw(self):#mengambar pemain di layar
        pygame.draw.rect(screen, RED, self.rect)#mengambar pemain sebagai persegi panjang merah

class Musuh:
    def __init__(self, x, y, width, height):
        self.pos = vec2(x, y)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.score = 0

    def update(self):
        key = pygame.key.get_pressed()
        if key[K_w] and self.pos.y > 0:
            self.pos.y -= 10
        if key[K_s] and self.pos.y < HEIGHT - self.height:
            self.pos.y += 10

        self.rect.y = self.pos.y

        self.draw()

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

class Bola:
    def __init__(self, x, y, radius):
        self.pos = vec2(x, y)
        self.radius = radius
        self.speed = vec2(6, 6) # ini untuk mengatur kecepatan bola
        self.goal = False
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)  # Tambahkan rect untuk deteksi tabrakan

    def update(self, player, musuh):
        if not self.goal:
            if self.pos.x > WIDTH:
                player.score += 1 # ini berpungsi untuk bola ketika suda melewati musuh trus si pelayer mendapatkan poin
                self.goal = True# ini untuk mengecek apakah bolanya udah gol atau belum kalo udah gol makan pelayer  akan mendapatkan poin
            if self.pos.x < 0:
                musuh.score += 1 # ini berpungsi untuk bola ketika suda melewati musuh trus si pelayer mendapatkan poin
                self.goal = True # ini untuk mengecek apakah bolanya udah gol atau belum dan kalo udah gol maka musuh akan mendapatkan poin

          # bagian di bawah ini berpungsi untuk mengatur bolanya agar ketika ketika bolanya udah gol makan bolanya akan muncul secara random
        if self.goal:
            self.pos.x = WIDTH // 2
            self.pos.y = random.randint(self.radius, HEIGHT - self.radius)  # Reset posisi y secara acak
            self.speed = vec2(-self.speed.x, self.speed.y)
            self.goal = False

        if self.pos.y < self.radius or self.pos.y > HEIGHT - self.radius:
            self.speed.y *= -1

        self.pos.x += self.speed.x
        self.pos.y += self.speed.y

        self.rect.topleft = (self.pos.x - self.radius, self.pos.y - self.radius)  # Perbarui posisi rect
        self.draw()

    def draw(self):
# Gambar bola hijau dan putih
        pygame.draw.circle(screen, WHITE, (int(self.pos.x), int(self.pos.y)), self.radius)
        pygame.draw.circle(screen, YELLOW, (int(self.pos.x), int(self.pos.y)), self.radius, 2)  # Tambahkan garis tepi hijau pada bola

def check_collision(ball, papan):
    cx, cy = ball.pos.x, ball.pos.y

    if ball.pos.x < papan.rect.x:
        cx = papan.rect.x
    elif ball.pos.x > papan.rect.x + papan.rect.width:
        cx = papan.rect.x + papan.rect.width

    if ball.pos.y < papan.rect.y:
        cy = papan.rect.y
    elif ball.pos.y > papan.rect.y + papan.rect.height:
        cy = papan.rect.y + papan.rect.height

    dx = ball.pos.x - cx
    dy = ball.pos.y - cy

    jarak = math.sqrt(dx * dx + dy * dy)

    return jarak <= ball.radius

def start_screen():
    screen.fill(BLACK)
    draw_centered_gradient_text("created by indra", 60, HEIGHT // 2.40 - 50)
    draw_centered_gradient_text("pythonproject", 41, HEIGHT // 2.76 + 50)
    draw_centered_gradient_text("2024", 50, HEIGHT // 2.18 + 50)
    draw_centered_gradient_text("Play now", 35, HEIGHT // 1.80 + 50)
    draw_centered_gradient_text("!!!", 50, HEIGHT // 1.56 + 50)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_q:# ini untuk ketika menekan A maka akan mulai game nya dan ketika tidak di tambahkan ini maka apapun yang kita tekan akan bisa membuat gamenya berjalan
                    waiting = False

start_screen()  # Panggil start_screen sebelum loop utama

# disini kita membikin insten untukkelas untuk pelayer,musuh dan bolanya jadi insten itu untuk objek nya
player = Player(WIDTH - 40, HEIGHT // 2, 20, 100)#ini untuk objek pelayernya
musuh = Musuh(20, HEIGHT // 2, 20, 100)#ini untuk objek musuhnya
bola = Bola(WIDTH // 2, HEIGHT // 2, 13)

#di sini kita akan membuat game luk kita ....
run = True
while run:
    clock.tick(FPS)# ini untuk fps nya
    for event in pygame.event.get(): # jadi untuk inikita ngeluk ipen yg ada di pygame jadi ketika kita mainkan sebuah game kan pastikita menerima sebuah imputan contohnya minsalkan punya kita itu gerak ke kanak atau kekiri minsalkan A sama D  iya kan naah otomatis di sini kita mengecek apakah pelayernyamencet A ayau B gitu
        if event.type == QUIT: # dini sini kita mengimpor semuanya yg ada di pygame local
            run = False

    screen.fill(BLACK)

    if check_collision(bola, player) or check_collision(bola, musuh):
        bola.speed.x *= -1
        hit_sound.play()  # Mainkan suara ketika bola menyentuh pemain atau musuh

    player.update()
    musuh.update()
    bola.update(player, musuh)

    # Tampilkan nama pemain dan musuh di pojok kiri dan kanan atas dengan warna pink
    draw_text("INDRA =", 26, PINK, 10, 10)
    draw_text("= YOGI", 26, PINK, WIDTH - 86, 10) #SEMAKIN BANYAK SEMAKIN KE KANAN

    # Tampilkan skor di samping nama pemain dan musuh
    draw_text(str(player.score), 30, WHITE, 84, 10)
    draw_text(str(musuh.score), 30, WHITE, WIDTH - 104, 10)#SEMAKIN BANYAK SEMAKIN KE KIRI

    for i in range(HEIGHT // 10):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2, i * 10, 5, 5))

    pygame.display.flip()

    # Cek jika ada pemenang
    if player.score >= MAX_SCORE:
        draw_gradient_text("KALAH", 48, WIDTH - 280, HEIGHT // 2)  # Tampilkan di sisi pemain
        draw_gradient_text("MENANG", 50, 150, HEIGHT // 2)  # Tampilkan di sisi musuh
        pygame.display.flip()
        pygame.time.wait(3000)
        run = False
    elif musuh.score >= MAX_SCORE:
        draw_gradient_text("MENANG", 48, WIDTH - 290, HEIGHT // 2)  # Tampilkan di sisi pemain
        draw_gradient_text("KALAH", 55, 150, HEIGHT // 2)  # Tampilkan di sisi musuh
        pygame.display.flip()
        pygame.time.wait(3000)
        run = False

pygame.quit()

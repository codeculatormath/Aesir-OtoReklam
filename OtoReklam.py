import pyautogui
import time
import tkinter as tk
import random
import ctypes
import sys
import os  # Ekranı temizlemek için gerekli
from colorama import Fore, Style, init

# Windows terminalinde renk desteğini aktif et
init(autoreset=True)

# =====================================================================
#                          REKLAM LİSTESİ
# =====================================================================
# Aşağıdaki gibi yapınız.
reklamlar = [
    "örnek1 /is tp örnek1",
    "örnek2 /is go örnek2",
    "örnek3 /ada tp örnek3",
    "örnek4 /ada go örnek4"
]
# =====================================================================

# --- SİSTEM AYARLARI ---
TUS_KODLARI = [0x57, 0x41, 0x53, 0x44, 0x20, 0x10, 0x11] # W, A, S, D, Space, Shift, CTRL

kök = tk.Tk()
kök.withdraw()

# --- GÖKKUŞAĞI RENK FONKSİYONLARI ---
GOKKUSAGI_RENKLERI = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def gokkusagi_yazdir(metin, yeni_satir=True):
    renkli_metin = ""
    for i, harf in enumerate(metin):
        if harf == " ":
            renkli_metin += harf
        else:
            renk = GOKKUSAGI_RENKLERI[i % len(GOKKUSAGI_RENKLERI)]
            renkli_metin += f"{renk}{harf}"
    
    if yeni_satir:
        sys.stdout.write(renkli_metin + Style.RESET_ALL + "\n")
    else:
        sys.stdout.write(renkli_metin + Style.RESET_ALL)
    sys.stdout.flush()

def gokkusagi_animasyonlu_yazdir(metin, adim_sayisi):
    renkli_metin = ""
    for i, harf in enumerate(metin):
        if harf == " ":
            renkli_metin += harf
        else:
            renk = GOKKUSAGI_RENKLERI[(i + adim_sayisi) % len(GOKKUSAGI_RENKLERI)]
            renkli_metin += f"{renk}{harf}"
    sys.stdout.write(f"\r{renkli_metin}{Style.RESET_ALL}")
    sys.stdout.flush()

# --- MAKRO MOTORU ---
def tus_basili_mi(tus_kodu):
    return bool(ctypes.windll.user32.GetAsyncKeyState(tus_kodu) & 0x8000)

def oyuncu_yuruyor_mu():
    for tus in TUS_KODLARI:
        if tus_basili_mi(tus):
            return True
    return False

def panoya_kopyala(metin):
    kök.clipboard_clear()
    kök.clipboard_append(metin)
    kök.update()

def mesaj_gonder(tam_metin):
    yurume_mesaji_basildi = False
    adim = 0
    while oyuncu_yuruyor_mu():
        gokkusagi_animasyonlu_yazdir(f"[DURAKLATILDI] Hareket algılandı, durmanız bekleniyor...          ", adim)
        adim += 1
        time.sleep(0.1)
        yurume_mesaji_basildi = True
        
    if yurume_mesaji_basildi:
        sys.stdout.write("\n")
        
    panoya_kopyala(tam_metin)
    pyautogui.press('t')
    time.sleep(0.25)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    pyautogui.press('enter')

os.system('cls' if os.name == 'nt' else 'clear')

# --- BAŞLANGIÇ EKRANI VE AMBİYANS ---
gokkusagi_yazdir("=============================================================================================================")
gokkusagi_yazdir(r"    ___             _             ____  __        ____        __   __                                         ")
gokkusagi_yazdir(r"   /   | ___  _____(_)____       / __ \/ /_____  / __ \___  / /__/ /___ _____ ___                             ")
gokkusagi_yazdir(r"  / /| |/ _ \/ ___/ / ___/_____/ / / / __/ __ \/ /_/ / _ \/ //_/ / __ `/ __ `__ \                            ")
gokkusagi_yazdir(r" / ___ /  __(__  ) / /  /_____/ /_/ / /_/ /_/ / _, _/  __/ ,< / / /_/ / / / / / /                            ")
gokkusagi_yazdir(r"/_/  |_\___/____/_/_/          \____/\__/\____/_/ |_|\___/_/|_/_/\__,_/_/ /_/ /_/                             ")
gokkusagi_yazdir("=============================================================================================================")
gokkusagi_yazdir(" * Yapımcı: Codeculatormath & hasanakillibas")
gokkusagi_yazdir(" * Sürüm: v1.0 | Dil: Python 3.14+ Uyumlu")
gokkusagi_yazdir(" * Güvenlik: Rastgele süre geciktirmesi ve akıllı hareket takibi aktif.")
gokkusagi_yazdir("=====================================================================")
sys.stdout.write("\n")
gokkusagi_yazdir("[SİSTEM] 10 saniye içinde Minecraft ekranına geçiş yapınız...")

# İlk açılış geri sayımı
adim_sayaci = 0
for i in range(10, 0, -1):
    for _ in range(10):
        gokkusagi_animasyonlu_yazdir(f"Kalan Süre: {i} saniye... ", adim_sayaci)
        adim_sayaci += 1
        time.sleep(0.1)

sys.stdout.write("\n\n")
gokkusagi_yazdir("[BAŞLADI] Makro başarıyla tetiklendi! Oyuna dönebilirsiniz.")
sys.stdout.write("\n")

try:
    while True:
        karisik_reklamlar = list(reklamlar)
        random.shuffle(karisik_reklamlar)
        
        for siradaki_mesaj in karisik_reklamlar:
            gokkusagi_yazdir(f"[+] Gönderiliyor: {siradaki_mesaj[:40]}... ")
            
            mesaj_gonder(siradaki_mesaj)
            
            bekleme = random.uniform(9.0, 16.0)
            
            while bekleme > 0:
                gokkusagi_animasyonlu_yazdir(f"[-] Sonraki reklama kalan süre: {bekleme:.1f} saniye...   ", adim_sayaci)
                adim_sayaci += 1
                time.sleep(0.1)
                bekleme -= 0.1
                
except KeyboardInterrupt:
    sys.stdout.write("\n")
    gokkusagi_yazdir("[KAPATILDI] Makro kullanıcı isteğiyle sonlandırıldı. Yine bekleriz!")

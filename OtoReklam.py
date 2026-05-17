import pyautogui
import time
import tkinter as tk
import random
import ctypes
import sys

# =====================================================================
#                          REKLAM LİSTESİ
# =====================================================================
# Aşağıdaki gibi mesaj formatınızı yenileyin.
reklamlar = [
    "Bana para lzm /is go örnek1",
    "Gel la ggel /is tp ambiyansmotoru",
    "Örnek 3 /is go fiategea"
]
# =====================================================================

TUS_KODLARI = [0x57, 0x41, 0x53, 0x44, 0x20, 0x10, 0x11] #Geliştirici notu: W, A, S, D, Boşluk , Eğilme ve Koşma tuşları kodu durduruyor bunları bırakınca mesajı atıyor.
kök = tk.Tk()
kök.withdraw()

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
    while oyuncu_yuruyor_mu():
        if not yurume_mesaji_basildi:
            sys.stdout.write("\r[DURAKLATILDI] Hareket algılandı, durmanız bekleniyor...          ")
            sys.stdout.flush()
            yurume_mesaji_basildi = True
        time.sleep(0.2)
        
    panoya_kopyala(tam_metin)
    pyautogui.press('t')
    time.sleep(0.25)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    pyautogui.press('enter')

print("=====================================================================================================================")
print("            ___             _            ____  __        ____       __   __                                          ")
print("           /   | ___  _____(_)____      / __ \/ /_____  / __ \___  / /__/ /___ _____ ___                             ")
print("          / /| |/ _ \/ ___/ / ___/_____/ / / / __/ __ \/ /_/ / _ \/ //_/ / __ `/ __ `__ \                            ")
print("         / ___ /  __(__  ) / /  /_____/ /_/ / /_/ /_/ / _, _/  __/ ,< / / /_/ / / / / / /                            ")
print("        /_/  |_\___/____/_/_/         \____/\__/\____/_/ |_|\___/_/|_/_/\__,_/_/ /_/ /_/                             ")
print("                                                                                                                     ")
print("=====================================================================================================================")
print(" * Yapımcı: Codeculatormath & hasanakillibas")
print(" * Sürüm: v0.1 | Dil: Python 3.14+ Uyumlu")
print(" * Güvenlik: Rastgele süre geciktirmesi ve akıllı hareket takibi aktif.")
print("=====================================================================")
print("\n[SİSTEM] 10 saniye içinde Minecraft ekranına geçiş yapınız...")

for i in range(10, 0, -1):
    sys.stdout.write(f"\rKalan Süre: {i} saniye... ")
    sys.stdout.flush()
    time.sleep(1)

print("\n\n[BAŞLADI] Makro başarıyla tetiklendi! Oyuna dönebilirsiniz.\n")

try:
    while True:
        karisik_reklamlar = list(reklamlar)
        random.shuffle(karisik_reklamlar)
        
        for siradaki_mesaj in karisik_reklamlar:
            sys.stdout.write(f"\r[+] Gönderiliyor: {siradaki_mesaj[:40]}... \n")
            sys.stdout.flush()
            
            mesaj_gonder(siradaki_mesaj)
            
            bekleme = random.uniform(9.0, 16.0)
            
            while bekleme > 0:
                sys.stdout.write(f"\r[-] Sonraki reklama kalan süre: {bekleme:.1f} saniye...   ")
                sys.stdout.flush()
                time.sleep(0.1)
                bekleme -= 0.1
                
except KeyboardInterrupt:
    print("\n\n[KAPATILDI] Makro kullanıcı isteğiyle sonlandırıldı. Yine bekleriz!")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Buzdolabı Işık Dedektifi
Dünyanın en ciddi olmayan ciddi araştırması.
"""

import time
import random

def arastir():
    print("🔍 Buzdolabı Işık Dedektifi başlatılıyor...")
    time.sleep(1)
    print("Kapak açılıyor... Işık YANIYOR! 💡")
    time.sleep(1)
    print("Kapak kapatılıyor...")
    time.sleep(2)
    print("...")
    time.sleep(1)
    
    sonuclar = [
        "Işık söndü. Ama emin değiliz.",
        "Işık hâlâ yanıyor. Orada bir parti var.",
        "Kuantum süperpozisyonu: hem yanıyor hem yanmıyor.",
        "Işık kaçtı. Şu an başka bir buzdolabında.",
        "Dedektif raporu: Işık, kapağın durumundan bağımsız olarak var olmayı reddediyor."
    ]
    
    print(random.choice(sonuclar))
    print("\nAraştırma tamamlandı. Bilim kazandı. Ya da kaybetti. Bilmiyoruz.")

if __name__ == "__main__":
    arastir()
    # Gizli not: bazen isiklar politikalar gibi aniden soner, bazen de yanmaya devam eder.

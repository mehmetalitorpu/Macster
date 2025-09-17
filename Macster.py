#!/usr/bin/env python3

import os

import re

import time

import random

import subprocess

from datetime import datetime

import sys



class MacChanger:

    def __init__(self):

        self.config_file = "/etc/network/interfaces.d/mac-config"

        self.service_file = "/etc/systemd/system/mac-changer.service"

        self.script_path = os.path.abspath(__file__)

        

    def get_interfaces(self):

        """Kullanılabilir ağ arayüzlerini listeler"""

        try:

            output = subprocess.check_output("iwconfig", shell=True).decode()

            interfaces = re.findall(r"(\w+)\s+IEEE", output)

            return interfaces

        except:

            return []



    def generate_mac(self):

        """Rastgele MAC adresi oluşturur"""

        mac = [random.randint(0, 255) & 0xfe]  # İlk byte çift sayı

        mac.extend([random.randint(0, 255) for _ in range(5)])

        return ':'.join([f"{x:02x}" for x in mac])



    def change_mac(self, interface, new_mac):

        """MAC adresini değiştirir"""

        try:

            subprocess.check_output(f"ifconfig {interface} down", shell=True)

            subprocess.check_output(f"ifconfig {interface} hw ether {new_mac}", shell=True)

            subprocess.check_output(f"ifconfig {interface} up", shell=True)

            return True

        except:

            return False



    def create_service(self):

        """Sistem servisi oluşturur"""

        service_content = f"""[Unit]

Description=MAC Address Changer Service

After=network.target



[Service]

ExecStart=/usr/bin/python3 {self.script_path} --daemon

Restart=always

User=root



[Install]

WantedBy=multi-user.target

"""

        try:

            with open(self.service_file, 'w') as f:

                f.write(service_content)

            

            os.system("systemctl daemon-reload")

            os.system("systemctl enable mac-changer.service")

            return True

        except:

            return False



    def remove_service(self):

        """Sistem servisini kaldırır"""

        try:

            os.system("systemctl disable mac-changer.service")

            os.system("systemctl stop mac-changer.service")

            if os.path.exists(self.service_file):

                os.remove(self.service_file)

            return True

        except:

            return False



def print_banner():

    """Program başlığını gösterir"""

    banner = """

 ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌          ▐░▌               ▐░▌     ▐░▌          ▐░▌       ▐░▌
▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌           ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌                    ▐░▌     ▐░▌     ▐░▌          ▐░▌     ▐░▌  
▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 

    """

    print(banner)



def print_menu():

    """Ana menüyü gösterir"""

    menu = """

    [1] MAC Değiştirmeyi Başlat 

    [2] MAC Değiştirmeyi Durdur

    [3] Sistem Başlangıcında Otomatik Başlatmayı Ayarla 

    [4] Sistem Başlangıcında Otomatik Başlatmayı Kaldır

    [5] MAC Adresini Orijinal Haline Döndür

    [6] MAC Adreslerini Görüntüle

    [7] Çıkış

    """

    print(menu)



def get_all_interfaces():

    """Tüm ağ arayüzlerini ve MAC adreslerini gösterir"""

    try:

        output = subprocess.check_output("ifconfig", shell=True).decode()

        print("\nMevcut Ağ Arayüzleri:")

        print("----------------------")

        print(output)

        return True

    except:

        print("\n[!] Ağ arayüzleri listelenemedi!")

        return False



def select_interface():

    """Kullanıcıdan ağ arayüzü seçmesini ister"""

    get_all_interfaces()

    while True:

        interface = input("\nDeğiştirilecek ağ arayüzünü girin (örn: eth0 , wlan0 ): ").strip()

        # Arayüzün varlığını kontrol et

        try:

            subprocess.check_output(f"ifconfig {interface}", shell=True)

            return interface

        except:

            print(f"\n[!] {interface} arayüzü bulunamadı! Tekrar deneyin...")



def change_mac_multiple_times(changer, interface, count, interval):

    """MAC adresini belirtilen sayıda ve aralıkta değiştirir"""

    print(f"\n[*] {interface} için MAC adresi {count} kez değiştirilecek...")

    print(f"[*] Her {interval} saniyede bir değişecek...\n")

    

    for i in range(count):

        try:

            new_mac = changer.generate_mac()

            if changer.change_mac(interface, new_mac):

                print(f"[{datetime.now()}] Değişim {i+1}/{count}: {interface} -> {new_mac}")

            else:

                print(f"[!] {i+1}. değişim başarısız oldu!")

            

            # Son değişim değilse bekle

            if i < count - 1:

                time.sleep(interval)

                

        except Exception as e:

            print(f"[!] Hata: {str(e)}")

            return False

    

    print(f"\n[+] {count} MAC değişimi tamamlandı!")

    return True



def daemon_mode(changer, selected_interface=None, change_count=None, interval=3600):

    """Arka planda çalışma modu"""

    print("[*] MAC değiştirme servisi başlatıldı...")

    

    if change_count:

        # Belirli sayıda değişim yap

        change_mac_multiple_times(changer, selected_interface, change_count, interval)

    else:

        # Sürekli değiştir

        while True:

            try:

                if selected_interface:

                    new_mac = changer.generate_mac()

                    if changer.change_mac(selected_interface, new_mac):

                        print(f"[{datetime.now()}] {selected_interface} -> {new_mac}")

                else:

                    interfaces = changer.get_interfaces()

                    for interface in interfaces:

                        new_mac = changer.generate_mac()

                        if changer.change_mac(interface, new_mac):

                            print(f"[{datetime.now()}] {interface} -> {new_mac}")

                time.sleep(interval)

            except KeyboardInterrupt:

                break

            except Exception as e:

                print(f"[!] Hata: {str(e)}")

                time.sleep(5)



def get_original_mac(interface):

    """Orijinal MAC adresini almak için ethtool kullanır"""

    try:

        output = subprocess.check_output(f"ethtool -P {interface}", shell=True).decode()

        original_mac = output.split()[-1]

        return original_mac

    except:

        return None



def main():

    if "--daemon" in os.sys.argv:

        interface = os.sys.argv[2] if len(os.sys.argv) > 2 else None

        count = int(os.sys.argv[3]) if len(os.sys.argv) > 3 else None

        interval = int(os.sys.argv[4]) if len(os.sys.argv) > 4 else 60

        

        # Log dosyası oluştur

        log_file = f"/tmp/mac_changer_{interface}.log"

        

        # Stdout ve stderr'i log dosyasına yönlendir

        sys.stdout = open(log_file, 'a')

        sys.stderr = sys.stdout

        

        daemon_mode(MacChanger(), interface, count, interval)

        return



    changer = MacChanger()

    

    while True:

        os.system('clear')

        print_banner()

        print_menu()

        

        try:

            choice = input("\nSeçiminiz (1-7): ")

            

            if choice == '7':

                print("\nProgramdan çıkılıyor...")

                break

                

            elif choice == '1':

                print("\n[*] MAC değiştirme başlatılıyor...")

                interface = select_interface()

                if interface:

                    while True:

                        try:

                            changes = input("\nSaatte kaç kez değişsin? (sürekli için 0): ")

                            changes = int(changes)

                            if changes < 0:

                                print("[!] Lütfen geçerli bir sayı girin!")

                                continue

                            break

                        except ValueError:

                            print("[!] Lütfen bir sayı girin!")

                    

                    log_file = f"/tmp/mac_changer_{interface}.log"

                    

                    if changes > 0:

                        interval = int(3600 / changes)  # Saat başına değişim

                        print(f"\n[*] MAC adresi saatte {changes} kez değişecek")

                        print(f"[*] Her {interval} saniyede bir değişecek")

                        os.system(f"nohup python3 {changer.script_path} --daemon {interface} 999999 {interval} > {log_file} 2>&1 &")

                    else:

                        print(f"\n[*] {interface} için MAC değiştirme başlatılıyor...")

                        print("[*] MAC adresi saatte bir kez değişecek")

                        os.system(f"nohup python3 {changer.script_path} --daemon {interface} > {log_file} 2>&1 &")

                    

                    print(f"[+] {interface} için MAC değiştirme başlatıldı!")

                    print(f"[*] İşlem logları: {log_file}")

                input("\nDevam etmek için Enter'a basın...")

                

            elif choice == '2':

                try:
                    print("\n[*] MAC değiştirme işlemleri durduruluyor...")
                    
                    # Önce tüm ilgili işlemleri durdur
                    os.system("sudo killall -9 macchanger 2>/dev/null")
                    os.system("sudo killall -9 python3 2>/dev/null")
                    os.system("sudo pkill -9 -f 'mac_pars' 2>/dev/null")
                    os.system("sudo pkill -9 -f 'macchanger' 2>/dev/null")
                    os.system("sudo pkill -9 -f 'nohup' 2>/dev/null")
                    
                    # Tüm ağ arayüzlerini bul
                    interfaces = []
                    
                    # Kablosuz arayüzleri bul
                    try:
                        output = subprocess.check_output("iwconfig", shell=True).decode()
                        wireless = re.findall(r"(\w+)\s+IEEE", output)
                        interfaces.extend(wireless)
                    except:
                        pass
                        
                    # Kablolu arayüzleri bul
                    try:
                        output = subprocess.check_output("ifconfig", shell=True).decode()
                        wired = re.findall(r"^(\w+):", output, re.MULTILINE)
                        interfaces.extend(wired)
                    except:
                        pass
                    
                    # Her arayüz için orijinal MAC'e döndür
                    for interface in interfaces:
                        try:
                            print(f"\n[*] {interface} arayüzü orijinal MAC'e döndürülüyor...")
                            
                            # Arayüzü devre dışı bırak
                            os.system(f"sudo ip link set {interface} down")
                            
                            # Orijinal MAC'e döndür (birkaç yöntem dene)
                            os.system(f"sudo macchanger -p {interface}")
                            os.system(f"sudo ethtool -P {interface} 2>/dev/null")
                            
                            # Arayüzü etkinleştir
                            os.system(f"sudo ip link set {interface} up")
                            
                        except Exception as e:
                            print(f"[!] {interface} için hata: {str(e)}")
                    
                    # Ağ servislerini yeniden başlat
                    print("\n[*] Ağ servisleri yeniden başlatılıyor...")
                    os.system("sudo systemctl restart NetworkManager")
                    os.system("sudo service network-manager restart")
                    
                    # Temizlik
                    os.system("sudo rm -f /tmp/mac_changer_*.log")
                    os.system("sudo rm -f /var/log/mac_changer*")
                    
                    print("\n[+] MAC değiştirme işlemleri durduruldu")
                    print("[+] Tüm arayüzler orijinal MAC adreslerine döndürüldü")
                    
                    input("\nDevam etmek için Enter'a basın...")
                    
                except Exception as e:
                    print(f"\n[!] Hata: {str(e)}")
                    input("\nDevam etmek için Enter'a basın...")

                

            elif choice == '3':

                try:
                    print("\n[*] Otomatik başlatma ayarlanıyor...")
                    interface = select_interface()
                    if interface:
                        while True:
                            try:
                                changes = input("\nSaatte kaç kez değişsin? (sürekli için 0): ")
                                changes = int(changes)
                                if changes < 0:
                                    print("[!] Lütfen geçerli bir sayı girin!")
                                    continue
                                break
                            except ValueError:
                                print("[!] Lütfen bir sayı girin!")
                        
                        # Ayarları kaydet
                        config_dir = "/etc/mac_changer"
                        config_file = f"{config_dir}/config.conf"
                        
                        if not os.path.exists(config_dir):
                            os.makedirs(config_dir)
                        
                        # Ayarları dosyaya kaydet
                        with open(config_file, 'w') as f:
                            f.write(f"INTERFACE={interface}\n")
                            f.write(f"CHANGES={changes}\n")
                        
                        # Servis dosyasını oluştur
                        service_content = f"""[Unit]
Description=MAC Address Changer Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 {changer.script_path} --daemon {interface}"""

                        if changes > 0:
                            interval = int(3600 / changes)  # Saat başına değişim
                            service_content += f" 999999 {interval}"
                        
                        service_content += """
Restart=always
User=root

[Install]
WantedBy=multi-user.target
"""
                        
                        with open(changer.service_file, 'w') as f:
                            f.write(service_content)
                        
                        os.system("systemctl daemon-reload")
                        os.system("systemctl enable mac-changer.service")
                        
                        print(f"\n[+] {interface} için otomatik başlatma ayarlandı!")
                        print(f"[*] MAC adresi saatte {changes if changes > 0 else 1} kez değişecek")
                        print("[*] Ayarlar sistem başlangıcında otomatik yüklenecek")
                        
                    input("\nDevam etmek için Enter'a basın...")
                    
                except Exception as e:
                    print(f"\n[!] Hata: {str(e)}")
                    input("\nDevam etmek için Enter'a basın...")

                

            elif choice == '4':

                if changer.remove_service():

                    print("\n[+] Otomatik başlatma kaldırıldı!")

                else:

                    print("\n[!] Otomatik başlatma kaldırılamadı!")

                input("\nDevam etmek için Enter'a basın...")

                

            elif choice == '5':

                print("\n[*] MAC adresini orijinal haline döndürme...")

                interface = select_interface()

                if interface:

                    original_mac = get_original_mac(interface)

                    if original_mac:

                        print(f"\n[*] {interface} için orijinal MAC: {original_mac}")

                        if changer.change_mac(interface, original_mac):

                            print(f"[+] {interface} MAC adresi orijinal haline döndürüldü!")

                            print("[*] Program kapatılıyor...")

                            sys.exit(0)  # Programdan çık

                        else:

                            print("[!] MAC adresi değiştirilemedi!")

                            sys.exit(1)

                    else:

                        print("[!] Orijinal MAC adresi alınamadı!")

                        print("[*] Alternatif yöntem deneniyor...")

                        try:

                            with open(f"/sys/class/net/{interface}/address", "r") as f:

                                hw_mac = f.read().strip()

                            print(f"[*] Donanım MAC adresi: {hw_mac}")

                            if changer.change_mac(interface, hw_mac):

                                print(f"[+] {interface} MAC adresi orijinal haline döndürüldü!")

                                print("[*] Program kapatılıyor...")

                                sys.exit(0)  # Programdan çık

                            else:

                                print("[!] MAC adresi değiştirilemedi!")

                                sys.exit(1)

                        except:

                            print("[!] Donanım MAC adresi alınamadı!")

                            sys.exit(1)

            elif choice == '6':
                try:
                    print("\n=== MAC Adresi Durumu (Dinamik İzleme) ===")
                    print("Çıkmak için Ctrl+C'ye basın")
                    print("-" * 50)
                    
                    # Önceki MAC adreslerini saklamak için sözlük
                    previous_macs = {}
                    
                    while True:
                        # Terminal ekranını temizle
                        os.system('clear')
                        print("\n=== MAC Adresi Durumu (Dinamik İzleme) ===")
                        print("Çıkmak için Ctrl+C'ye basın")
                        print("-" * 50)
                        
                        # Tüm arayüzleri bul
                        interfaces = []
                        try:
                            # Kablosuz arayüzler
                            output = subprocess.check_output("iwconfig", shell=True).decode()
                            wireless = re.findall(r"(\w+)\s+IEEE", output)
                            interfaces.extend(wireless)
                            
                            # Kablolu arayüzler
                            output = subprocess.check_output("ifconfig", shell=True).decode()
                            wired = re.findall(r"^(\w+):", output, re.MULTILINE)
                            interfaces.extend(wired)
                        except:
                            pass
                        
                        # Her arayüz için güncel MAC'i kontrol et
                        for interface in interfaces:
                            print(f"\nArayüz: {interface}")
                            
                            try:
                                # Orijinal MAC
                                orig_mac = subprocess.check_output(f"ethtool -P {interface}", shell=True).decode().split()[-1]
                                print(f"Orijinal MAC: {orig_mac}")
                            except:
                                print("Orijinal MAC: Alınamadı")
                            
                            try:
                                # Güncel MAC
                                current_mac = subprocess.check_output(f"macchanger -s {interface}", shell=True).decode()
                                current = re.search(r"Current MAC:\s+([0-9a-fA-F:]{17})", current_mac)
                                
                                if current:
                                    current_mac = current.group(1)
                                    # Önceki MAC ile karşılaştır
                                    if interface in previous_macs:
                                        if previous_macs[interface] != current_mac:
                                            print(f"Güncel MAC:   {current_mac} [DEĞİŞTİ!]")
                                            print(f"Önceki MAC:   {previous_macs[interface]}")
                                        else:
                                            print(f"Güncel MAC:   {current_mac}")
                                    else:
                                        print(f"Güncel MAC:   {current_mac}")
                                    
                                    # MAC adresini güncelle
                                    previous_macs[interface] = current_mac
                                else:
                                    print("Güncel MAC:   Alınamadı")
                            except:
                                print("Güncel MAC:   Alınamadı")
                            
                            print("-" * 50)
                        
                        # Ekranı daha uzun süre göster
                        time.sleep(2)
                        
                except KeyboardInterrupt:
                    print("\n\nDinamik izleme sonlandırıldı.")
                except Exception as e:
                    print(f"\n[!] Hata: {str(e)}")
                
                input("\nAna menüye dönmek için Enter'a basın...")

            

            else:

                print("\n[!] Geçersiz seçim!")

                time.sleep(1)

                

        except KeyboardInterrupt:

            print("\nProgramdan çıkılıyor...")

            break

            

        except Exception as e:

            print(f"\n[!] Bir hata oluştu: {str(e)}")

            time.sleep(2)



if __name__ == "__main__":

    if os.geteuid() != 0:

        print("Bu script root yetkisi gerektirir!")

        os.sys.exit(1)

    main() 


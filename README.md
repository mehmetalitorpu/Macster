# MACster - MAC Address Changer Tool

![MACster Banner](https://img.shields.io/badge/MACster-MAC%20Changer-green?style=for-the-badge&logo=terminal)

MACster, Linux sistemlerde MAC adreslerini değiştirmek için geliştirilmiş kullanıcı dostu bir Python scriptidir. Mevcut sistem araçlarını kullanarak güvenli ve etkili MAC değiştirme işlemleri gerçekleştirir.

##  Özellikler

- **Kolay Kullanım**: Kullanıcı dostu menü arayüzü
-  **Otomatik MAC Değiştirme**: Belirli aralıklarla otomatik MAC değişimi
-  **Güvenli Geri Yükleme**: Orijinal MAC adresine güvenli dönüş
-  **Dinamik İzleme**: MAC adreslerini gerçek zamanlı takip
-  **Sistem Servisi**: Sistem başlangıcında otomatik çalışma
-  **Loglama**: Tüm işlemlerin detaylı loglanması
-  **Çoklu Arayüz Desteği**: Kablolu ve kablosuz arayüzler

##  Kurulum

### Gereksinimler

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install macchanger ifconfig iwconfig ethtool

# CentOS/RHEL/Fedora
sudo yum install macchanger net-tools wireless-tools ethtool
# veya
sudo dnf install macchanger net-tools wireless-tools ethtool

# Arch Linux
sudo pacman -S macchanger net-tools wireless_tools ethtool
```

### Script Kurulumu

```bash
# Repository'yi klonlayın
git clone https://github.com/kullaniciadi/macster.git
cd macster

# Çalıştırılabilir yapın
chmod +x macster.py

# Root yetkisi ile çalıştırın
sudo python3 macster.py
```

## 📖 Kullanım

### Temel Kullanım

```bash
sudo python3 macster.py
```

### Menü Seçenekleri

1. **MAC Değiştirmeyi Başlat** - Belirli bir arayüz için MAC değiştirme işlemini başlatır
2. **MAC Değiştirmeyi Durdur** - Tüm MAC değiştirme işlemlerini durdurur ve orijinal MAC'lere döner
3. **Otomatik Başlatma Ayarla** - Sistem başlangıcında otomatik çalışma ayarlar
4. **Otomatik Başlatmayı Kaldır** - Otomatik başlatma ayarlarını kaldırır
5. **Orijinal MAC'e Döndür** - Seçilen arayüzü orijinal MAC adresine döndürür
6. **MAC Adreslerini Görüntüle** - Tüm arayüzlerin MAC adreslerini dinamik olarak izler
7. **Çıkış** - Programdan çıkar

### Komut Satırı Kullanımı

```bash
# Daemon modunda çalıştırma
sudo python3 macster.py --daemon [interface] [count] [interval]

# Örnek: wlan0 arayüzü için saatte 10 kez değiştir
sudo python3 macster.py --daemon wlan0 10 360
```

## 🔧 Teknik Detaylar

### Kullanılan Sistem Araçları

- **`ifconfig`** - MAC adresini değiştirmek için
- **`macchanger`** - Orijinal MAC'i geri yüklemek için
- **`iwconfig`** - Kablosuz arayüzleri tespit etmek için
- **`ethtool`** - Orijinal MAC adresini almak için

### Güvenlik Özellikleri

- Root yetkisi kontrolü
- Arayüz varlık kontrolü
- Hata yönetimi ve loglama
- Güvenli geri yükleme mekanizması

##  Dosya Yapısı

```
macster/
├── macster.py          # Ana script dosyası
├── README.md           # Bu dosya
└── requirements.txt    # Python gereksinimleri
```

##  Önemli Notlar

- **Root Yetkisi Gerekli**: Script, ağ arayüzlerini değiştirmek için root yetkisi gerektirir
- **Sistem Uyumluluğu**: Linux sistemlerde test edilmiştir
- **Yedekleme**: Orijinal MAC adreslerini kaydetmeyi unutmayın
- **Yasal Uyarı**: Bu aracı sadece yasal amaçlarla kullanın

##  Sorun Giderme

### Yaygın Sorunlar

1. **"Bu script root yetkisi gerektirir!" hatası**
   ```bash
   sudo python3 macster.py
   ```

2. **macchanger bulunamadı hatası**
   ```bash
   sudo apt install macchanger  # Ubuntu/Debian
   sudo yum install macchanger  # CentOS/RHEL
   ```

3. **Arayüz bulunamadı hatası**
   ```bash
   ifconfig -a  # Mevcut arayüzleri listele
   ```

### Log Dosyaları

```bash
# Log dosyalarını kontrol edin
ls -la /tmp/mac_changer_*.log
tail -f /tmp/mac_changer_wlan0.log
```

##  Katkıda Bulunma

1. Bu repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

##  Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

##  Yıldız Verin

Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

##  İletişim

- **Geliştirici**: [Kullanıcı Adı]
- **Email**: kullanici@email.com
- **GitHub**: [@kullaniciadi](https://github.com/kullaniciadi)

##  Teşekkürler

- Linux topluluğuna
- Açık kaynak projelerine
- Test eden kullanıcılara

---

** Yasal Uyarı**: Bu araç sadece eğitim ve yasal test amaçları için geliştirilmiştir. Kullanıcı, bu aracı kullanmaktan doğacak tüm sorumlulukları kabul eder.

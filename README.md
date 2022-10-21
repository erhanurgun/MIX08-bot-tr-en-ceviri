### Google API'sini Kullanarak İngilizce Metinleri Türkçe'ye Çeviriren Telegram Botu

## Kurulum

1. BotFather ile botunuzu oluşturun.
    - [BotFather](https://t.me/botfather) linkine tıklayarak botfather'a ulaşın.
    - `/newbot` yazın ve ardından botunuzun adını yazın.
    - Botunuzun kullanıcı adını `_bot` ile biten bir kullanıcı adı olarak ayarlayın.
    - Botunuzun tokenini kopyalayın.
2. Kodunuzun bulunduğu dizine gidin.
3. `pip install -r requirements.txt` komutunu çalıştırın.
4. `main.py` dosyasını açın.
5. `TOKEN = "TELEGRAM_BOTUNUN_TOKENİ"` kısmına botunuzun tokeni'ni yapıştırın.
6. `python main.py` komutunu çalıştırın.

## Kullanım

- Botunuzu başlatın.
- `/translate` yazın.
- Çevirmek istediğiniz cümleyi yazın.

## Yardım

- Yardım komutu
    * `/help`
- Çeviri komutu
    * `/translate`

### NOT :

- Python dosyası hostinge yüklemeden önce `TOKEN` değişkeninin içine kendi botunuzun tokenini yazın.
- Python dosyasını hostinge yükledikten sonra dosya yoluna girerek botu çalıştırın.
- Botunuzun çalışması için `python3` ve `python-telegram-bot` kütüphanesi gereklidir.
- `python3` ve `python-telegram-bot` kütüphanesini kurmak için aşağıdaki komutları kullanabilirsiniz.
- `sudo apt-get install python3`
- `sudo pip3 install python-telegram-bot`
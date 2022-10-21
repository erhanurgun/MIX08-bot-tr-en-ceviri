# google translate kullanarak ingilizce cümleleri türkçeye çeviriren telegram botu

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters   # gerekli kütüphaneleri import eder
from telegram import ReplyKeyboardMarkup                                    # klavye oluşturmak için gerekli kütüphane
import requests                                                             # http istekleri için
import json                                                                 # json formatı için gerekli kütüphane

TOKEN = "TELEGRAM_BOTUNUN_TOKEN_ADRESI"                                     # TOKEN yerine botunuzun tokenini yazın

def start(update, context):                                                 # /start komutu
    update.message.reply_text("Merhaba, ben Google Translate botuyum. Beni kullanmak için /help yazabilirsin.")


def help(update, context):                                                  # /help komutu
    update.message.reply_text("İngilizce cümlelerinizi Türkçeye çevirmek için /translate yazabilirsiniz.")


def translate(update, context):                                             # /translate komutu
    update.message.reply_text("Çevirmek istediğiniz cümleyi yazınız.")
    return 1                                                                # translate2 fonksiyonuna geçiş yapar


def translate2(update, context):                                            # /translate komutu ile gelen cümleyi çevirir
    text = update.message.text                                              # gelen cümleyi text değişkenine atar
                                                                            # google translate api adresi
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=tr&dt=t&q=" + text
    response = requests.get(url)                                            # url adresine get isteği atar
    json_data = json.loads(response.text)                                   # gelen cevabı json formatına çevirir
    update.message.reply_text(json_data[0][0][0])                           # cevabın ilk kelimesini gönderir
    print("Çeviri yapıldı...")


def main():                                                                 # botu çalıştırır
    updater = Updater(TOKEN, use_context=True)                              # updater nesnesi oluşturur
    dp = updater.dispatcher                                                 # dispatcher nesnesi oluşturur
    dp.add_handler(CommandHandler("start", start))                          # /start komutu için start fonksiyonunu çalıştırır
    dp.add_handler(CommandHandler("help", help))                            # /help komutu için help fonksiyonunu çalıştırır
    dp.add_handler(CommandHandler("translate", translate))                  # /translate komutu için translate fonksiyonunu çalıştırır
    dp.add_handler(MessageHandler(Filters.text,
                                  translate2))                              # translate fonksiyonu ile gelen cümleyi translate2 fonksiyonuna gönderir
    updater.start_polling()                                                 # botu çalıştırır
    print("Bot başlatıldı.")
    updater.idle()                                                          # botu durdurur
    print("Bot durduruldu!")


if __name__ == '__main__':                                                  # main fonksiyonunu çalıştırır
    main()

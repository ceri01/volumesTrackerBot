import botogram
import parser
import redis
import conf

bot = botogram.create("")
r = redis.Redis(
    host=conf.HOST,
    port=conf.PORT,
    password=conf.PASS
)

r.set(bot.itself.id, "INIT")

@bot.command("start")
def start(chat):
    chat.send("benvenuto")
    return r.set(chat.id, "START")

@bot.command("cerca")
def search_command(chat):
    print(r.get(chat.id))
    if r.get(chat.id) == "INIT":
        chat.send("Usare il comando /start per iniziare")
        return
    chat.send("Inserisci il nome del manga.")
    return r.set(chat.id, "SEARCH")

@bot.process_message
def process(chat, message):
    btns = botogram.Buttons()
    index = 0
    if r.get(chat.id) == b'INIT' or r.get(chat.id) != b'SEARCH':
        chat.send("Scrivi /help per vedere i comandi")
        return

    result = parser.create_list(message.text)
    if not result:
        chat.send("Manga non trovato!\nRiprova, potresti aver sbagliato a digitare.")
        return

    for element in result:
        btns[index].callback(str(element.name), "test", element)
        index += 1
    chat.send("Risultati:", attach=btns)

@bot.callback("test")
def selezione_callback(query, data, chat, message):
    chat.send("Manga: " + data)


if __name__ == "__main__":
    bot.run()

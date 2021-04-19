import botogram
import parser

bot = botogram.create("1707074696:AAE3zjvtf2TUWzJwvJn010ULN3YsfPf0Stw")


@bot.command("cerca")
def search_command(chat, message, args):
    btns = botogram.Buttons()
    index = 0
    chat.send("Inserisci il nome del manga.")
    # wait message
    result = parser.create_list(message.text)  # insert recived message
    if not result:
        chat.send("Manga non trovato!\nRiprova, potresti aver sbagliato a digitare.")

    for element in result:
        btns[index].callback(element.name, "selezione", element)


@bot.callback("selezione")
def select_callback(quary, data, chat, message):
    chat.send(data.name + ":\nAlbi presenti: " + data.disp + ".\nAlbi mancanti: " + data.manc)


if __name__ == "__main__":
    bot.run()

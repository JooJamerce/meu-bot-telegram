from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CallbackQueryHandler

# Substitua 'SEU_TOKEN_AQUI' pelo token do seu bot
TOKEN = '7945218141:AAFYmUqfO3sDG95N0ZbzM_8iAa7H2BjudmU'

async def send_welcome(update, context):
    # Criando um botão com a mensagem
    keyboard = [
        [InlineKeyboardButton("Clique aqui para começar", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Enviando a mensagem com o botão assim que a pessoa começar a conversar com o bot
    await update.message.reply_text('Seja VIP de ⚪️Conteúdos Raros⚪️ e tenha acesso a todos os vídeos sem cortes!', reply_markup=reply_markup)

async def button(update, context):
    query = update.callback_query
    await query.answer()

    # Enviar a mensagem personalizada quando o botão for pressionado
    await query.edit_message_text(
        text="Seja VIP de ⚪️Conteúdos Raros⚪️ e tenha acesso a todos os vídeos sem cortes! "
             "Faça um pix no valor de 16,00R$ para chave imjoojj@gmail.com e envie o comprovante para @imjooj para conseguir acesso imediato (opcional)."
    )

def main():
    # Criação do Application
    application = Application.builder().token(TOKEN).build()

    # Handler para qualquer mensagem recebida (não precisa de /start)
    application.add_handler(MessageHandler(filters.TEXT, send_welcome))

    # Handler para o clique no botão
    application.add_handler(CallbackQueryHandler(button))

    # Iniciando o bot
    print("Bot está rodando...")
    application.run_polling()

if __name__ == '__main__':
    main()

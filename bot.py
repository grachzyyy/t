import logging
import random
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Вставьте сюда токен вашего бота
TOKEN = '7269595996:AAFGD4t-0xlqsn03oToJDhl97x_23ohdtj8'

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levellevel)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Путь к папке с изображениями
IMAGE_FOLDER = r'/img'
IMAGE_FOLDERS = r'/images'

# Функция для получения списка изображений из папки
def get_images():
    images = []
    for filename in os.listdir(IMAGE_FOLDERS):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            images.append(os.path.join(IMAGE_FOLDERS, filename))
    return images

# Функция для получения случайного процента ставки
def get_random_bet_percentage():
    return random.choice(['15%', '20%', '30%', '25%', '35%'])

# Функция для обработки команды /start
async def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("🧿Пройти алгоритм", callback_data='start_algorithm')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправка конкретного изображения с нужным сообщением
    image_path = os.path.join(IMAGE_FOLDER, r'photo_2024-06-21_16-04-20.jpg')
    with open(image_path, 'rb') as image_file:
        message = await update.message.reply_photo(
            photo=image_file,
            caption=('Добро пожаловать, Ты уже в шаге от своего ВЫИГРЫША!😉\n\n'
                     'Для того чтобы подвязать свой аккаунт к нашему боту и '
                     'получать БЕСПЛАТНЫЕ ЭКСКЛЮЗИВНЫЕ СИГНАЛЫ с помощью которых '
                     'ты сможешь делать крупные ВЫИГРЫШИ, необходимо выполнить '
                     'определённый алгоритм действий.\n\n'
                     '🔜 Нажимай на кнопку "🧿 Пройти алгоритм" для продолжения.'),
            reply_markup=reply_markup
        )
        context.user_data['last_message_id'] = message.message_id

# Функция для удаления предыдущего сообщения
async def delete_previous_message(context: CallbackContext, chat_id: int):
    if 'last_message_id' in context.user_data:
        last_message_id = context.user_data['last_message_id']
        await context.bot.delete_message(chat_id=chat_id, message_id=last_message_id)

# Функция для обработки нажатия на кнопку "Пройти алгоритм"
async def start_algorithm(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    # Удаление предыдущего сообщения
    await delete_previous_message(context, query.message.chat_id)
    
    image_path = os.path.join(IMAGE_FOLDER, r'photo_2024-06-21_16-19-47.jpg')
    with open(image_path, 'rb') as image_file:
        message = await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=image_file,
            caption=('Шаг 1 - Зарегистрируйся.\n\n'
                     '🧿Для синхронизации с нашим ботом необходимо зарегистрировать НОВЫЙ аккаунт по ранее неиспользованному '
                     'на этом сайте номеру телефона, а также без использования социальных сетей.\n\n'
                     '❕ВНИМАНИЕ❕\n'
                     'ЕСЛИ У ВАС УЖЕ ЕСТЬ АККАУНТ НА 1win, ВЫЙДИТЕ ИЗ НЕГО, ЗАКРОЙТЕ БРАУЗЕР, ТОЛЬКО ПОТОМ ПЕРЕЙДИТЕ ПО ССЫЛКЕ И ПРОЙДИТЕ РЕГИСТРАЦИЮ\n\n'
                     '🔍После завершения регистрации, нажмите кнопку "Проверить регистрацию".'),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🌐Сайт для регистрации", url='https://1wqsg.com/?open=register&p=3zvs')],
                [InlineKeyboardButton("🔍Проверить регистрацию", callback_data='check_registration')]
            ])
        )
        context.user_data['last_message_id'] = message.message_id

# Функция для обработки нажатия на кнопку "Проверить регистрацию"
async def check_registration(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    # Удаление предыдущего сообщения
    await delete_previous_message(context, query.message.chat_id)
    
    image_path = os.path.join(IMAGE_FOLDER, r'photo_2024-06-21_19-13-37.jpg')
    with open(image_path, 'rb') as image_file:
        message = await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=image_file,
            caption=('Шаг 2 - Сделайте первый депозит.\n\n'
                     '💼 От депозита зависит ваши LVL (уровень) в боте, статус и вероятность успеха сигнала. Чем больше депозит, тем выше ваш LVL в боте, а чем выше ваш уровень в боте, тем больше сигналов с высокой вероятностью успеха вы будете получать.\n\n'
                     '💳 Активируйте свой счет, сделав первый депозит. Эти средства будут зачислены на ВАШ СЧЕТ, после чего вы сможете использовать их для игры и, что самое главное, выигрыша.\n\n'
                     '🔍После внесения первого депозита нажмите кнопку "Проверить депозит".'),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🌐Открыть сайт", url='https://1wqsg.com/?open=register&p=3zvs')],
                [InlineKeyboardButton("🔍Проверить депозит", callback_data='check_deposit')]
            ])
        )
        context.user_data['last_message_id'] = message.message_id

# Функция для обработки нажатия на кнопку "Проверить депозит"
async def check_deposit(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    
    # Удаление предыдущего сообщения
    await delete_previous_message(context, query.message.chat_id)
    
    message = await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='🎰',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Получить сигнал", callback_data='get_signal')]
        ])
    )
    context.user_data['jackpot_message_id'] = message.message_id

# Функция для обработки нажатия на кнопку "Получить сигнал"
async def get_signal(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    # Удаление сообщения с кнопкой "Получить сигнал"
    if 'jackpot_message_id' in context.user_data:
        await context.bot.delete_message(chat_id=query.message.chat_id, message_id=context.user_data['jackpot_message_id'])
        del context.user_data['jackpot_message_id']

    images = get_images()
    if images:
        random_image = random.choice(images)
        bet_percentage = get_random_bet_percentage()

        caption = (f"🔮 Сигнал на следующий раунд:\n\n"
                   f"⏳ Срок действия: 90 секунд\n"
                   f"💶 Ставим: {bet_percentage} от банка\n\n"
                   f"Играть строго с нового аккаунта, получив при этом все бонусы по кнопке ниже 👇🏻")

        # Добавляем кнопки "Обновить сигнал", "Сделать ставку" и "Получить бонус"
        keyboard = [
            [InlineKeyboardButton("Обновить сигнал", callback_data='get_signal')],
            [InlineKeyboardButton("Сделать ставку", url='https://1wqsg.com/v3/2158/1win-mines?p=054h')],
            [InlineKeyboardButton("Получить бонус", url='https://telegra.ph/svvvcu-06-21')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Проверяем, есть ли ранее отправленное сообщение с фото
        if query.message.photo:
            # Обновляем сообщение с новым фото и подписью
            media = InputMediaPhoto(media=open(random_image, 'rb'), caption=caption)
            await query.edit_message_media(media, reply_markup=reply_markup)
        else:
            # Отправляем новое сообщение с фото и подписью
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(random_image, 'rb'), caption=caption, reply_markup=reply_markup)
    else:
        await query.edit_message_text("В папке нет изображений.", reply_markup=None)

# Новая функция для команды /get_jackpot
async def signal(update: Update, context: CallbackContext):
    # Удаление команды /get_jackpot
    await update.message.delete()
    
    message = await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='🎰',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Получить сигнал", callback_data='get_signal')]
        ])
    )
    context.user_data['jackpot_message_id'] = message.message_id

def main():
    # Создание объекта приложения
    application = Application.builder().token(TOKEN).build()

    # Обработка команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("signal", signal))
    application.add_handler(CallbackQueryHandler(start_algorithm, pattern='start_algorithm'))
    application.add_handler(CallbackQueryHandler(check_registration, pattern='check_registration'))
    application.add_handler(CallbackQueryHandler(check_deposit, pattern='check_deposit'))
    application.add_handler(CallbackQueryHandler(get_signal, pattern='get_signal'))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()

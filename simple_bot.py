import os
import random
from datetime import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Telegram Bot token (getting from environment variables or using a placeholder)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "YOUR_TOKEN_HERE")

# Dictionary to store user job information
user_jobs = {}

# Collection of daytime reminders
DAYTIME_REMINDERS = [
    "⚔️ Напоминание воина: Как продвигается твоя битва сегодня? Помни о своих целях и оставайся сосредоточенным.",
    "🔥 Середина дня - время проверить свой прогресс. Ты уже сделал шаг к самосовершенствованию сегодня?",
    "🛡️ Воин-напоминание: Сделай паузу на 2 минуты. Глубоко вдохни. Почувствуй свою силу. Продолжай сражаться.",
    "⏱️ Взгляни на свои приоритеты. Что действительно важно сделать до конца дня? Сконцентрируйся на этом.",
    "💧 Момент осознанности: Сделай глоток воды. Почувствуй, как она течет. Вернись к настоящему моменту."
]

async def morning_job(context: ContextTypes.DEFAULT_TYPE):
    """Send the morning motivation message."""
    try:
        chat_id = context.job.chat_id
        await context.bot.send_message(
            chat_id=chat_id,
            text="Вставай, воин. Вот твой путь на сегодня:\n\n"
                 "Тема: Контроль над импульсом\n"
                 "1. Откажись от одной слабости.\n"
                 "2. Замечай импульсы. Наблюдай, не действуй.\n"
                 "3. Сделай одно действие, которое обычно откладываешь.\n\n"
                 'Фраза дня: "Я выбираю делать то, что делает меня сильнее, а не то, что легче."'
        )
    except Exception as e:
        print(f"Error sending morning message: {e}")

async def daytime_reminder_job(context: ContextTypes.DEFAULT_TYPE):
    """Send a daytime reminder message."""
    try:
        chat_id = context.job.chat_id
        reminder = random.choice(DAYTIME_REMINDERS)
        await context.bot.send_message(
            chat_id=chat_id,
            text=reminder
        )
        print(f"Sent daytime reminder to chat {chat_id}")
    except Exception as e:
        print(f"Error sending daytime reminder: {e}")

async def evening_job(context: ContextTypes.DEFAULT_TYPE):
    """Send the evening reflection message."""
    try:
        chat_id = context.job.chat_id
        await context.bot.send_message(
            chat_id=chat_id,
            text="Ты был сегодня сильным?\nЗапиши 3 вещи:\n"
                 "1. Где я победил?\n"
                 "2. Где меня потащило?\n"
                 "3. Как я себя чувствую после самоконтроля?"
        )
    except Exception as e:
        print(f"Error sending evening message: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start the bot and schedule daily messages."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    
    # Remove any existing jobs for this user
    remove_jobs(context, user_id)
    
    # Schedule new jobs
    morning = context.job_queue.run_daily(
        morning_job, 
        time(hour=8, minute=0), 
        chat_id=chat_id
    )
    
    # Add midday reminder (14:00)
    midday_reminder = context.job_queue.run_daily(
        daytime_reminder_job,
        time(hour=14, minute=0),
        chat_id=chat_id
    )
    
    # Add afternoon reminder (17:00)
    afternoon_reminder = context.job_queue.run_daily(
        daytime_reminder_job,
        time(hour=17, minute=0),
        chat_id=chat_id
    )
    
    evening = context.job_queue.run_daily(
        evening_job, 
        time(hour=22, minute=0), 
        chat_id=chat_id
    )
    
    # Store job references
    user_jobs[user_id] = (morning, midday_reminder, afternoon_reminder, evening)
    
    # Send confirmation message
    await update.message.reply_text(
        "🌟 Бот Воин Мотивации активирован! 🌟\n\n"
        "Вы будете получать:\n"
        "- Утреннюю мотивацию в 8:00\n"
        "- Дневное напоминание в 14:00\n"
        "- Дополнительное напоминание в 17:00\n"
        "- Вечернюю рефлексию в 22:00\n\n"
        "Используйте /stop чтобы приостановить сообщения."
    )

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stop the scheduled messages."""
    user_id = update.effective_user.id
    
    if remove_jobs(context, user_id):
        await update.message.reply_text(
            "Ежедневные сообщения остановлены. Используйте /start чтобы активировать их снова."
        )
    else:
        await update.message.reply_text(
            "У вас нет активных запланированных сообщений.\n"
            "Используйте /start чтобы активировать ежедневные мотивационные сообщения."
        )

def remove_jobs(context, user_id):
    """Remove scheduled jobs for a user."""
    if user_id in user_jobs:
        morning_job, midday_reminder, afternoon_reminder, evening_job = user_jobs[user_id]
        morning_job.schedule_removal()
        midday_reminder.schedule_removal()
        afternoon_reminder.schedule_removal()
        evening_job.schedule_removal()
        del user_jobs[user_id]
        return True
    return False

async def send_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send an immediate reminder."""
    chat_id = update.effective_chat.id
    reminder = random.choice(DAYTIME_REMINDERS)
    await context.bot.send_message(
        chat_id=chat_id,
        text=reminder
    )
    print(f"Sent manual reminder to chat {chat_id}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show help information."""
    help_text = (
        "📱 *Команды Воина Мотивации* 📱\n\n"
        "/start - Активировать ежедневные сообщения (утро, день, вечер)\n"
        "/stop - Приостановить ежедневные сообщения\n"
        "/remind - Получить мотивационное напоминание прямо сейчас\n"
        "/help - Показать эту справочную информацию\n\n"
        "Этот бот создан, чтобы помочь вам в пути личностного роста "
        "через постоянную мотивацию и рефлексию с воинским подходом к самодисциплине."
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

if __name__ == '__main__':
    # Initialize and run the bot
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CommandHandler("remind", send_reminder))
    app.add_handler(CommandHandler("help", help_command))
    
    # Start the bot
    print("Starting bot...")
    app.run_polling()
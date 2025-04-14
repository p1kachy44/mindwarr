import logging
from datetime import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from motivational_content import (
    get_morning_motivation, 
    get_daytime_reminder,
    get_evening_reflection
)

# Get logger
logger = logging.getLogger(__name__)

# Dictionary to store user job information
user_jobs = {}

async def morning_job(context: ContextTypes.DEFAULT_TYPE):
    """Send the morning motivation message."""
    try:
        chat_id = context.job.chat_id
        motivation = get_morning_motivation()
        await context.bot.send_message(
            chat_id=chat_id,
            text=motivation
        )
        logger.info(f"Sent morning motivation to chat {chat_id}")
    except Exception as e:
        logger.error(f"Error sending morning message: {e}")

async def daytime_reminder_job(context: ContextTypes.DEFAULT_TYPE):
    """Send a daytime reminder message."""
    try:
        chat_id = context.job.chat_id
        reminder = get_daytime_reminder()
        await context.bot.send_message(
            chat_id=chat_id,
            text=reminder
        )
        logger.info(f"Sent daytime reminder to chat {chat_id}")
    except Exception as e:
        logger.error(f"Error sending daytime reminder: {e}")

async def evening_job(context: ContextTypes.DEFAULT_TYPE):
    """Send the evening reflection message."""
    try:
        chat_id = context.job.chat_id
        reflection = get_evening_reflection()
        await context.bot.send_message(
            chat_id=chat_id,
            text=reflection
        )
        logger.info(f"Sent evening reflection to chat {chat_id}")
    except Exception as e:
        logger.error(f"Error sending evening message: {e}")

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
    
    logger.info(f"Started scheduled messages for user {user_id}")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stop the scheduled messages."""
    user_id = update.effective_user.id
    
    if remove_jobs(context, user_id):
        await update.message.reply_text(
            "Ежедневные сообщения остановлены. Используйте /start чтобы активировать их снова."
        )
        logger.info(f"Stopped scheduled messages for user {user_id}")
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
    reminder = get_daytime_reminder()
    await context.bot.send_message(
        chat_id=chat_id,
        text=reminder
    )
    logger.info(f"Sent manual reminder to chat {chat_id}")

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

def create_bot(token):
    """Create and configure the bot with handlers."""
    app = ApplicationBuilder().token(token).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CommandHandler("remind", send_reminder))
    app.add_handler(CommandHandler("help", help_command))
    
    return app

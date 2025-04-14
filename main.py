import os
import logging
import sys
import random
from flask import Flask, render_template_string, request, session, url_for

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)

# Sample motivational content from motivational_content.py
MORNING_MOTIVATIONS = [
    {
        "theme": "Discipline",
        "text": "Вставай, воин. Вот твой путь на сегодня:\n\n"
                "Тема: Контроль над импульсом\n"
                "1. Откажись от одной слабости.\n"
                "2. Замечай импульсы. Наблюдай, не действуй.\n"
                "3. Сделай одно действие, которое обычно откладываешь.\n\n"
                'Фраза дня: "Я выбираю делать то, что делает меня сильнее, а не то, что легче."'
    },
    {
        "theme": "Mindfulness",
        "text": "Доброе утро, созидатель. Твой фокус на сегодня:\n\n"
                "Тема: Осознанное присутствие\n"
                "1. Проведи 5 минут в тишине перед началом дня.\n"
                "2. Во время еды отложи телефон и почувствуй вкус.\n"
                "3. Сделай одно дело в полном присутствии без отвлечений.\n\n"
                'Фраза дня: "Моя сила в моем присутствии здесь и сейчас."'
    },
    {
        "theme": "Productivity",
        "text": "Пора действовать. Вот твой план на сегодня:\n\n"
                "Тема: Эффективное движение\n"
                "1. Определи три главные задачи дня.\n"
                "2. Устрани один отвлекающий фактор.\n"
                "3. Работай интервалами: 25 минут фокуса, 5 минут отдыха.\n\n"
                'Фраза дня: "Я не жду идеальных условий. Я создаю результаты."'
    }
]

# Collection of daytime reminders
DAYTIME_REMINDERS = [
    "⚔️ Напоминание воина: Как продвигается твоя битва сегодня? Помни о своих целях и оставайся сосредоточенным.",
    "🔥 Середина дня - время проверить свой прогресс. Ты уже сделал шаг к самосовершенствованию сегодня?",
    "🛡️ Воин-напоминание: Сделай паузу на 2 минуты. Глубоко вдохни. Почувствуй свою силу. Продолжай сражаться.",
    "⏱️ Взгляни на свои приоритеты. Что действительно важно сделать до конца дня? Сконцентрируйся на этом.",
    "💧 Момент осознанности: Сделай глоток воды. Почувствуй, как она течет. Вернись к настоящему моменту.",
    "🧠 Проверь свои мысли: они тебя усиливают или ослабляют? Воин контролирует свой разум.",
    "🏆 Напоминание: Дисциплина - это свобода. Твой выбор сейчас определяет твое будущее.",
    "⚡ Энергетическая перезагрузка: Встань, сделай 10 глубоких вдохов и 10 приседаний. Верни себе энергию воина.",
    "🔄 Проверь, не отклонился ли ты от утреннего плана. Еще есть время вернуться на путь.",
    "🧘 Минута тишины: останови все, закрой глаза и прочувствуй момент. Вернись сильнее."
]

EVENING_REFLECTIONS = [
    "Ты был сегодня сильным?\nЗапиши 3 вещи:\n"
    "1. Где я победил?\n"
    "2. Где меня потащило?\n"
    "3. Как я себя чувствую после самоконтроля?",
    
    "Время вечернего анализа:\n"
    "1. Какое решение сегодня меня усилило?\n"
    "2. Какие эмоции управляли мной сегодня?\n"
    "3. Что я сделаю иначе завтра?",
    
    "Твой день завершается. Подумай:\n"
    "1. Чем я горжусь сегодня?\n"
    "2. Какие привычки я укрепил?\n"
    "3. Как я стал лучше, чем вчера?"
]

def get_morning_motivation():
    """Return a random morning motivation message."""
    return random.choice(MORNING_MOTIVATIONS)["text"]

def get_daytime_reminder():
    """Return a random daytime reminder message."""
    return random.choice(DAYTIME_REMINDERS)

def get_evening_reflection():
    """Return a random evening reflection prompt."""
    return random.choice(EVENING_REFLECTIONS)

# Set up Flask web app for Replit hosting
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "warrior-motivation-secret-key")

@app.route('/')
def index():
    return """
    <html>
    <head>
        <title>Telegram Motivation Bot</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: var(--bs-body-bg);
                color: var(--bs-body-color);
                padding-top: 2rem;
                padding-bottom: 2rem;
            }
            .message-box {
                background-color: var(--bs-dark);
                border-radius: 10px;
                padding: 1rem;
                margin-bottom: 1rem;
                white-space: pre-line;
                border-left: 4px solid var(--bs-info);
            }
            .card {
                margin-bottom: 2rem;
                border: none;
                box-shadow: 0 .5rem 1rem rgba(0,0,0,.15);
            }
            .card-header {
                font-weight: 600;
                background-color: var(--bs-primary-bg-subtle);
                color: var(--bs-primary-text);
            }
            .bot-demo-title {
                border-bottom: 2px solid var(--bs-primary);
                padding-bottom: 0.5rem;
                margin-bottom: 1.5rem;
            }
        </style>
    </head>
    <body data-bs-theme="dark">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-10">
                    <div class="text-center mb-5">
                        <h1 class="display-4">💪 Воин мотивации</h1>
                        <p class="lead">Telegram бот для ежедневного личностного роста с воинским мышлением</p>
                    </div>
                    
                    <div class="card mb-4">
                        <div class="card-header">О боте</div>
                        <div class="card-body">
                            <p>Telegram бот, разработанный для тех, кто стремится укрепить самодисциплину и развить в себе воинский дух. Бот отправляет:</p>
                            <ul>
                                <li>Утренние мотивационные сообщения в 8:00 - чтобы зарядить день силой и целенаправленностью</li>
                                <li>Вечерние подсказки для рефлексии в 22:00 - для анализа достижений и извлечения уроков</li>
                            </ul>
                            <p>Основная идея бота - помочь выработать внутреннюю силу и дисциплину через ежедневную практику самоконтроля и рефлексии.</p>
                        </div>
                    </div>
                    
                    <h2 class="bot-demo-title">Демонстрация сообщений бота</h2>
                    
                    <div class="row">
                        <div class="col-md-4">
                            <div class="card">
                                <div class="card-header">Утреннее сообщение</div>
                                <div class="card-body">
                                    <div class="message-box">""" + get_morning_motivation().replace('\n', '<br>') + """</div>
                                    <a href="/morning" class="btn btn-primary mt-2">Показать другое утреннее сообщение</a>
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-md-4">
                            <div class="card">
                                <div class="card-header">Дневное напоминание</div>
                                <div class="card-body">
                                    <div class="message-box">""" + get_daytime_reminder().replace('\n', '<br>') + """</div>
                                    <a href="/reminder" class="btn btn-primary mt-2">Показать другое напоминание</a>
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-md-4">
                            <div class="card">
                                <div class="card-header">Вечернее сообщение</div>
                                <div class="card-body">
                                    <div class="message-box">""" + get_evening_reflection().replace('\n', '<br>') + """</div>
                                    <a href="/evening" class="btn btn-primary mt-2">Показать другое вечернее сообщение</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card mt-4">
                        <div class="card-header">Команды бота</div>
                        <div class="card-body">
                            <ul class="list-group">
                                <li class="list-group-item d-flex justify-content-between align-items-center">
                                    <span><strong>/start</strong> - Активировать ежедневные сообщения</span>
                                    <span class="badge bg-primary rounded-pill">Основная</span>
                                </li>
                                <li class="list-group-item d-flex justify-content-between align-items-center">
                                    <span><strong>/stop</strong> - Приостановить ежедневные сообщения</span>
                                    <span class="badge bg-secondary rounded-pill">Управление</span>
                                </li>
                                <li class="list-group-item d-flex justify-content-between align-items-center">
                                    <span><strong>/help</strong> - Показать справочную информацию</span>
                                    <span class="badge bg-info rounded-pill">Помощь</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                    
                    <div class="text-center mt-5">
                        <p class="text-muted">Чтобы использовать бота, вам нужно:</p>
                        <ol class="text-start d-inline-block">
                            <li>Получить токен от @BotFather в Telegram</li>
                            <li>Установить зависимости: python-telegram-bot</li>
                            <li>Запустить скрипт bot.py со своим токеном</li>
                        </ol>
                        <div class="mt-3">
                            <a href="https://github.com/your-repo/telegram-motivation-bot" class="btn btn-outline-light mx-2">GitHub репозиторий</a>
                            <a href="https://t.me/BotFather" class="btn btn-outline-info mx-2">Создать бота через BotFather</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/morning')
def morning():
    motivation = get_morning_motivation().replace('\n', '<br>')
    return """
    <html>
    <head>
        <title>Morning Motivation</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: var(--bs-body-bg);
                color: var(--bs-body-color);
                padding-top: 2rem;
                padding-bottom: 2rem;
            }
            .message-box {
                background-color: var(--bs-dark);
                border-radius: 10px;
                padding: 1rem;
                margin-bottom: 1rem;
                white-space: pre-line;
                border-left: 4px solid var(--bs-info);
            }
        </style>
    </head>
    <body data-bs-theme="dark">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="card">
                        <div class="card-header">Утреннее сообщение</div>
                        <div class="card-body">
                            <div class="message-box">""" + motivation + """</div>
                            <div class="mt-3">
                                <a href="/morning" class="btn btn-primary">Еще одно сообщение</a>
                                <a href="/" class="btn btn-secondary">Назад</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/reminder')
def reminder():
    reminder = get_daytime_reminder().replace('\n', '<br>')
    return """
    <html>
    <head>
        <title>Daytime Reminder</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: var(--bs-body-bg);
                color: var(--bs-body-color);
                padding-top: 2rem;
                padding-bottom: 2rem;
            }
            .message-box {
                background-color: var(--bs-dark);
                border-radius: 10px;
                padding: 1rem;
                margin-bottom: 1rem;
                white-space: pre-line;
                border-left: 4px solid var(--bs-info);
            }
        </style>
    </head>
    <body data-bs-theme="dark">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="card">
                        <div class="card-header">Дневное напоминание</div>
                        <div class="card-body">
                            <div class="message-box">""" + reminder + """</div>
                            <div class="mt-3">
                                <a href="/reminder" class="btn btn-primary">Еще одно напоминание</a>
                                <a href="/" class="btn btn-secondary">Назад</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/evening')
def evening():
    reflection = get_evening_reflection().replace('\n', '<br>')
    return """
    <html>
    <head>
        <title>Evening Reflection</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: var(--bs-body-bg);
                color: var(--bs-body-color);
                padding-top: 2rem;
                padding-bottom: 2rem;
            }
            .message-box {
                background-color: var(--bs-dark);
                border-radius: 10px;
                padding: 1rem;
                margin-bottom: 1rem;
                white-space: pre-line;
                border-left: 4px solid var(--bs-info);
            }
        </style>
    </head>
    <body data-bs-theme="dark">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="card">
                        <div class="card-header">Вечернее сообщение</div>
                        <div class="card-body">
                            <div class="message-box">""" + reflection + """</div>
                            <div class="mt-3">
                                <a href="/evening" class="btn btn-primary">Еще одно сообщение</a>
                                <a href="/" class="btn btn-secondary">Назад</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

# This code runs when the script is executed directly
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

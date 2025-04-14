import os
import random

# Sample motivational content
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

def get_evening_reflection():
    """Return a random evening reflection prompt."""
    return random.choice(EVENING_REFLECTIONS)

def generate_html_page():
    """Generate the complete HTML page with Bootstrap styling."""
    morning_msg = get_morning_motivation().replace('\n', '<br>')
    evening_msg = get_evening_reflection().replace('\n', '<br>')
    
    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <title>Telegram Motivation Bot</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #212529;
                color: #f8f9fa;
                padding-top: 2rem;
                padding-bottom: 2rem;
            }}
            .message-box {{
                background-color: #343a40;
                border-radius: 10px;
                padding: 1rem;
                margin-bottom: 1rem;
                white-space: pre-line;
                border-left: 4px solid #0d6efd;
            }}
            .card {{
                margin-bottom: 2rem;
                border: none;
                background-color: #2c3034;
                color: #f8f9fa;
                box-shadow: 0 .5rem 1rem rgba(0,0,0,.15);
            }}
            .card-header {{
                font-weight: 600;
                background-color: #212529;
                color: #0d6efd;
                border-bottom: 1px solid #444;
            }}
            .bot-demo-title {{
                border-bottom: 2px solid #0d6efd;
                padding-bottom: 0.5rem;
                margin-bottom: 1.5rem;
                color: #f8f9fa;
            }}
            .btn-primary {{
                background-color: #0d6efd;
                border-color: #0d6efd;
            }}
            .btn-secondary {{
                background-color: #6c757d;
                border-color: #6c757d;
            }}
            .btn-outline-light {{
                color: #f8f9fa;
                border-color: #f8f9fa;
            }}
            .btn-outline-info {{
                color: #0dcaf0;
                border-color: #0dcaf0;
            }}
            .list-group-item {{
                background-color: #343a40;
                color: #f8f9fa;
                border-color: #444;
            }}
            .badge {{
                font-size: 0.8em;
            }}
            .text-muted {{
                color: #adb5bd !important;
            }}
        </style>
    </head>
    <body>
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
                        <div class="col-md-6">
                            <div class="card">
                                <div class="card-header">Утреннее сообщение</div>
                                <div class="card-body">
                                    <div class="message-box">{morning_msg}</div>
                                    <button class="btn btn-primary mt-2" onclick="refreshMessage('morning')">Показать другое утреннее сообщение</button>
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-md-6">
                            <div class="card">
                                <div class="card-header">Вечернее сообщение</div>
                                <div class="card-body">
                                    <div class="message-box">{evening_msg}</div>
                                    <button class="btn btn-primary mt-2" onclick="refreshMessage('evening')">Показать другое вечернее сообщение</button>
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
                        <ol class="text-start mx-auto" style="display: inline-block;">
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
        
        <script>
            function refreshMessage(type) {{
                // Simulate message refresh with JavaScript
                fetch('/api/' + type)
                    .then(response => response.text())
                    .then(data => {{
                        const boxes = document.querySelectorAll('.message-box');
                        if (type === 'morning') {{
                            boxes[0].innerHTML = data;
                        }} else {{
                            boxes[1].innerHTML = data;
                        }}
                    }});
            }}
        </script>
    </body>
    </html>
    """

def get_api_response(message_type):
    """Get a response for API endpoint."""
    if message_type == 'morning':
        return get_morning_motivation().replace('\n', '<br>')
    elif message_type == 'evening':
        return get_evening_reflection().replace('\n', '<br>')
    else:
        return "Invalid message type"

def application(environ, start_response):
    """Simple WSGI application."""
    path = environ.get('PATH_INFO', '').lstrip('/')
    
    if path == '':
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        return [generate_html_page().encode('utf-8')]
    elif path.startswith('api/'):
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        message_type = path.split('/')[-1]
        return [get_api_response(message_type).encode('utf-8')]
    else:
        status = '404 Not Found'
        headers = [('Content-type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        return [b'Page not found']

if __name__ == '__main__':
    # Run with a simple server for local testing
    from wsgiref.simple_server import make_server
    port = int(os.environ.get('PORT', 5000))
    httpd = make_server('0.0.0.0', port, application)
    print(f"Serving on port {port}...")
    httpd.serve_forever()
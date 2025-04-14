import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
    <head>
        <title>Telegram Motivation Bot</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #121212;
                color: #e0e0e0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .container {
                max-width: 800px;
                padding: 20px;
                background-color: #1e1e1e;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
            }
            h1 {
                color: #bb86fc;
                border-bottom: 1px solid #333;
                padding-bottom: 10px;
            }
            .description {
                margin: 20px 0;
                line-height: 1.6;
            }
            .features {
                background-color: #2d2d2d;
                padding: 15px;
                border-radius: 5px;
                margin: 15px 0;
            }
            .features h3 {
                margin-top: 0;
                color: #03dac6;
            }
            pre {
                background-color: #2d2d2d;
                padding: 10px;
                border-radius: 5px;
                overflow-x: auto;
            }
            .bot-link {
                background-color: #bb86fc;
                color: #000;
                text-decoration: none;
                padding: 10px 20px;
                border-radius: 4px;
                display: inline-block;
                margin-top: 20px;
                font-weight: bold;
            }
            .bot-link:hover {
                background-color: #9d4edd;
            }
            .status {
                margin-top: 15px;
                padding: 10px;
                background-color: #2d2d2d;
                border-radius: 5px;
                border-left: 4px solid #03dac6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>💪 Telegram Motivation Bot</h1>
            
            <div class="description">
                Telegram бот, разработанный для отправки ежедневных утренних мотивационных сообщений и вечерних подсказок для рефлексии, помогающих в личностном росте и самосовершенствовании.
            </div>
            
            <div class="features">
                <h3>Функции</h3>
                <ul>
                    <li>Ежедневные утренние мотивационные сообщения в 8:00</li>
                    <li>Вечерние подсказки для рефлексии в 22:00</li>
                    <li>Простые команды для запуска и остановки запланированных сообщений</li>
                </ul>
            </div>
            
            <div class="features">
                <h3>Команды бота</h3>
                <ul>
                    <li><strong>/start</strong> - Активировать ежедневные сообщения</li>
                    <li><strong>/stop</strong> - Приостановить ежедневные сообщения</li>
                    <li><strong>/help</strong> - Показать справочную информацию</li>
                </ul>
            </div>
            
            <a href="https://t.me/your_bot_username" class="bot-link">Открыть бота в Telegram</a>
            
            <div class="status">
                Статус бота: <strong>Работает</strong>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
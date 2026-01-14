from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Получите эту строку из настроек ВК
CONFIRMATION_TOKEN = "e4fb8b24"  # ← ВСТАВЬТЕ ВАШ КОД ЗДЕСЬ!

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🎮 VK Game Bot</title>
        <style>
            body { font-family: Arial; padding: 40px; text-align: center; }
            .success { color: green; font-size: 24px; font-weight: bold; }
            .url { background: #f0f0f0; padding: 15px; margin: 20px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>🎮 VK Game Bot</h1>
        <p class="success">✅ Сервер работает!</p>
        <p>Confirmation token: <strong>""" + CONFIRMATION_TOKEN + """</strong></p>
        <p>Callback URL для ВК:</p>
        <div class="url">https://ваш-домен.vercel.app/api/callback</div>
        <p>Статус: <span style="color: green;">Готов к подключению ВК</span></p>
    </body>
    </html>
    """

# Эндпоинт для Callback API
@app.route('/api/callback', methods=['POST'])
def callback():
    data = request.json
    
    # ВАЖНО: Проверка от ВК (confirmation)
    if data.get('type') == 'confirmation':
        print(f"Confirmation request: returning {CONFIRMATION_TOKEN}")
        return CONFIRMATION_TOKEN  # ← Возвращаем ТОЧНО эту строку!
    
    # Обработка сообщений
    elif data.get('type') == 'message_new':
        message = data['object']['message']
        user_id = message['from_id']
        text = message['text'].lower()
        
        # Игровая логика
        response = "🎮 Игровой бот ВКонтакте!\n\n"
        response += "Команды:\n"
        response += "• Играть 🎰\n"
        response += "• Баланс 💰\n"
        response += "• Бонус 🎁\n"
        response += "• Помощь ❓"
        
        if "играть" in text:
            import random
            responses = [
                "🎉 Вы выиграли 100 монет!",
                "💰 Ваш выигрыш: 50 монет",
                "😢 Попробуйте ещё раз!",
                "🎰 Джекпот! 500 монет!"
            ]
            response = random.choice(responses)
        
        elif "баланс" in text:
            response = "💰 Ваш баланс: 1500 монет"
        
        elif "бонус" in text:
            response = "🎁 Ежедневный бонус: 200 монет!"
        
        # Возвращаем ответ ВК
        return jsonify({
            'response': response
        })
    
    # Для других событий
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template
import openai

app = Flask(__name__)

from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 配置OpenAI API密钥
app.config['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    
    # 调用OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    
    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    app.run(debug=True)

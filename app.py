from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>OdaNet Formu</title>
  <style>
    body { font-family: Arial; padding: 30px; background: #f3f4f6; color: #111827; }
    form { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); max-width: 400px; margin: auto; }
    input, button { width: 100%; padding: 10px; margin-top: 10px; font-size: 16px; }
    button { background: #6366f1; color: white; border: none; cursor: pointer; }
    h2 { text-align: center; margin-top: 20px; }
  </style>
</head>
<body>
  <form method="post">
    <label>Adınız:</label>
    <input name="name" placeholder="Adınızı yazın" required>
    
    <label>Şehir:</label>
    <input name="city" placeholder="Şehir adı" required>
    
    <label>Bütçe (₺):</label>
    <input name="budget" placeholder="Aylık bütçe" required>

    <button type="submit">Gönder</button>
  </form>

  {% if name %}
    <h2>Merhaba {{ name }}!</h2>
    <p>{{ city }} şehrinde ₺{{ budget }} ile oda aramanız kaydedildi.</p>
  {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    name = city = budget = ""
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        budget = request.form['budget']
        with open("odanet_users.txt", "a") as f:
            f.write(f"{name}, {city}, {budget}\n")
    return render_template_string(html, name=name, city=city, budget=budget)

# REQUIRED for Render to run on the correct port
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

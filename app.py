print("🏠 Odanet'e hoş geldin!")

name = input("Adın nedir? ")
city = input("Hangi şehirde oda arıyorsun? ")
budget = input("Aylık maksimum bütçen nedir? (₺) ")

print("\nMerhaba", name + "!")
print(city, "şehrinde ₺" + budget + " bütçeyle sana uygun odaları arıyoruz...")

# (Future: Here would be AI/Database logic to match listings)
print("📬 En kısa sürede sana uygun ilanları göndereceğiz!")
from flask import Flask, request, render_template_string

app = Flask(__name__)

html = '''
<form method="post">
  Adın: <input name="name"><br>
  Şehir: <input name="city"><br>
  Bütçe: <input name="budget"><br>
  <button type="submit">Gönder</button>
</form>
{% if name %}
  <h2>Merhaba {{ name }}!</h2>
  <p>{{ city }} şehrinde ₺{{ budget }} ile eşleşmeler aranıyor.</p>
{% endif %}
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

if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")
app.run(debug=True, host="localhost", port=5000)
from flask import Flask, request, render_template_string

app = Flask(__name__)

html = '''
<form method="post">
  Adınız: <input name="name"><br>
  Şehir: <input name="city"><br>
  Bütçe (₺): <input name="budget"><br>
  <button type="submit">Gönder</button>
</form>
{% if name %}
  <h2>Merhaba {{ name }}!</h2>
  <p>{{ city }} şehrinde ₺{{ budget }} ile eşleşmeler aranıyor.</p>
{% endif %}
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
   
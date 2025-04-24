from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# HTML form content
form_html = '''
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>OdaNet Formu</title>
  <style>
    body { font-family: Arial; padding: 30px; background: #f3f4f6; color: #111827; }
    form { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }
    input, select, textarea, button {
      width: 100%; padding: 10px; margin-top: 10px; font-size: 16px;
    }
    textarea { resize: vertical; }
    button {
      background: #6366f1; color: white; border: none; cursor: pointer;
    }
    h2 { margin-top: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 5px; }
  </style>
</head>
<body>
  <form method="post">
    <h2>İlan Kategorisi</h2>

    <label for="category">Kategori:</label>
    <select name="category" required>
      <option value="">Seçiniz</option>
      <option value="Konut">Konut</option>
      <option value="İşyeri">İşyeri</option>
      <option value="Arsa">Arsa</option>
    </select>

    <label for="sub_category">Konut Alt Kategori:</label>
    <select name="sub_category" required>
      <option value="">Seçiniz</option>
      <option value="Daire">Daire</option>
      <option value="Stüdyo">Stüdyo</option>
      <option value="Rezidans">Rezidans</option>
    </select>

    <label for="listing_type">Yayın Tipi:</label>
    <select name="listing_type" required>
      <option value="">Seçiniz</option>
      <option value="Kiralık">Kiralık</option>
      <option value="Satılık">Satılık</option>
    </select>

    <h2>İlan Bilgileri</h2>

    <label for="title">İlan Başlığı:</label>
    <input name="title" type="text" placeholder="İlan başlığı girin" required>

    <label for="description">İlan Açıklaması:</label>
    <textarea name="description" rows="4" placeholder="Açıklama girin" required></textarea>

    <button type="submit">Kaydet</button>
  </form>

  {% if message %}
    <p style="text-align:center; margin-top: 30px; color: green;">{{ message }}</p>
  {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        category = request.form.get('category')
        sub_category = request.form.get('sub_category')
        listing_type = request.form.get('listing_type')
        title = request.form.get('title')
        description = request.form.get('description')

        with open("odanet_listings.txt", "a") as f:
            f.write(f"{category}, {sub_category}, {listing_type}, {title}, {description}\n")
        
        message = "İlan başarıyla kaydedildi!"
    
    return render_template_string(form_html, message=message)

# Admin page (basic version — optional for now)
@app.route('/admin')
def admin():
    try:
        with open("odanet_listings.txt", "r") as f:
            lines = f.readlines()
        rows = [line.strip().split(', ') for line in lines]
    except FileNotFoundError:
        rows = []

    admin_html = '''
    <html>
    <head>
      <title>İlan Listesi</title>
      <style>
        body { font-family: Arial; padding: 30px; background: #f3f4f6; }
        table { width: 90%; max-width: 800px; margin: auto; border-collapse: collapse; background: white; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: center; }
        th { background-color: #6366f1; color: white; }
        h2 { text-align: center; margin-bottom: 20px; }
      </style>
    </head>
    <body>
      <h2>İlanlar</h2>
      <table>
        <tr><th>Kategori</th><th>Alt Kategori</th><th>Tip</th><th>Başlık</th><th>Açıklama</th></tr>
        {% for row in rows %}
          <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
            <td>{{ row[4] }}</td>
          </tr>
        {% endfor %}
      </table>
    </body>
    </html>
    '''
    return render_template_string(admin_html, rows=rows)

# Run on Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

form_html = '''
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
'''

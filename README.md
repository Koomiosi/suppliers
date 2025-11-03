# Django Customer & Order Management System

Tämä Django-pohjainen sovellus hallinnoi asiakkaita, tuotteita, toimittajia ja tilauksia.  
Sovellus sisältää sekä tavallisen käyttäjän että superuserin oikeudet.

---

## 📌 Ominaisuudet

### Asiakkaat
- Listaa kaikki asiakkaat.
- Lomake uuden asiakkaan lisäämiseen.
- Jokaiselle asiakkaalle:
  - **Make Order** – Luo tilaus kyseiselle asiakkaalle.
  - **View Orders** – Näyttää asiakkaan kaikki tilaukset.
  - **Delete** – Poistaa asiakkaan.

### Tuotteet
- Listaa kaikki tuotteet.
- Lomake uuden tuotteen lisäämiseen.
- Tuotteen tiedot: nimi, pakkauskoko, yksikköhinta, varastosaldo, toimittaja.

### Toimittajat
- Listaa kaikki toimittajat.
- Lomake uuden toimittajan lisäämiseen.
- Toimittajan tiedot: yritys, yhteyshenkilö, osoite, puhelin, sähköposti, maa.

### Tilaukset
- Superuser näkee kaikkien käyttäjien tilaukset.
- Tavallinen käyttäjä näkee vain omat tilauksensa.
- Näyttää:
  - Tilausnumero (satunnainen, 8-merkkinen)
  - Asiakas
  - Tuote
  - Pakkauskoko
  - Yksikköhinta
  - Tilattu määrä
  - Subtotal (hinta × määrä)
  - Toimittaja
- Superuser voi poistaa tilauksia.

### Tilausten luominen
- Valitaan tuote dropdown-valikosta.
- Pakkauskoko ja hinta täytetään automaattisesti.
- Määrä voidaan syöttää.
- Varastosaldo vähenee automaattisesti tilauksen jälkeen.
- Lomakkeessa ainoastaan määrä on muokattavissa, hinta on lukittu.

---

## 🧑‍💻 Käyttäjäoikeudet
- **Tavallinen käyttäjä:** näkee ja hallinnoi omia tilauksiaan.
- **Superuser:** näkee ja hallinnoi kaikkia tilauksia ja voi poistaa niitä.

---

## 💾 Tietokanta
- **Models:**
  - `Customer` – asiakkaat
  - `Supplier` – toimittajat
  - `Product` – tuotteet (liittyy toimittajiin)
  - `Order` – tilaukset (liittyy asiakkaisiin, tuotteisiin ja käyttäjiin)
- Subtotal lasketaan tilauksen `quantity` × `unitprice`.
- `ordernumber` generoidaan satunnaisesti automaattisesti.

---

## 🖼️ Templates
- `index.html` – pääpohja
- `customers.html` – asiakkaiden lista + lomake
- `add-order.html` – tilauksen luonti tietylle asiakkaalle
- `orders.html` – kaikkien tilauksien lista
- `customer_orders.html` – yksittäisen asiakkaan tilaukset

---

## ⚙️ Asennus

1. **Luo virtuaaliympäristö ja aktivoi se**
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Aplicație de Gestionare a Bugetului

Această aplicație de gestionare financiară a fost construită în Python folosind `tkinter` pentru interfața grafică și `matplotlib` pentru vizualizarea distribuției bugetului. Aplicația permite utilizatorilor să își seteze venitul, să adauge și să elimine categorii din buget, să adauge venit suplimentar și să salveze/încarce bugetul dintr-un fișier JSON.

## Funcționalități

- **Setează Venitul**: Setează venitul total și aplicația va calcula automat 20% din acesta pentru economii.
- **Adaugă/Șterge Categorie**: Utilizatorii pot adăuga categorii personalizate (precum "Mâncare", "Distracție", etc.) și să specifice sumele alocate pentru fiecare.
- **Urmărește Suma Rămasă**: Suma rămasă este actualizată automat și afișată.
- **Vizualizare Buget**: Un grafic tip bară este afișat pentru a arăta distribuția bugetului.
- **Adaugă Venit Suplimentar**: Utilizatorii pot adăuga venit suplimentar, iar 20% din această sumă va fi adăugată automat la economii.
- **Salvează/Încarcă Bugetul**: Bugetul poate fi salvat într-un fișier JSON și încărcat înapoi în aplicație.
- **Avertizare Zero Rămas**: Dacă suma rămasă este zero, se afișează o imagine care indică faptul că întregul venit a fost utilizat.

## Cerințe

Pentru a rula această aplicație, vei avea nevoie de următoarele biblioteci Python:

- `tkinter`: pentru interfața grafică
- `matplotlib`: pentru crearea graficului de distribuție a bugetului
- `PIL` (Pillow): pentru manipularea imaginilor (afișarea imaginii de "zero balance")
- `json`: pentru salvarea și încărcarea datelor bugetului în format JSON

Poți instala bibliotecile necesare folosind `pip`:

```bash
pip install matplotlib pillow

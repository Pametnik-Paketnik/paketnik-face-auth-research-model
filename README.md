# Sistem za prepoznavanje obrazov

## O projektu

Ta projekt predstavlja sistem za prepoznavanje obrazov, ki uporablja strojno učenje za zaznavanje in klasifikacijo obrazov v videoposnetkih. Sistem je razvit kot del šolskega projekta in vključuje celoten proces od priprave podatkov do testiranja modela.

## Ekipa

- **Jakob Mlakar** - Razvoj modela, optimizacija in OpenCV programi za zajemanje obrazov
- **Nikola Mitrovic** - Obdelava podatkov in testiranje  
- **Vito Senic** - Integracija sistema in dokumentacija

## Funkcionalnosti

- ✅ Ekstrakcija sličic iz videoposnetkov
- ✅ Predobdelava in čiščenje podatkov
- ✅ Treniranje modelov nevronskih mrež
- ✅ Testiranje na posameznih videoposnetkih
- ✅ Testiranje na več videoposnetkih hkrati
- ✅ Zaznavanje in prepoznavanje obrazov v realnem času

## Struktura projekta

```
notebooks/
├── prepare_LFW_falsedataset_for_training.ipynb # Priprava negativnih podatkov (LFW)
├── prep_data.ipynb                             # Obdelava podatkov iz videoposnetkov
├── prep_data_videos.ipynb                      # Dodatna obdelava video podatkov
├── mod_training.ipynb                          # Treniranje glavnega modela
└── mod_training_videos.ipynb                   # Treniranje in testiranje na videoposnetkih

scripts/
├── face_capture.py      # OpenCV program za zajemanje obrazov (Jakob)
├── face_processing.py   # Obdelava in procesiranje obrazov
└── face_augumentation.py # Povečavanje podatkovne množice

data/
├── raw/                # Surovi podatki
├── processed/          # Obdelani podatki
└── models/            # Shranjeni modeli
```

## Uporabljene tehnologije

- **Python 3.10+**
- **TensorFlow/Keras** - Strojno učenje
- **OpenCV** - Računalniški vid
- **MediaPipe** - Zaznavanje obrazov
- **NumPy & Pandas** - Obdelava podatkov
- **Matplotlib** - Vizualizacija

## Namestitev

1. Kloniraj repozitorij:
```bash
git clone [URL_REPOZITORIJA]
cd test-python-auth
```

2. Namesti odvisnosti:
```bash
pip install -r requirements.txt
```

3. Zaženi Jupyter notebook:
```bash
jupyter notebook
```



---
*Projekt razvit v okviru študija na [Fakulteta za racunalnistvo in informatiko FERI v Mariboru] - [2025]* 
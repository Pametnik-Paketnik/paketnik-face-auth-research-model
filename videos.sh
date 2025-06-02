#!/bin/bash

# Pot do mape z videi (zamenjaj s svojo potjo)
VIDEO_FOLDER="./data/raw/videos/train"

# Seznam podprtih video razširitev
VIDEO_EXTENSIONS="*.mp4 *.mkv *.avi *.mov *.wmv *.flv *.webm"

# Inicializiraj spremenljivko za skupno dolžino
TOTAL_DURATION=0

echo "Preverjam videoposnetke v mapi: $VIDEO_FOLDER"
echo "-------------------------------------"

# Spremeni se v mapo z videi
cd "$VIDEO_FOLDER" || { echo "Napaka: Mapa '$VIDEO_FOLDER' ne obstaja ali ni dostopna."; exit 1; }

# Zanka skozi vse video datoteke
for video_file in $VIDEO_EXTENSIONS; do
    # Preveri, ali je datoteka dejansko obstaja (pomembno, če ni videov z določeno razširitvijo)
    if [ -f "$video_file" ]; then
        # Pridobi dolžino videa z ffprobe
        duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$video_file")

        # Preveri, ali je ffprobe vrnil veljavno številko
        if [[ "$duration" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
            # Izpiši dolžino posameznega videa (zaokroženo na 2 decimalni mesti)
            printf "Video '%s' traja %.2f sekund.\n" "$video_file" "$duration"
            # Dodaj k skupni dolžini (za bash je potrebna aritmetična operacija z 'bc' za decimalna števila)
            TOTAL_DURATION=$(echo "$TOTAL_DURATION + $duration" | bc)
        else
            echo "Opozorilo: Ni mogoče pridobiti dolžine za '$video_file' (morda ni veljaven video)."
        fi
    fi
done

echo "-------------------------------------"
printf "Skupna dolžina vseh videoposnetkov: %.2f sekund.\n" "$TOTAL_DURATION"
echo "-------------------------------------"

# Izračun 70/15/15 % delitev
# Uporabimo 'bc' za decimalne izračune
PERCENTAGE_70=$(echo "scale=2; $TOTAL_DURATION * 0.70" | bc)
PERCENTAGE_15_1=$(echo "scale=2; $TOTAL_DURATION * 0.15" | bc)
PERCENTAGE_15_2=$(echo "scale=2; $TOTAL_DURATION * 0.15" | bc)

echo "Razdelitev skupne dolžine:"
printf "  70%% delež: %.2f sekund\n" "$PERCENTAGE_70"
printf "  15%% delež: %.2f sekund\n" "$PERCENTAGE_15_1"
printf "  15%% delež: %.2f sekund\n" "$PERCENTAGE_15_2"
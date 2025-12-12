import json
import argparse
import os

def json_to_m3u(json_data, output_file):
    """
    Converte una lista JSON di canali IPTV in un file M3U.

    :param json_data: Lista JSON contenente i dati dei canali.
    :param output_file: Nome del file M3U di output.
    """
    with open(output_file, 'w', encoding='utf-8') as m3u_file:
        # Scrivi l'intestazione del file M3U
        m3u_file.write("#EXTM3U\n")
        
        # Itera attraverso ogni canale nel JSON
        for channel in json_data:
            # Estrai le informazioni del canale
            group = channel.get("channeldata","area", "")
            name = channel.get("channeldata""channelname", "")
            logo = channel.get("channeldata","logo", "")
            tvg_id = channel.get("tvg_id", "")
            url = channel.get("playbackurl", "")
            
            # Scrivi le informazioni del canale nel file M3U
            m3u_file.write(f'#EXTINF:-1 group-title="{group}" tvg-id="{tvg_id}" tvg-logo="{logo}",{name}\n')
            m3u_file.write(f'{url}\n')

def main():
    # Configura il parser degli argomenti
    parser = argparse.ArgumentParser(description="Converti un file JSON di canali IPTV in un file M3U.")
    parser.add_argument("input_file", help="Percorso del file JSON di input")
    args = parser.parse_args()

    # Verifica che il file di input esista
    if not os.path.exists(args.input_file):
        print(f"Errore: Il file {args.input_file} non esiste.")
        return

    # Carica il file JSON
    with open(args.input_file, 'r', encoding='utf-8') as json_file:
        json_data = json.load(data/tamilott.m3u)

    # Genera il nome del file di output
    base_name = os.path.splitext(args.input_file)[0]  # Rimuove l'estensione .json
    output_file = f"{base_name}.m3u"

    # Converti il JSON in M3U e salva il file
    json_to_m3u(json_data, output_file)
    print(f"File M3U generato con successo: {output_file}")

if __name__ == "__main__":
    main()

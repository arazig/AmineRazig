import os
import requests

# Créer le dossier images s'il n'existe pas
os.makedirs('images', exist_ok=True)

# URLs des images à télécharger
image_urls = {
    'linkedin.png': 'https://cdn-icons-png.flaticon.com/512/174/174857.png',
    'github.png': 'https://cdn-icons-png.flaticon.com/512/25/25231.png',
    'email.png': 'https://cdn-icons-png.flaticon.com/512/561/561127.png',
    'education.png' : 'https://cdn-icons-png.flaticon.com/512/3145/3145765.png',
'work.png' : 'https://cdn-icons-png.flaticon.com/512/3135/3135715.png',
'research.png' :'https://cdn-icons-png.flaticon.com/512/4248/4248443.png'
}

# Téléchargement des images
for filename, url in image_urls.items():
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Vérifie que le téléchargement a réussi
        
        with open(f'images/{filename}', 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"✅ {filename} téléchargé avec succès")
    except Exception as e:
        print(f"❌ Erreur lors du téléchargement de {filename}: {e}")

print("Téléchargement terminé!")
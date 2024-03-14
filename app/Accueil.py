# Function to write the content into a file
def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Content to be written
content = """
Projet Nostradamus : Analyse des dernières élections européennes et prédiction pour 2024 (emoji magicien ou boule de cristal)
Les élections européennes sont l’occasion pour les citoyens de participer activement à la vie démocratique de l’Union européenne et d’influencer les décisions qui impactent leur quotidien. Alors, allons voter !

Projet de 2 semaines dans le cadre de la formation du Wagon en data analytics
Comprendre les élections européennes et leurs enjeux
Contexte électoral français
Décryptage des votes : Comprendre les tendances électorales
Étude de cas : Focus sur la Haute Garonne
Prédictions pour les élections européennes de 2024

N’oublions pas que ces prédictions sont basées sur des tendances actuelles et peuvent évoluer. Restons attentifs aux développements politiques et aux changements sociodémographiques pour affiner nos prévisions.
"""

# Path to the file
file_path = "welcome_page.txt"

# Writing content to the file
write_to_file(file_path, content)

print("Content has been written to", file_path)


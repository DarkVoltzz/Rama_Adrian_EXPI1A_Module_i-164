from flask import Flask
import pymysql



app = Flask(__name__)

# Configuration de la base de données
app.config['MYSQLHOST'] = 'localhost' # Adresse IP ou nom d'hôte du serveur MySQL
app.config['MYSQLUSER'] = 'root'  # Nom d'utilisateur MySQL
app.config['MYSQLPASSWORD'] = ''  # Mot de passe MySQL
app.config['MYSQL_DB'] = 'rama_adrian_expi1a_i164'  # Nom de la base de données

# Établir une connexion à la base de données
conn = pymysql.connect(host=app.config['MYSQLHOST'],
                       user=app.config['MYSQLUSER'],
                       password=app.config['MYSQLPASSWORD'],
                       database=app.config['MYSQL_DB'])

# Créer un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exemple : exécution d'une requête pour récupérer toutes les lignes d'une table nommée 'ma_table'
cursor.execute("SELECT * FROM applications")
rows = cursor.fetchall()

# Parcourir les résultats
for row in rows:
    print("fait chier ce module",row)

# Fermer le curseur et la connexion à la base de données
cursor.close()
conn.close()

if __name__ == '__main__':
    app.run()
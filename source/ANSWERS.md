Que pensez-vous de la confidentialité des données vis à vis du serveur?
La confidentialité des données n'est pas garantie car les messages sont envoyés en clair entre les clients et le serveur,une interception des paquets permettrait de lire toutes les communications et l'absence de chiffrement expose les utilisateurs à des attaques de type "Man-in-the-Middle" (MITM).


Pouvez vous expliquer en quoi la sérialisation pickle est certainement le plus mauvais choix ?
parceque le pickle permet l'exécution de code arbitraire lorsqu'un objet est désérialisé et un attaquant peut injecter un objet malveillant exécutant du code à la réception.


 Quels types de sérialisation pourrait-on utiliser pour éviter cela ? (hors CVE)
Pour éviter les problèmes de sécurité liés à pickle, il est recommandé d'utiliser des formats de sérialisation sûrs comme JSON, MsgPack ou Protocol Buffers. Contrairement à pickle, ces formats ne permettent pas l'exécution de code arbitraire lors de la désérialisation, ce qui les rend plus sécurisés


Pourquoi le chiffrement seul est-il insuffisant?
Le chiffrement seul protège la confidentialité, mais pas l'intégrité. Un attaquant peut modifier un message chiffré et le réinjecter sans être détecté


Quelle fonction? en python permet de générer un salt avec une qualité cryptographique ?
os.urandom(16) permet de générer un salt aléatoire de manière cryptographiquement sûre.


Faudra t-il transmettre le salt comme champ en clair supplémentaire du paquet message ?
Oui, le salt doit être transmis en clair, mais il ne doit pas être secret. Son rôle est d'empêcher les attaques par pré-calcul (rainbow tables).


Que constatez-vous côté serveur ?
Côté serveur, après avoir implémenté le chiffrement et l'intégrité des messages, on constate que la communication est sécurisée, ce qui empêche un serveur malveillant d'altérer ou de manipuler les messages. Les messages arrivent chiffrés et ne peuvent pas être lus ni modifiés sans la clé de déchiffrement


Que peux faire le serveur si il est malveillant sur les messages ?
Si le serveur est malveillant, il pourrait :

Modifier les messages : Le serveur pourrait altérer le contenu des messages envoyés entre les clients, par exemple en modifiant le texte des messages ou en envoyant de faux messages à un ou plusieurs clients.

Réémettre des messages : Le serveur pourrait réémettre des messages précédemment reçus (en replay) pour perturber la communication ou causer des attaques de type "replay attack".

Intercepter des messages sensibles : Le serveur pourrait lire les messages envoyés entre les clients si ces derniers ne sont pas chiffrés, exposant ainsi des informations sensibles.



Que faudrait-il faire en théorie pour éviter l’action du rogue server ? Pourquoi Fernet n’est 
pas adapté dans ce cadre ?
Fernet assure la confidentialité et l'intégrité, mais ne protège pas contre un serveur malveillant qui pourrait réémettre ou modifier les messages sans être détecté.




Solution simple pour conserver Fernet?

Concaténer le champ nick (nom de l'utilisateur) au message chiffré et vérifier sa cohérence après déchiffrement.

 Est-ce que le rogue serveur fonctionne t-il encore ?

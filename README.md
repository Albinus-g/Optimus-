# Autobot

Ceci est une ARCHIVE, ne lance pas ce bot ![](https://risibank.fr/cache/medias/0/0/86/8618/thumb.png)

Il est glissant et peut être exploité ![](https://risibank.fr/cache/medias/0/7/717/71734/thumb.png)

Note: tu es légalement responsable des posts de tes bots ![](https://risibank.fr/cache/medias/0/7/760/76073/thumb.png)

## Configuration

Avant de lancer le bot, définissez les variables d'environnement suivantes :

- `ONCHE_USERNAME`
- `ONCHE_PASSWORD`
- `ONCHE_ADMIN`
- `REDIS_USERNAME`
- `REDIS_PASSWORD`
- `LOKI_URL`

Le programme vérifie leur présence au démarrage et lève une `RuntimeError` si l'une d'elles est absente.

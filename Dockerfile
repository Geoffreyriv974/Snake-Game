FROM python:3.9

# Copier le script Python dans le conteneur
COPY main.py .
COPY game.py .

RUN pip install mysql-connector-python

# Exécuter le script Python
CMD ["python", "main.py"]

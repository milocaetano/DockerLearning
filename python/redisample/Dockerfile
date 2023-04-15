# Use a imagem oficial do Python 3
FROM python:3

# Defina o diretório de trabalho como /app
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências especificadas em requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o arquivo app.py para o diretório de trabalho
COPY app.py .

# Exponha a porta 5000
EXPOSE 5000

# Inicie o aplicativo
CMD ["python", "app.py"]

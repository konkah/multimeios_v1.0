### Instalando o Python Default

```
sudo apt update
sudo apt install -y python3
sudo apt install -y python3-pip
```

### Instalando uma versão do Python Específica e suas Dependências (Python 3.7.4)

```bash
sudo apt install -y curl #(Serve para visitar páginas da web via terminal)
sudo curl https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz > Python-3.7.4.tar.xz #(Baixar o arquivo compactado Python 3.7.4)
tar -xf Python-3.7.4.tar.xz #(Descompactar o arquivo)
cd /Python3.7.4 #(Entrar no diretório)
sudo apt install libffi-dev libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk libgdm-dev libdb4o-cil-dev libpcap-dev #(Dependências do Python)
sudo ./configure #(Faz a configuração e Build do Python)
#sudo ./configure --enable-optimizations (Opcional)
sudo make altinstall
```
```bash
sudo rm Python-3.7.4.tar.xz #(Remover o arquivo compactado baixado)
sudo rm -r Python-3.7.4 #(Remover o diretório)
```

### Instalando a Virtualenv Default

```bash
sudo pip3 install virtualenv
```

### Criando uma ENV de uma versão Específica (Python 3.7.4)

```bash
which python3.7 #(Mostra o caminho dos diretórios da versão do Python escolhida)
virtualenv -p /usr/local/bin/python3.7 envRES
```

### Ativar e Desativar a ENV

```bash
source envRES/bin/activate
deactivate #(Pode ser digitado em qualquer diretório do terminal enquanto a env estiver ativada)
```

### Dentro da ENV

```bash
python --version #(Ver versão do Python)
python -m pip install -U pip #(Atualizar o Pip)
cd /multimeios
python -m pip install Django #(Instalar o Django do Zero)
python -m django --version ##(Ver versão do Django)
pip install -r requirements.txt #(Instalar um projeto Django, caso você tenha um projeto pronto)
python manage.py migrate
```

### Dentro da ENV - Rodar o Sistema

```bash
cd /multimeios
python manage.py runserver
#Depois ir no Browser e digitar: 127.0.0.1:8000
```

### Instalando o Python Default

```
sudo apt update
sudo apt install -y python3
sudo apt install -y python3-pip
```

### Instalando uma versão do Python Específica e suas Dependências (Python 3.7.4)

```bash
sudo apt install -y curl #(Serve para visitar páginas da web via terminal)
sudo curl https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz > Python-3.7.4.tar.xz #(Baixar a versão Python 3.7.4)
sudo apt install libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk libgdm-dev libdb4o-cil-dev libpcap-dev #(Dependências do Python)

```

### Instalando a Virtualenv Default

```bash
sudo pip3 install virtualenv
```

### Criando uma ENV de uma versão Específica (Python 3.7.4)

```bash
which python3.7 #(Mostra o caminho dos diretórios da versão do Python escolhida)
sudo virtualenv -p /usr/local/bin/python3.7 envRES
```

### Dentro da ENV

```bash
sudo python -m pip install -U pip #(Atualizar o Pip)
pip install mysqlclient
cd /multimeios
python manage.py migrate
cd ..
pip install -r requirements.txt

```

### Dentro da ENV - Rodar o Sistema

```bash
cd /multimeios
python manage.py runserver
Depois ir no Browser e digitar: 127.0.0.1:8000
```

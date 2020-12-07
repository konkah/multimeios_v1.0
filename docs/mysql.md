### Instalando o MySql

```
sudo apt install mysql-server
sudo systemctl status mysql (Verify service status)
sudo mysql_secure_installation
sudo mysql (Login root to mysql)
```

### Instalando MySql Workbench
```
Download configuratio file: https://dev.mysql.com/downloads/repo/apt/
sudo apt install ./mysql-apt-config_*.*.**-*_all.deb
sudo apt update
sudo apt install mysql-workbench-community
mysql-workbench (Launch MySQL Workbench)

```

Então configure o banco de dados local

#### Caso dê acesso negado ao root, mesmo colocando a senha certa

```
sudo mysql -u root -p
```

Vai abrir o terminal do mysql. Dentro do terminal:
```
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '{{sua senha aqui}}'; flush privileges;
```

Caso precise de uma senha simples, ainda dentro do terminal do mysql:
```
SET GLOBAL validate_password_policy=LOW;
```

No caso da LOW, a única exigência é ter 8 caracteres.

#### Caso dê mySQL não encontrado

Comando para colocar as bibliotecas do mysqlclient na env.
```
sudo apt-get install python3-dev libmysqlclient-dev
```

Comando para instalar o mysqlclient na env.
```
pip install mysqlclient
```

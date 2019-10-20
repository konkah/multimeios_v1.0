### Instalando o MySql

```
sudo apt mysql-server
sudo apt mysql-workbench
sudo mysql_secure_installation
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
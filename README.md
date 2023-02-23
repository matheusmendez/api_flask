# Api-Flask

##

## Api de teste para cadastros de veículos utilizando flask, docker e mysql.

- Instalação
```bash
git clone https://github.com/matheusmendez/api_flask.git
```
```bash
cd api_flask/src && sudo docker build -t carros-db .
```

```bash
sudo docker run -d --name carros-db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=RootPassword -e MYSQL_DATABASE=db_carros -e MYSQL_USER=MyUser -e MYSQL_PASSWORD=MyPassword carros-db
```
```bash
poetry install
```
```bash
poetry shell
```
```bash
py app.py
```
- Teste
```bash
curl 127.0.0.1:5000/carros
```

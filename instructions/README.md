# MMMenus :: OVH :: Deploy
Repository for deployment



## Gestion des clés SSH
https://www.ovh.com/manager/#/dedicated/billing/autorenew/ssh

```bash
ssh-keygen -t ed25519 -C "mmmenus_prod"
ssh-keygen -t ed25519 -C "mmmenus_test"
```

## Console VPS
https://www.ovh.com/manager/#/dedicated/vps/vps-b6af1dcf.vps.ovh.net/dashboard 

Nom: `mmmenus-test.vps.ovh.net` 
```
IPv4 135.125.237.244
IPv6 2001:41d0:701:1100::848e
Gateway 2001:41d0:701:1100::1
```

```
Modèle : VPS vps2023-le-2 
vCores : 2
Mémoire :2 Go
Stockage : 40 Go
OS / Distribution : Ubuntu 24.04 
```

## Acces SSH

```bash
ssh -i ~/.ssh/mmmenus_test ubuntu@135.125.237.244
ssh -i ~/.ssh/mmmenus_test ubuntu@test.mmmenus.fr
```

## DNS
https://www.ovh.com/manager/#/web/zone/mmmenus.fr

Créez les 2 entrées `A` et `AAAA`
```
test.mmmenus.fr.
	0 	A 	135.125.237.244
```

```
test.mmmenus.fr.
	0 	AAAA 	2001:41d0:701:1100::848e
```

Test
```bash
ping test.mmmenus.fr
ping6 test.mmmenus.fr
```

## Service de test HTTP (NGINX + PHP7)
TODO

```bash
mkdir  ~/test_nginx/html

echo "
<!doctype html>
<html lang="en">
<head>
<title>MMMenus :: Nginx with Docker Compose</title>
</head>
<body>
<h1>MMMenus</h1>
<h2>Install Nginx using Docker Compose.</h2>
<p>This content is being served by an Nginx Docker container.</p>
</body>
</html>
" > ~/test_nginx/html/index.html
```


`docker-compose.yml`
```yml
version: '3'

services:
 web:
  image: nginx:latest
  ports:
   - "80:80"
  volumes:
   - ./html:/usr/share/nginx/html
  links:
   - php

 php:
  image: php:7-fpm
```


```bash
cd ~/test_nginx
docker compose up -d
```

Browse http://test.mmmenus.fr 

This Banner should be displayed
```
MMMenus
Install Nginx using Docker Compose.

This content is being served by an Nginx Docker container.
```

## Emails
TODO

https://www.ovh.com/manager/#/web/email_domain/mmmenus.fr/email

## Sécurité

[Checklist + Instructions](security.md)

## CI / CD

https://docs.github.com/fr/actions

* Exemple pour VueJS et Flask avec Azure : https://github.com/Azure-Samples/flask-vuejs-webapp/blob/main/.github/workflows/build_and_deploy.yaml

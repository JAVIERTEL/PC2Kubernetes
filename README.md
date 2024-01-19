# Despliegue de una aplicación basada en microservicios utilizando Kubernetes 


3.1 Lo primero que hacemos es subir nuestras imágenes a dockerhub con 
```
docker tag mi_imagen_local:latest tu_usuario_dockerhub/mi_nuevo_nombre:latest
```
```
docker push tu_usuario_dockerhub/nuevo_nombre:tag
```
Para ver las imagenes disponibles:
```
docker images
```
No olvidar que hay que estar logueado
```
docker login
```



3.1 Ahora vamos  a https://console.cloud.google.com/kubernetes y crear un kubernetes en europe-west1 (la más cercana a nuestra localización). Y seleccionaremos connect y seleccionaremos run in cloud Shell. Una vez abierta ya tenemos un cluster de ordenadores donde podemos desplegar Pods, formados por contenedores Docker. Importaremos nuestros archivos yaml y ejecutaremos nuestro script de python

```
python3 ./comandos3.py
```

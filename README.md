# Flask on Kubernetes

Este proyecto consiste en una **aplicación web básica desarrollada con Flask (Python)**, empaquetada en un contenedor Docker y desplegada en un **clúster de Kubernetes**. Además, cuenta con integración de **CI/CD a través de Azure Pipelines**, lo cual permite construir y desplegar la aplicación automáticamente desde GitHub.

## 🚀 Tecnologías utilizadas

- **Python 3.9**
- **Flask**
- **Docker**
- **Kubernetes**
- **Azure Pipelines (CI/CD)**

## 🌐 Descripción de la Aplicación

La aplicación muestra una página HTML sencilla con información sobre su despliegue y características. Se accede desde la raíz (`/`) y fue pensada como parte de un proyecto académico enfocado en redes y despliegue en la nube.

## 📁 Estructura del Proyecto

```bash
mi-aplicacion-python/
├── app.py                 # Aplicación Flask
├── Dockerfile             # Imagen Docker
├── requirements.txt       # Dependencias de Python
└── azure-pipelines.yml    # Definición del pipeline de CI/CD
```

## 🐳 Docker

### Construcción del contenedor:

```bash
docker build -t flask-k8s-app .
```

### Ejecución local:

```bash
docker run -p 8080:80 flask-k8s-app
```

Accede a la aplicación en [http://localhost:8080](http://localhost:8080)

---

## ☸️ Kubernetes

Ejemplo de despliegue (necesitas archivo `deployment.yaml` y `service.yaml`):

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

---

## 🔄 CI/CD con Azure Pipelines

El archivo `azure-pipelines.yml` automatiza:

1. Instalación de dependencias.
2. Construcción de imagen Docker.
3. Publicación de imagen en DockerHub.

> ⚠️ **Importante**: Asegúrate de eliminar o reemplazar cualquier token sensible (como `ghp_XXXXXX`) en los archivos del repositorio.

---

## 📬 Contacto

Para más información puedes visitar [mi perfil de GitHub](https://github.com/ismaoft) o contactarme directamente.

---

## 📝 Licencia

Este proyecto es de uso académico. Puedes adaptarlo libremente para tus propios fines.

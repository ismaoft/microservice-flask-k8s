from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
        <head>
            <title>Mi Aplicación en Kubernetes</title>
        </head>
        <body>
            <h1>Proyecto Redes</h1>
            <p>Bienvenido a mi aplicación desplegada en un clúster de Kubernetes.</p>
            <h2>Sobre la Aplicación</h2>
            <p>Esta es una simple aplicación web construida con Flask.</p>
            <p>La aplicación se ejecuta en un contenedor Docker y está orquestada por Kubernetes en Azure.</p>
            <h2>Características</h2>
            <ul>
                <li>Desarrollada en Python utilizando el framework Flask.</li>
                <li>Contenerizada utilizando Docker.</li>
                <li>Desplegada en un clúster de Kubernetes en Azure.</li>
            </ul>
            <h2>Contacto</h2>
            <p>Para más información, visita <a href="https://github.com/ismaoft/mi-aplicacion-python">nuestro repositorio en GitHub</a>.</p>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

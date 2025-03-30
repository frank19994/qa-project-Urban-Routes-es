🍣 Proyecto QA - Urban Routes (ES)

Este proyecto contiene pruebas automatizadas para la aplicación Urban Routes, desarrolladas con Python, Selenium WebDriver y Pytest.

✨ Descripción del archivo main.py

El archivo main.py incluye:

Una clase UrbanRoutesPage que implementa el patrón Page Object Model (POM) para interactuar con la interfaz de usuario de la aplicación Urban Routes.

Una clase TestUrbanRoutes que contiene pruebas automatizadas secuenciales para simular todo el flujo de uso de la aplicación: desde seleccionar una ruta hasta agregar una tarjeta de pago y enviar un mensaje al conductor.

Una función retrieve_phone_code() para recuperar el código de confirmación de teléfono desde los logs de red de Chrome.

Cada método de UrbanRoutesPage representa una acción o elemento específico de la UI, como ingresar direcciones, seleccionar tarifas, ingresar datos de pago o escribir mensajes.


📃 Descripción del archivo data.py
El archivo data.py contiene los datos de entrada usados en las pruebas automatizadas.
Estos datos son utilizados por los distintos tests dentro de main.py para poblar formularios, simular entradas del usuario y validar comportamientos esperados.


 📆 Tecnologías utilizadas

Python – Lenguaje principal del proyecto.

Selenium WebDriver – Automatización de interacción con el navegador.

Pytest – Framework de pruebas utilizado para organizar y ejecutar los tests.


📅 Requisitos previos

Python 3.8+

Google Chrome

ChromeDriver (versión compatible con tu navegador)

Virtualenv (opcional pero recomendado)


✨ Clonación del repositorio 
cd ~     # Debes estar en tu directorio de inicio
cd projects # Entrar a la carpeta projects

 git clone git@github.com:frank19994/qa-project-Urban-Routes-es.git # Clona el repositorio (no olvides cambiar tu nombre de usuario)

✨ Instalación de dependencias necesarias 

Instala las dependencias necesarias:

```bash
pip install selenium 
pip install pytest


📂 Estructura del proyecto

qa-project-Urban-Routes-es/
├── main.py               # Lógica de pruebas y Page Object principal
├── data.py               # Datos de entrada como direcciones, teléfono, tarjetas
└── README.md             # Este archivo

🧪 Ejecución de pruebas
Puedes ejecutar las pruebas con el siguiente comando:
pytest main.py

O si quieres correr una prueba específica:
pytest main.py::TestUrbanRoutes::test_search_taxi



🧠 Notas adicionales

Las pruebas están diseñadas para ejecutarse en Chrome.

Se utiliza WebDriverWait para esperar elementos de forma robusta.

retrieve_phone_code() extrae el código SMS desde los logs de red para simular autenticación.

Todas las pruebas están escritas como funciones dentro de TestUrbanRoutes siguiendo una secuencia lógica de uso de la app.

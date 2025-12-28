# Sistema de Gestión de Gimnasio (SGG)

## 📋 Descripción del Proyecto
Sistema integral desarrollado en **Python** y **Django** para la administración de centros deportivos. Esta solución permite gestionar el ciclo de vida de los clientes, controlar la vigencia de membresías mediante lógica de negocios y mantener un registro financiero de pagos.

El proyecto fue diseñado con un enfoque en la escalabilidad y la integridad referencial de los datos.

## 🚀 Características Principales
* **Gestión de Clientes:** Registro detallado con validaciones de datos personales.
* **Control de Membresías:** Sistema inteligente que vincula suscripciones a clientes específicos.
    * *Visualización de Estado:* Indicadores visuales automáticos (✅ Activa / ❌ Vencida) en el panel administrativo.
* **Registro Financiero:** Historial de pagos inmutable vinculado al cliente.
* **Admin Panel Robusto:** Interfaz de administración personalizada con filtros avanzados, búsqueda y acciones rápidas.

## 🛠 Tecnologías Utilizadas
* **Lenguaje:** Python 3.12+
* **Framework Web:** Django 6.0
* **Base de Datos:** SQLite (Entorno de Desarrollo) / Extensible a PostgreSQL
* **Arquitectura:** MVT (Model-View-Template)

## ⚙️ Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/gestion-gimnasio.git](https://github.com/tu-usuario/gestion-gimnasio.git)
    cd gestion-gimnasio
    ```

2.  **Crear entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install django
    ```

4.  **Ejecutar migraciones:**
    ```bash
    python3 manage.py migrate
    ```

5.  **Iniciar servidor:**
    ```bash
    python3 manage.py runserver
    ```

## Autor
[Luis Marabolí Quitral] - Desarrollador Full Stack en formación.
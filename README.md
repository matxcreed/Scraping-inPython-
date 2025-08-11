# Scraping en python

YTS Scraping

Este proyecto es un web scraper desarrollado en Python con Scrapy para extraer información de la página YTS y almacenarla en una base de datos MongoDB.
Su objetivo es demostrar cómo implementar un flujo de scraping completo con paginación y uso de user-agent para simular un navegador real.
✨ Características

    Scraping estructurado usando Scrapy.

    Paginación automática para recorrer múltiples páginas de resultados.

    User-Agent personalizado para evitar bloqueos básicos.

    Almacenamiento en MongoDB para guardar la información extraída.

    Código pensado para aprendizaje y uso por hobbistas e estudiantes.

📦 Requisitos

    Python 3.9+

    MongoDB instalado y en ejecución

    Librerías Python:

        scrapy

        pymongo

🚀 Uso

    Clona este repositorio:

git clone https://github.com/matxcreed/YTS-Scraping.git
cd YTS-Scraping

    Configura la conexión a tu base de datos MongoDB en el archivo de configuración del proyecto (por ejemplo, en settings.py).

    Ejecuta el scraper:

scrapy crawl movie

    Verifica que los datos se hayan guardado en tu base de datos MongoDB.

📚 Inspiración

Siempre quise aprender cómo extraer datos de una página web de manera estructurada. Este proyecto es el resultado de experimentar y aplicar conceptos de scraping, almacenamiento de datos y buenas prácticas con Scrapy.

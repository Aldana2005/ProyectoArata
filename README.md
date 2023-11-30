# Arata

## Requisitos

- Python 3.11.6

## Instalación

1. Clona este repositorio:

```bash
   git clone https://github.com/Aldana2005/Arata.git
```

2. Ve al directorio del proyecto:

```bash
   cd Arata
```

3. Crea un entorno virtual (se recomienda usar virtualenv):

  ```bash
     python -m venv venv
```
  
4. Activa el entorno virtual:

  - En Windows:

   ```bash
       cd venv\Scripts
   ```
   ```bash
      activate
   ```

5. Instala las dependencias:

```bash
   pip install -r requirements.txt
```

6. Aplica las migraciones:

```bash
   python manage.py makemigrations
```
```bash
   python manage.py migrate
```

7. Uso
    - Ejecuta el servidor de desarrollo:

```bash
   python manage.py runserver
```
El proyecto estará disponible en http://localhost:8000/.




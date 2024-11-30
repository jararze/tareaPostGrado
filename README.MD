# Plataforma de Donaciones

Este proyecto es una plataforma creada con Django y Django Rest Framework que permite gestionar causas sociales, registrar donaciones, clasificar causas en categorías, y realizar comentarios para fomentar la interacción y transparencia en el sistema.

## **Características del Proyecto**
1. Gestión de **Causas**:
    - Registrar causas con título, descripción, monto objetivo, estado activo/inactivo y categoría asociada.
    - Validación personalizada: El monto objetivo debe ser mayor a 0.

2. Gestión de **Donaciones**:
    - Registrar donaciones asociadas a causas existentes.
    - Validación personalizada: El monto debe ser mayor a 0 y la causa debe estar activa.

3. Gestión de **Categorías**:
   - Clasificar causas en categorías como "Educación", "Salud", etc.
   - **Nuevo**: Filtro para buscar categorías por nombre usando un parámetro de consulta en la API. Ejemplo de uso:
     ```
     /api/categorias?nombre=PALABRA_A_FILTRAR
     ```
     Permite realizar búsquedas dinámicas por nombre dentro del endpoint de categorías.

4. Gestión de **Comentarios**:
    - Los usuarios pueden agregar comentarios a causas específicas.

5. **Usuarios Personalizados**:
    - Modelo de usuario personalizado (`Usuario`) con correos únicos.

6. **API REST**:
    - Endpoints para interactuar con causas, donaciones, categorías, usuarios, y comentarios.
    - API personalizada (`/api/resumen/`) para mostrar un resumen de las donaciones por causa y el total general.

## **Rutas Disponibles**
### Navegación General
- `/`: Landing Page
- `/admin/`: Acceso al panel administrativo (usuario y contraseña: `admin/admin`)
- `/api/`: Punto de acceso principal para las APIs

### Endpoints de la API
- **Causas**: `/api/causas/`
- **Donaciones**: `/api/donaciones/`
- **Categorías**: `/api/categorias/` (Soporta el filtro `nombre`)
- **Comentarios**: `/api/comentarios/`
- **Usuarios**: `/api/usuarios/`
- **Resumen de Donaciones**: `/api/resumen/`
- **Total de Donaciones**: `/api/total_donaciones/`

## **Requisitos del Sistema**
- Python 3.10+
- Django 4.x
- Django Rest Framework

## **Instalación**
1. Clona el repositorio:
   ```bash
   git clone https://github.com/jararze/tareaPostGrado.git
2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate       # En Linux/Mac
    venv\Scripts\activate          # En Windows
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Crea un superusuario si deseas acceder al panel administrativo (opcional):
    ```bash
    python manage.py createsuperuser
    ```

6. Inicia el servidor:
    ```bash
    python manage.py runserver
    ```


## **Usuario y Contraseña del Admin**
- **Usuario**: `admin`
- **Contraseña**: `admin`

---

## **Personalizaciones y Funcionalidades Adicionales**

### **Landing Page**
- Diseñada con **HTML y TailwindCSS**, incluye enlaces a las principales rutas y un resumen de las funcionalidades.

### **Modelos Personalizados**
1. **Usuario**:
    - Modelo personalizado basado en `AbstractUser` con correos únicos.
2. **Causa**:
    - Incluye validaciones y relación con el modelo `Categoria`.
3. **Donación**:
    - Relacionada con causas activas, validación de montos mayores a 0.
4. **Comentario**:
    - Permite a los usuarios agregar mensajes en las causas.

### **Validaciones Personalizadas**
- **Causa**: Validar que el monto objetivo sea mayor a 0.
- **Donación**: Validar que el monto sea mayor a 0 y que la causa esté activa.

### **API Personalizada**
- `/api/resumen/`: Muestra un resumen con el total recaudado y el progreso de cada causa.

---

## **Licencia**
Este proyecto es de uso académico y fue desarrollado como parte de un módulo de Django. Puedes usarlo y adaptarlo libremente con fines educativos.

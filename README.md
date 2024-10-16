# calculadora-python

Este proyecto implementa una calculadora en Python que incluye vulnerabilidades intencionales para el análisis de seguridad estático con SonarQube.

## Funcionalidades
- Suma
- Resta
- Multiplicación
- División

La aplicación web en Python contiene las siguientes vulnerabilidades:

1. **Inyección de Comandos (Command Injection)**:
   - **Descripción**: Permite la ejecución de comandos del sistema a través de la entrada del usuario sin sanitización.
   - **Ruta**: `/run_command?cmd=<comando>`
   - **Exploit**: Acceder a la ruta `/run_command?cmd=ls` para listar archivos del sistema o ejecutar comandos maliciosos como `/run_command?cmd=rm -rf /`.

2. **Cross-Site Scripting (XSS)**:
   - **Descripción**: Permite la ejecución de scripts maliciosos en el navegador del usuario.
   - **Ruta**: `/greet?name=<script>alert('XSS')</script>`
   - **Exploit**: Inyectar código JavaScript en el nombre para ejecutar alertas o realizar ataques de phishing.

3. **Deserialización Insegura (Insecure Deserialization)**:
   - **Descripción**: Permite la ejecución de código arbitrario durante el proceso de deserialización de objetos malformados.
   - **Ruta**: `/deserialize`
   - **Exploit**: Proporcionar un objeto malicioso durante la deserialización que ejecuta código no deseado en el servidor.

4. **Inyección SQL (SQL Injection)**:
   - **Descripción**: Permite que un atacante modifique o consulte la base de datos a través de entradas no sanitizadas.
   - **Ruta**: `/search?query=<consulta_sql>`
   - **Exploit**: Acceder a la ruta `/search?query=' OR 1=1--` para eludir controles de acceso o extraer datos sensibles.

5. **File Path Traversal**:
   - **Descripción**: Permite acceder a archivos fuera del directorio permitido mediante el uso de secuencias de directorios (`../`).
   - **Ruta**: `/view_file?filename=<path>`
   - **Exploit**: Usar `/view_file?filename=../../etc/passwd` para leer archivos fuera del directorio permitido.

6. **Almacenamiento Inseguro de Contraseñas**:
   - **Descripción**: Contraseñas almacenadas en texto plano en lugar de usar una técnica de hash segura.
   - **Ruta**: Almacenamiento en cualquier lugar en la aplicación.
   - **Exploit**: Compromete la seguridad de las cuentas si un atacante tiene acceso a la base de datos.

---

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Immune-Andres/calculadora-python.git
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
3. Ejecutar el proyecto:
   ```bash
   python calculator.py
Autores Andres Arrieta y Carlos Galo

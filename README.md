# **Taller: Inyección SQL Básica - Practica**

## **Introducción**
El objetivo de este taller es permitir que practiquen y comprendan conceptos básicos de seguridad en aplicaciones web, específicamente cómo una inyección SQL puede afectar la integridad de una base de datos y exponer información sensible. A través del desarrollo de un API vulnerable y la simulación de un ataque de inyección SQL, en este taller, podrán aprender a identificar puntos débiles y extraer información.

---


## **1. Teoría Básica**
### ¿Qué es una inyección SQL?
Una inyección SQL es un tipo de vulnerabilidad en las aplicaciones web que permite a un atacante ejecutar código malicioso en la base de datos de la aplicación, lo cual puede dar acceso a información sensible, alterar datos o causar daños.

### ¿Por qué es importante esta seguridad?
Las inyecciones SQL son una de las amenazas más comunes en las aplicaciones web. Aunque los desarrolladores suelen intentar prevenirlo, es fundamental entender cómo funciona para poder proteger mejor tus aplicaciones.

---

## **2. Herramientas de Desarrollo**
Para este taller, utilizaremos:
- **FastAPI**: Para crear un API simple y vulnerable.
- **SQLite**: Como base de datos, ya que es ligero y fácil de manejar.

---


## **3. Configuración del taller**
### **1. Crear el entorno virtual**

```bash
python -m venv .venv
```

### **2. Activar el entorno virtual**

***Desde sistemas basados en Unix***
```bash
source .venv/bin/activate
```

***Desde Windows***
```bash
cd .venv/Scripts
activate.bat
cd ../..
```

### **3. Instalar las dependencias**
```bash
pip install -r requirements.txt
```

### **4. Iniciar la aplicación**
```bash
python main.py
```

---

## **4. Desafío de Inyección SQL: Pensamiento Crítico**

Usualmente para simular una inyección SQL se utilizan multiples herramientas especializadas en el tema, pero para este primer taller no es necesario instalarlas ni configurarlas, puesto que vamos a hacerlo desde 0 de una forma manual, para así entender como funcionan estas herramientas especializadas.

Para ello vamos a comenzar con insertar código directamente en el navegador, y despues crearemos nuestra propia herramienta básica para ello.

### **1. Identificar los diferentes endpoints**

Para el caso de este taller se cuenta con un total de 3 endpoints sin contar el root (`/`).

* `/`: Ruta principal que devuelve un mensaje de bienvenida.
* `/catalogo/{catalogo}`: Ruta que devuelve toda la información de un catalogo.
* `/serie_titulo/{titulo}`: Ruta que devuelve toda la información de un articulo.
* `/dataset/{data}`: Ruta que devuelve toda la información de un dataset.

### **2. Simular el Ataque**

Para simular el ataque vamos a insertar código directamente en el navegador y en la barra de direcciones de nuestro navegador, vamos a comenzar insertar valores para cada uno de los endpoints.

Si bien se desconoce la el valor que cada endpoint puede recibir, vamos a intentar insertar valores que puedan afectar la integridad de la base de datos hasta obtener una vulnerabilidad, para ello vamos a tener que insertar valores que puedan ser utilizados para realizar una inyección SQL.

### **3. Preguntas Generadoras**

- ¿Cómo podrías descubrir la estructura de la base de datos?
- ¿Qué información podría ser sensible en este sistema?
- ¿Cómo probarías si un endpoint es vulnerable a inyección SQL?

### **4. Metodología de Análisis**

- No busques seguir pasos exactos
- Desarrolla tu propia estrategia de investigación
- Documenta cada paso y observación

---

## **5. Entregables**

1. **Documento de Investigación**:
- Documentación de la estrategia de investigación.
- Screenshots de las pruebas realizadas.
- El documento debe explicar detalladamente como realizó el ataque y cuál fue el resultado obtenido.

2. **Creación de Herramienta Ad-Hoc**:
- Descripción detallada de la herramienta.
- Código fuente de la herramienta en GitHub/GitLab o similar.

---

## **6. Conclusión**
Este taller ha demostrado cómo una inyección SQL puede vulnerabilizar una aplicación web y exponer información sensible. Aunque es atractivo practicar estos ataques, es importante recordar que la seguridad debe ser un pilar fundamental en el desarrollo de aplicaciones.

---

## **7. Consideraciones Éticas**
- Primitiva la práctica responsable: solo use herramientas de seguridad en entornos controlados.
- No ataque a aplicaciones reales sin autorización.
- Respetar la privacidad de los datos de otros usuarios.

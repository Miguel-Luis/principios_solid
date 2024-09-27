# 📚 Proyecto de Programación Orientada a Objetos en Python

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

Este proyecto tiene como objetivo enseñar los conceptos fundamentales de la Programación Orientada a Objetos (POO) y los principios SOLID utilizando ejemplos en Python. Organizado en tres secciones principales, este repositorio ofrece ejemplos claros y prácticos.

## 🚀 Estructura del Proyecto

| Carpeta                | Descripción                                                                 |
| ---------------------- | --------------------------------------------------------------------------- |
| `1_clases`             | Conceptos básicos de clases en Python.                                       |
| `2_relaciones`         | Ejemplos de relaciones entre clases: asociación, agregación, composición.    |
| `3_solid`              | Implementaciones de los principios SOLID: responsabilidad única, abierto/cerrado, etc. |

## 📂 Contenido

### 🔹 1. Clases
- **main.py**: Implementación de una clase principal.
- **persona.py**: Ejemplo de una clase `Persona` con atributos y métodos básicos.

### 🔹 2. Relaciones entre clases
- **a_asociacion**: Implementación de la relación de asociación entre clases.
- **b_agregacion**: Ejemplo de la relación de agregación, donde una clase incluye instancias de otra.
- **c_composicion**: Relación de composición donde una clase controla completamente el ciclo de vida de otra.
- **d_generalizacion**: Ejemplo de herencia y polimorfismo.

### 🔹 3. Principios SOLID
- **a_responsabilidad_unica**: Aplicación del principio de responsabilidad única.
- **b_abierto_cerrado**: Ejemplo del principio abierto/cerrado.
- **c_sustitucion_de_liskov**: Implementación del principio de sustitución de Liskov.
- **d_inversion_de_dependencia**: Ejemplo de inversión de dependencias.
- **e_segregacion_de_interfaces**: Segregación de interfaces aplicada en Python.

## 📖 Descripción Detallada de Conceptos

| Principio | Descripción |
| --------- | ----------- |
| **Responsabilidad Única** | Cada clase debe tener una única responsabilidad. |
| **Abierto/Cerrado** | Las entidades de software deben ser abiertas para extensión, pero cerradas para modificación. |
| **Sustitución de Liskov** | Los objetos de una clase derivada deben poder sustituir a los de una clase base. |
| **Inversión de Dependencias** | Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones. |
| **Segregación de Interfaces** | Los clientes no deberían verse forzados a depender de interfaces que no usan. |

## 🔔 Avisos Importantes

> ⚠️ **Nota:** Todos los ejemplos en este repositorio están implementados en **Python 3.x**. Es recomendable tener un conocimiento previo básico de Python y POO para aprovechar al máximo estos ejemplos.

> 📢 **Contribuciones:** Las contribuciones son bienvenidas. Si deseas agregar ejemplos, corregir errores o mejorar la documentación, siéntete libre de abrir un *Pull Request*.

## 🛠️ Requisitos

- Python 3.x
- Entorno de desarrollo (recomendado: VSCode)
- Git

## 📦 Extensiones Recomendadas para VSCode

Aquí te presentamos una lista de las extensiones recomendadas que optimizarán tu flujo de trabajo en Visual Studio Code:

| Extensión                | Descripción                                                                 |
| ------------------------ | --------------------------------------------------------------------------- |
| **Python**               | Proporciona soporte completo para desarrollo en Python, incluyendo linting, autocompletado, y depuración. |
| **isort**                | Organiza automáticamente las importaciones de Python, asegurando que estén ordenadas y sin duplicados. |
| **Jupyter**              | Añade soporte completo para la ejecución de notebooks Jupyter directamente desde VSCode. |
| **GitLens**              | Mejora las funcionalidades de Git dentro de VSCode, permitiendo revisar historiales de cambios, comparaciones y colaboración en equipo. |
| **Pylance**              | Extensión de lenguaje para Python, mejora la autocompletación, análisis estático y validación de tipos. |
| **Python Debugger**      | Proporciona herramientas avanzadas para la depuración de código Python, permitiendo puntos de interrupción, inspección de variables y más. |
| **Error Lens**           | Resalta los errores y advertencias directamente en el editor, proporcionando un feedback inmediato mientras escribes código. |
| **Path Intellisense**    | Proporciona autocompletado inteligente para rutas de archivos y carpetas dentro de tu proyecto. |

### Instalación

```bash
# Clona este repositorio
git clone https://github.com/Miguel-Luis/principios_solid.git

# Navega a la carpeta del proyecto
cd ../principios_solid

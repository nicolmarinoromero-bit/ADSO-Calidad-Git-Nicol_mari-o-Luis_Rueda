# Taller: Aseguramiento de calidad con Git y GitHub

## Integrantes

- **Nicol Mariño** — Desarrollador
- **Luis Rueda** — Desarrollador y revisor SQA

## Objetivo

Aplicar prácticas de aseguramiento de calidad mediante el uso colaborativo de Git y GitHub. El equipo organizará los cambios con ramas, registrará el trabajo en commits atómicos y revisará las contribuciones mediante Pull Requests antes de integrarlas a `main`.

## Repositorio

La guía propone el formato `ADSO-Calidad-Git-[Pareja]` para el nombre del repositorio. Este equipo usa **ADSO-Calidad-Git-Nicol_mari-o-Luis_Rueda**.

## Módulo de reportes

El archivo `reportes.py` genera reportes de los usuarios registrados. Lista los usuarios ordenados por nombre, cuenta cuántos pertenecen a cada dominio de correo y produce un resumen con el total.

```python
from registro import registrar_usuario
from reportes import generar_resumen

usuarios = {}
registrar_usuario(usuarios, "123456", "Ana Pérez", "ana@example.com")
print(generar_resumen(usuarios))
```

## Actividades requeridas

1. Configurar un `.gitignore` que excluya registros, binarios, archivos temporales, entornos virtuales y archivos sensibles como `.env`.
2. Invitar al compañero como colaborador del repositorio de GitHub.
3. Crear las ramas de trabajo indicadas en la guía:
   - `feature/modulo-registro`
   - `feature/modulo-reportes`
4. Realizar al menos tres commits atómicos en cada rama. Usar mensajes claros con convenciones como `feat:`, `fix:` y `docs:`.
5. Abrir un Pull Request de cada rama hacia `main`, describiendo el aporte.
6. Revisar los cambios del compañero, dejar comentarios de mejora cuando corresponda y aprobar los PR antes de fusionarlos.
7. Provocar y resolver un conflicto en un archivo compartido, por ejemplo `README.md`, y conservar el commit que registra la resolución.

## Diagrama del flujo de ramas

El siguiente diagrama ilustra el flujo esperado. Para completar la actividad, las dos ramas deben crearse y fusionarse realmente en GitHub mediante Pull Requests aprobados.

```mermaid
gitGraph
   commit id: "main"
   branch feature/modulo-registro
   commit id: "feat: agregar módulo"
   commit id: "fix: corregir validación"
   commit id: "docs: documentar módulo"
   checkout main
   merge feature/modulo-registro id: "PR revisado"
   branch feature/modulo-reportes
   commit id: "feat: agregar módulo"
   commit id: "fix: corregir salida"
   commit id: "docs: documentar módulo"
   checkout main
   merge feature/modulo-reportes id: "PR revisado"
```

## Entregable

Entregar el enlace al repositorio público de GitHub con el diagrama de red visible, al menos dos ramas fusionadas en `main` y el registro de Pull Requests aprobados.

Repositorio: [ADSO-Calidad-Git-Nicol_mari-o-Luis_Rueda](https://github.com/nicolmarinoromero-bit/ADSO-Calidad-Git-Nicol_mari-o-Luis_Rueda)

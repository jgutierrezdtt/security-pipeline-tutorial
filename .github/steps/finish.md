## ¡Tutorial completado! 🎉

¡Enhorabuena! Has completado los tres pasos del tutorial de seguridad en pipelines de GitHub Actions.

### Lo que has aprendido

| ✅ | Habilidad adquirida |
|---|---|
| ✅ | Configurar un workflow de **SAST con Semgrep** en GitHub Actions |
| ✅ | Identificar y corregir **SQL Injection** en código Python |
| ✅ | Identificar y corregir **Command Injection** con `os.system` |
| ✅ | Eliminar **credenciales hardcodeadas** del código fuente |
| ✅ | Activar **Dependabot** para monitorizar dependencias vulnerables |

### Conceptos clave

- **SAST** — Static Application Security Testing: análisis del código fuente sin ejecutarlo
- **SCA** — Software Composition Analysis: análisis de dependencias de terceros
- **SQL Injection** — el input del usuario se inyecta directamente en una consulta SQL; se evita con parámetros `?`
- **Command Injection** — el input llega a `os.system()` permitiendo ejecutar comandos arbitrarios; se evita con `subprocess.run(list)`
- **Hardcoded secrets** — credenciales en el código que pueden filtrarse en el historial de git; se usan variables de entorno en su lugar

### Próximos pasos recomendados

1. **Activa Dependabot en tus repos reales** — revisa Security → Dependabot alerts
2. **Explora más reglas de Semgrep** — prueba `p/owasp-top-ten` o `p/django` según tu stack
3. **Conoce el OWASP Top 10** — las 10 vulnerabilidades más críticas en aplicaciones web
4. **Prueba CodeQL** — análisis semántico más profundo disponible con GitHub Advanced Security
5. **Consulta el repo de pipelines** — workflows reutilizables de seguridad para toda la organización

---
*Tutorial completado · Seguridad en Pipelines de GitHub Actions*

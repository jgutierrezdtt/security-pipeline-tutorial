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

### Añade tu badge al perfil de GitHub

Copia este badge y pégalo en el `README.md` de tu repositorio de perfil (`tu-usuario/tu-usuario`):

```markdown
![Security Pipeline Tutorial](https://img.shields.io/badge/Security_Pipeline_Tutorial-Completado_%E2%9C%85-4caf50?style=flat-square&logo=githubactions&logoColor=white)
```

Resultado: ![Security Pipeline Tutorial](https://img.shields.io/badge/Security_Pipeline_Tutorial-Completado_%E2%9C%85-4caf50?style=flat-square&logo=githubactions&logoColor=white)

> Ve a `github.com/tu-usuario/tu-usuario` (o créalo si no existe) y edita el `README.md` para añadirlo.

### Próximos pasos recomendados

1. **Activa Dependabot en tus repos reales** — revisa Security → Dependabot alerts
2. **Explora más reglas de Semgrep** — prueba `p/owasp-top-ten` o `p/django` según tu stack
3. **Prueba CodeQL** — análisis semántico más profundo disponible con GitHub Advanced Security
4. **Consulta el repo de pipelines** — workflows reutilizables de seguridad para toda la organización

---
*Tutorial completado · Seguridad en Pipelines de GitHub Actions*

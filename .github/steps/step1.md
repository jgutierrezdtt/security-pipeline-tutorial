## Paso 1 de 3 — Añadir análisis SAST con Semgrep

¡El tutorial ha comenzado! 🎉

### Contexto

Este repositorio incluye el archivo `src/app.py` con varias vulnerabilidades de seguridad.  
En este paso añadirás un **workflow de análisis estático (SAST)** con Semgrep para detectarlas automáticamente en cada push.

### Tu tarea

Crea el archivo `.github/workflows/sast.yml` con el siguiente contenido:

```yaml
name: SAST con Semgrep
on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

jobs:
  semgrep:
    name: Análisis estático
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: semgrep/semgrep-action@v1
        with:
          config: >-
            p/python
            p/secrets
```

### Cómo hacerlo

**Opción A — Desde la interfaz web de GitHub:**
1. Ve a tu repositorio → **Add file** → **Create new file**
2. En el nombre del archivo escribe exactamente: `.github/workflows/sast.yml`
3. Pega el contenido de arriba
4. Haz click en **Commit changes** → **Commit directly to the `main` branch**

**Opción B — Desde la terminal:**
```bash
mkdir -p .github/workflows
# crea .github/workflows/sast.yml con el contenido de arriba
git add .github/workflows/sast.yml
git commit -m "ci: add Semgrep SAST workflow"
git push
```

### ¿Qué pasará?

Cuando hagas push de `sast.yml`:
- Semgrep analizará `src/app.py` automáticamente
- Encontrará las vulnerabilidades presentes en el código
- Verás los resultados en la pestaña **Actions** de tu repositorio
- Este README se actualizará al **Paso 2** ✅

---
*Paso 1 de 3 · Tutorial de Seguridad en Pipelines*

"""Tutorial de Seguridad en Pipelines — Aplicación de ejemplo

ADVERTENCIA: Este archivo contiene vulnerabilidades INTENCIONALES para el tutorial.
NO uses este código en producción.
"""

import os
import sqlite3

# Vulnerabilidad 1: credenciales hardcodeadas (Semgrep: p/secrets)
DB_PASSWORD = "admin123"
API_KEY = "sk-prod-abc123xyz789"


def search_user(username):
    """Busca un usuario por nombre."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerabilidad 2: SQL Injection — concatenación de strings sin sanitizar
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)

    return cursor.fetchall()


def ping_host(host):
    """Comprueba si un host es accesible."""
    # Vulnerabilidad 3: Command Injection — os.system con input del usuario
    os.system("ping -c 1 " + host)


def main():
    print("App started")
    result = search_user("admin")
    print(f"Found: {result}")
    ping_host("localhost")


if __name__ == "__main__":
    main()

import subprocess
import re
import sys
import typer
import questionary
from rich import print

app = typer.Typer(help="CLI para generar commits inteligentes y rápidos.")

def get_git_branch() -> str:
    """Obtiene el nombre de la rama Git actual."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""

def get_staged_files() -> list[str]:
    """Obtiene la lista de archivos actualmente en staging."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True, text=True, check=True
        )
        files = [f for f in result.stdout.strip().split("\n") if f]
        return files
    except subprocess.CalledProcessError:
        return []

def extract_ticket_from_branch(branch_name: str) -> str:
    """Extrae un ID de ticket (ej. ABC-123 o MELI-88) del nombre de la rama."""
    match = re.search(r"([A-Za-z]+-\d+)", branch_name)
    return match.group(1).upper() if match else ""

def generate_suggestions(files: list[str], ticket: str) -> list[str]:
    """Genera opciones de mensajes basados en los archivos en staging."""
    ticket_prefix = f"[{ticket}] " if ticket else ""
    
    # Analizamos extensiones de archivos para inferir el 'scope'
    has_docs = any(f.endswith(".md") or "docs/" in f for f in files)
    has_tests = any("test" in f or "spec" in f for f in files)
    has_config = any(f in ["package.json", "requirements.txt", "Dockerfile", "pyproject.toml"] for f in files)

    suggestions = []

    if has_docs and len(files) == 1:
        suggestions.append(f"docs: {ticket_prefix}actualizar documentación ({files[0]})")
    
    if has_tests:
        suggestions.append(f"test: {ticket_prefix}agregar o actualizar pruebas unitarias")
        
    if has_config:
        suggestions.append(f"chore: {ticket_prefix}actualizar dependencias y configuración del proyecto")

    # Opción genérica basada en la cantidad de archivos
    file_summary = ", ".join([f.split("/")[-1] for f in files[:2]])
    if len(files) > 2:
        file_summary += f" y {len(files) - 2} más"

    suggestions.append(f"feat: {ticket_prefix}actualizar {file_summary}")
    suggestions.append(f"fix: {ticket_prefix}resolver problema en {file_summary}")

    return suggestions

@app.command()
def commit():
    """Analiza staging y abre el menú para hacer commit."""
    staged_files = get_staged_files()

    if not staged_files:
        print("[bold yellow]⚠️  No hay archivos en staging.[/bold yellow] Usa [bold cyan]git add[/bold cyan] primero.")
        raise typer.Exit()

    branch = get_git_branch()
    ticket = extract_ticket_from_branch(branch)
    suggestions = generate_suggestions(staged_files, ticket)
    
    # Opción para escribir algo personalizado
    CUSTOM_OPTION = "✏️  Escribir un mensaje personalizado..."
    choices = suggestions + [CUSTOM_OPTION]

    print(f"[bold green]✓[/bold green] {len(staged_files)} archivo(s) detectado(s) en staging.")
    if ticket:
        print(f"[bold blue]ℹ[/bold blue] Ticket detectado en la rama: [bold]{ticket}[/bold]\n")

    # Interfaz interactiva en la terminal
    selected_message = questionary.select(
        "Selecciona el mensaje para tu commit:",
        choices=choices
    ).ask()

    if not selected_message:
        print("[yellow]Operación cancelada.[/yellow]")
        raise typer.Exit()

    if selected_message == CUSTOM_OPTION:
        selected_message = questionary.text("Escribe tu mensaje de commit:").ask()
        if not selected_message:
            print("[red]El mensaje no puede estar vacío.[/red]")
            raise typer.Exit()

    # Ejecutar el commit
    try:
        subprocess.run(["git", "commit", "-m", selected_message], check=True)
        print(f"\n[bold green]🚀 Commit realizado con éxito:[/bold green] \"{selected_message}\"")
    except subprocess.CalledProcessError:
        print("\n[bold red]❌ Error al ejecutar git commit.[/bold red]")

if __name__ == "__main__":
    app()
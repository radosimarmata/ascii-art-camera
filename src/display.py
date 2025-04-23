from rich.console import Console
from rich.panel import Panel

console = Console()

def show_ascii(ascii_art: str):
  console.print(Panel(ascii_art, title="🎞️ ASCII Art Output", subtitle="Tekan Ctrl+C untuk keluar", expand=False))

from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, TaskProgressColumn
from time import sleep
from datetime import datetime

console = Console()
duration = 0.1
task_message = "[green]estamos focados 🚀"
start_time = datetime.now().strftime("%I:%M%p")

progress = Progress(
    TextColumn("[bold cyan]~ > work"),
    TextColumn(task_message),
    TextColumn(f"[white]{start_time} - "),
    TimeElapsedColumn(),
    BarColumn(bar_width=None, complete_style="bold magenta"),
    TaskProgressColumn(show_speed=False),
    console=console,
)

with progress:
    task = progress.add_task("", total=duration * 60)
    while not progress.finished:
        progress.update(task, advance=1)
        sleep(1)
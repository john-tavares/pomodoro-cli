from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, TaskProgressColumn
from time import sleep
from datetime import datetime

console = Console()
duration = 25
task_message = "[green]~ > focus 🚀"
start_time = datetime.now().strftime("%I:%M%p")

progress = Progress(
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
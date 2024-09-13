from rich.progress import progress
import time

with progress() as progress:
    task = progress.add_task("[cyan]Downloading ", total=100)
    while not progress.finished:
        progress.update(task, advance=1)
        time.sleep(0.2)
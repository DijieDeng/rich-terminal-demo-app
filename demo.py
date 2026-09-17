from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

# Styled table
table = Table(title="Project Dashboard", show_header=True, header_style="bold magenta", box=box.ROUNDED)
table.add_column("Task", style="cyan", no_wrap=True)
table.add_column("Owner", style="green")
table.add_column("Status", justify="center")
table.add_column("Progress", justify="right", style="bold yellow")

table.add_row("Docs review", "Alice", "[green]Done[/green]", "100%")
table.add_row("Sandbox demo", "Bob", "[yellow]In progress[/yellow]", "60%")
table.add_row("Git push", "Carol", "[red]Pending[/red]", "0%")

# Panel
panel = Panel.fit(
    "[bold]Rich[/bold] makes terminal output beautiful :sparkles:\n"
    "Tables, panels, markdown, code, tracebacks — out of the box.",
    title="About",
    border_style="blue",
    padding=(1, 2),
)

console.print(panel)
console.print(table)
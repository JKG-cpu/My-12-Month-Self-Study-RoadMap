from rich.console import Console
from datetime import date
from os import system, name

# This just clears the terminal
def cc():
    system("cls" if name == "nt" else "clear")

# This will be used to display anything (pages, notes, etc)
class UI:
    def __init__(self):
        self.console = Console()
        self.console.style = "bold white"

    def display_page(self, page: str, title: str | None = None) -> None:
        cc()
        lines = page.replace("<br>", "").split("\n")

        if title:
            line_length = "┼──" + "─" * len(f"Viewing: {title}") + "──┼"
            
            self.console.print(line_length)
            self.console.print(f"Viewing: {title}".center(len(line_length)))
            self.console.print(line_length)
        
        print()
        for i, line in enumerate(lines, 1):
            self.console.print(f"{i} │ {line}")
        print()

# This will handle all the logs
class LogManager:
    def __init__(self) -> None:
        self.log_format = "DATE\n\nTOPIC\n\n### Information\nTime Spent: TIME-SPENT<br>\nSources: SOURCES<br>\nREFLECTION"

    # Get Information
    def get_date(self):
        """Returns x/y/z"""
        fixed_date = date.today().strftime("## %m/%d/%Y")
        return fixed_date
    
    # Helpers
    def _format_log(self, log: str, fixed_date: str, topic: str, time_spent: str, reflection: str, sources: list[str] | None) -> str:
        log = log.replace("DATE", fixed_date)
        log = log.replace("TOPIC", topic)
        log = log.replace("TIME-SPENT", time_spent)

        if sources is None:
            log = log.replace("Sources: SOURCES<br>\n", "")

        else:
            # Going to need to format sources to be either str or [str](link)
            log = log.replace("SOURCES", sources)

        log = log.replace("REFLECTION", reflection)
    
        return log

    # Creating a new log
    def new_log(self, topic: str, time_spent: str, reflection: str, sources: list[str] | None = None) -> str:
        # Create Basic Log
        log = self.log_format

        # Gather Information
        fdate = self.get_date()
        sources = sources

        # Change log
        log = self._format_log(
            log = log,
            fixed_date = fdate,
            topic = topic,
            time_spent = time_spent,
            reflection = reflection,
            sources = sources
        )

        # return log
        return log

# This will handle user input and routing it to use other classes / modules
class PDU:
    def __init__(self) -> None:
        # Base Variables
        self.running = True

        self.console = Console()
        self.console.style = "bold white"

        # Modules
        self.ui = UI()
        self.logManager = LogManager()

    def run(self) -> None:
        while self.running:
            cc()

            user_input = input(" > ").title().strip()

            match user_input:
                case "E":
                    self.running = False
                    cc()
                    continue
            
                case "L":
                    topic = input("Topic > ")
                    time_spent = input("Time spent > ")
                    reflection = input("Reflection > ")
                    sources = input("Sources > ")
                    
                    new_log = self.logManager.new_log(
                        topic = topic,
                        time_spent = time_spent,
                        reflection = reflection,
                        sources = sources if sources != "" else None
                    )

                    self.ui.display_page(new_log, "new_log.md")
                    input()

if __name__ == "__main__":
    pdu = PDU()
    pdu.run()
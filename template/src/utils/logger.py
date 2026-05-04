import sys


class Logger:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    BLUE   = "\033[34m"
    GREEN  = "\033[32m"
    YELLOW = "\033[33m"
    RED    = "\033[31m"
    CYAN   = "\033[36m"

    def step(self, msg: str)    -> None: print(f"{self.CYAN}{self.BOLD}→ {msg}{self.RESET}")
    def info(self, msg: str)    -> None: print(f"  {msg}")
    def success(self, msg: str) -> None: print(f"{self.GREEN}✓ {msg}{self.RESET}")
    def warn(self, msg: str)    -> None: print(f"{self.YELLOW}⚠ {msg}{self.RESET}", file=sys.stderr)
    def error(self, msg: str)   -> None: print(f"{self.RED}✗ {msg}{self.RESET}", file=sys.stderr)


logger = Logger()

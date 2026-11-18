from pathlib import Path
import csv


def load_faq(path: str | Path) -> list[dict[str, str]]:
    """Charge une FAQ CSV. Les réponses doivent être validées par la NARSA."""
    path = Path(path)
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))

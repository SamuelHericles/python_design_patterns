from handler import SupportHandler


class Level1Support(SupportHandler):
    def handle(self, level: int, issue: str) -> str:
        if level <= 1:
            return f"  [L1] Resolvido: {issue}"
        return self._pass_to_next(level, issue)


class Level2Support(SupportHandler):
    def handle(self, level: int, issue: str) -> str:
        if level <= 2:
            return f"  [L2] Resolvido: {issue}"
        return self._pass_to_next(level, issue)


class Level3Support(SupportHandler):
    def handle(self, level: int, issue: str) -> str:
        return f"  [L3 - Especialista] Resolvido: {issue}"

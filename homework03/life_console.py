import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border("|", "|", "-", "-", "+", "+", "+", "+")

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        screen.clear()
        for y in range(1, self.life.rows + 1):
            for x in range(1, self.life.cols + 1):
                if not self.life.curr_generation[y - 1][x - 1]:
                    screen.addstr(y, x, " ")
                else:
                    screen.addstr(y, x, "*")

    def run(self) -> None:
        screen = curses.initscr()
        curses.resizeterm(self.life.rows + 2, self.life.cols + 2)
        while self.life.is_changing and not self.life.is_max_generations_exceeded:
            self.life.step()
            self.draw_borders(screen)
            self.draw_grid(screen)
            screen.refresh()
            curses.napms(400)
        curses.endwin()

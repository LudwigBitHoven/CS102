import pygame
from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)

        self.cell_size = cell_size

        self.width = self.life.cols * self.cell_size
        self.height = self.life.rows * self.cell_size
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.speed = speed

    def draw_lines(self) -> None:
        # Copy from previous assignment
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, x), (self.height, x))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (y, 0), (y, self.width))

    def draw_grid(self) -> None:
        # Copy from previous assignment
        y = 0
        for row in self.life.curr_generation:
            x = 0
            for cell in row:
                color = pygame.Color("green") if cell else pygame.Color("white")
                pygame.draw.rect(self.screen, color, (y, x, self.cell_size, self.cell_size))
                x += self.cell_size
            y += self.cell_size

    def run(self) -> None:

        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        self.life.create_grid(True)

        running = True
        paused = False
        while running and self.life.is_changing and not self.life.is_max_generations_exceeded:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False

                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        paused = not paused

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = [coord // self.cell_size for coord in event.pos]
                        if self.life.curr_generation[y][x] == 0:
                            self.life.curr_generation[y][x] = 1
                        else:
                            self.life.curr_generation[y][x] = 0
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = [coord // self.cell_size for coord in event.pos]
                    if self.life.curr_generation[y][x] != 0:
                        self.life.curr_generation[y][x] = 0
                    else:
                        self.life.curr_generation[y][x] = 1

            self.draw_lines()
            self.draw_grid()

            if not paused:
                self.life.step()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

import pygame

from position import Position
from direction import Direction
from game_state import GameState

pygame.init()

CUBE_SIZE = 25
CUBE_NUM = 20
WIGHT = CUBE_NUM * CUBE_SIZE
screen = pygame.display.set_mode((WIGHT, WIGHT))

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

state = GameState(snake=None, direction=None, food=None, field_size=CUBE_NUM)
state.set_initial_position()


def draw_snake_part(pos):
	position = (pos.x * CUBE_SIZE, pos.y * CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)
	pygame.draw.rect(screen, GREEN, position)


def draw_food(pos):
	radius = float(CUBE_SIZE) / 2
	position = (pos.x * CUBE_SIZE + radius, pos.y * CUBE_SIZE + radius)
	pygame.draw.circle(screen, BLUE, position, radius)


def draw_snake(snake):
	for part in snake:
		draw_snake_part(part)


def fill_bg():
	screen.fill(WHITE)


def draw(snake, food):
	fill_bg()
	draw_snake(snake)
	draw_food(food)
	pygame.display.update()


draw(
	snake=[Position(1, 1), Position(1, 2), Position(1, 3), Position(2, 3), Position(2, 4), Position(2, 5)],
	food=Position(10, 6),
)

clock = pygame.time.Clock()
while True:
	clock.tick(7)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				state.turn(Direction.LEFT)
			elif event.key == pygame.K_RIGHT:
				state.turn(Direction.RIGHT)
			elif event.key == pygame.K_UP:
				state.turn(Direction.UP)
			elif event.key == pygame.K_DOWN:
				state.turn(Direction.DOWN)

	state.step()
	draw(state.snake, state.food)
	pygame.display.update()

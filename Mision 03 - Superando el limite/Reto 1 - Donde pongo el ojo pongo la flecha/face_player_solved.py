from os.path import dirname, join
from solution import computeOrientation
import pygame  # Module used for game development in python


def rotate(surface_to_rotate, angle_to_rotate, center_x, center_y):
    rotated_surface = pygame.transform.rotozoom(surface_to_rotate, angle_to_rotate, 1)
    rotated_rect = rotated_surface.get_rect(center=(center_x, center_y))
    return rotated_surface, rotated_rect


if __name__ == "__main__":
    pygame.init()  # initializes all pygame modules

    # Set up game window with its background
    background = pygame.image.load(join(dirname(__file__), "Image_files/dungeonBackground.jpg"))
    screen = pygame.display.set_mode((background.get_width(), background.get_height()))
    pygame.display.set_caption('Dark Souls')

    # Set up enemy image
    enemyImage = pygame.image.load(join(dirname(__file__), 'Image_files/enemyArcher.png'))
    enemyImage = pygame.transform.scale(enemyImage, (138, 182))
    enemy_x = background.get_width() / 2
    enemy_y = background.get_height() / 2
    enemyImage_rect = enemyImage.get_rect(center=(enemy_x, enemy_y))

    # Set up player image
    playerImage = pygame.image.load(join(dirname(__file__), 'Image_files/solaire.png'))
    playerImage = pygame.transform.scale(playerImage, (138, 182))
    playerImage_rect = playerImage.get_rect(center=(background.get_width() / 2, background.get_height() / 2))

    angle = 0

    # Infinite execution loop
    while True:
        # Exit game if player press game window X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Get mouse position in game window and use it to set player position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        playerImage_rect = playerImage.get_rect(center=(mouse_x, mouse_y))

        angle = computeOrientation(enemy_x, enemy_y, mouse_x, mouse_y)
        print(angle)

        # Draw background and sprites in their corresponding position, and refresh game window
        screen.blit(background, (0, 0))

        enemyImage_rotated, enemyImage_rect_rotated = rotate(enemyImage, angle, background.get_width() / 2,
                                                            background.get_height() / 2)
        screen.blit(enemyImage_rotated, enemyImage_rect_rotated)

        screen.blit(playerImage, playerImage_rect)

        pygame.display.update()

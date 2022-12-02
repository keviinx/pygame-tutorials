"""
Create-a-Picture
"""

import pygame

pygame.init()

# Color definition
# Use nordic color schemes instead because the original color is too bright
DORAEMON_BLUE = (128, 161, 192)
DORAEMON_WHITE = (229, 234, 240)
DORAEMON_RED = (190, 97, 107)
DORAEMON_YELLOW = (234, 203, 139)
DORAEMON_BLACK = (46, 52, 64)

PI = 3.141592653

# Define the border thickness before the rest are defined
BORDER_THICKNESS = 3

# Screen size
size = (400, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Doraemon")

# Loop until the user click the close button
done = False
clock = pygame.time.Clock()


def draw_background():
    # Fill the whole screen with doraemon colors
    background_colors = [
        DORAEMON_BLUE,
        DORAEMON_WHITE,
        DORAEMON_RED,
        DORAEMON_YELLOW,
        DORAEMON_BLACK,
    ]
    background_top_left_x_coordinate = 0
    background_top_left_y_coordinate = 0
    background_bottom_right_x_coordinate = 80
    background_bottom_right_y_coordinate = 400
    for background_color in background_colors:
        pygame.draw.rect(
            screen,
            background_color,
            [
                background_top_left_x_coordinate,
                background_top_left_y_coordinate,
                background_bottom_right_x_coordinate,
                background_bottom_right_y_coordinate,
            ],
        )
        background_top_left_x_coordinate += 80
        background_bottom_right_x_coordinate += 80


# Main game loop
while not done:

    # To capture the click of close button on window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    draw_background()

    # Draw the doraemon collar, this have to start first so that the rest is drawn on top of this
    collar_x_coordinate = 200
    collar_y_coordinate = 245
    collar_radius = 125
    pygame.draw.circle(
        screen, DORAEMON_RED, [collar_x_coordinate, collar_y_coordinate], collar_radius
    )
    pygame.draw.circle(
        screen,
        DORAEMON_BLACK,
        [collar_x_coordinate, collar_y_coordinate],
        collar_radius,
        BORDER_THICKNESS,
    )

    # The main circle head of doraemon
    head_x_coordinate = 200
    head_y_coordinate = 200
    head_radius = 150
    pygame.draw.circle(
        screen, DORAEMON_BLUE, [head_x_coordinate, head_y_coordinate], head_radius
    )
    pygame.draw.circle(
        screen,
        DORAEMON_BLACK,
        [head_x_coordinate, head_y_coordinate],
        head_radius,
        BORDER_THICKNESS,
    )

    # the white part of doraemon's face
    mouth_x_coordinate = 200
    mouth_y_coordinate = 235
    mouth_radius = 115
    pygame.draw.circle(
        screen, DORAEMON_WHITE, [mouth_x_coordinate, mouth_y_coordinate], mouth_radius
    )
    pygame.draw.circle(
        screen,
        DORAEMON_BLACK,
        [mouth_x_coordinate, mouth_y_coordinate],
        mouth_radius,
        BORDER_THICKNESS,
    )

    # the red nose
    nose_x_coordinate = 200
    nose_y_coordinate = 185
    pygame.draw.circle(screen, DORAEMON_RED, [nose_x_coordinate, nose_y_coordinate], 25)
    pygame.draw.circle(
        screen,
        DORAEMON_BLACK,
        [nose_x_coordinate, nose_y_coordinate],
        25,
        BORDER_THICKNESS,
    )
    pygame.draw.circle(
        screen,
        DORAEMON_WHITE,
        [nose_x_coordinate - 10, nose_y_coordinate - 10],
        7,
    )

    # the yellow bell
    bell_x_coordinate = 200
    bell_y_coordinate = 375
    pygame.draw.circle(
        screen, DORAEMON_YELLOW, [bell_x_coordinate, bell_y_coordinate], 25
    )
    pygame.draw.circle(
        screen,
        DORAEMON_BLACK,
        [bell_x_coordinate, bell_y_coordinate],
        25,
        BORDER_THICKNESS,
    )
    pygame.draw.circle(
        screen, DORAEMON_BLACK, [bell_x_coordinate, bell_y_coordinate], 7
    )
    pygame.draw.line(screen, DORAEMON_BLACK, [200, 380], [200, 397], BORDER_THICKNESS)
    pygame.draw.circle(
        screen,
        DORAEMON_WHITE,
        [bell_x_coordinate - 10, bell_y_coordinate - 10],
        7,
    )

    # draw the eyes
    eye_offsets = [0, 75]
    for eye_offset in eye_offsets:
        pygame.draw.ellipse(screen, DORAEMON_WHITE, [125 + eye_offset, 80, 75, 100])
        pygame.draw.ellipse(
            screen, DORAEMON_BLACK, [125 + eye_offset, 80, 75, 100], BORDER_THICKNESS
        )

    # draw the pupil
    pupil_x_coordinate = 165
    pupil_black_y_coordinate = 130
    pupil_white_y_coordinate = 125
    pupil_black_radius = 15
    pupil_white_radius = 7
    pupil_offsets = [0, 75]
    for pupil_offset in pupil_offsets:
        pygame.draw.circle(
            screen,
            DORAEMON_BLACK,
            [pupil_x_coordinate + pupil_offset, pupil_black_y_coordinate],
            pupil_black_radius,
        )
        pygame.draw.circle(
            screen,
            DORAEMON_WHITE,
            [pupil_x_coordinate + pupil_offset, pupil_white_y_coordinate],
            pupil_white_radius,
        )

    # Draw the mouth
    mouth_start_angle = PI + (0.1 * PI)
    mouth_stop_angle = 2 * PI - (0.1 * PI)
    pygame.draw.line(screen, DORAEMON_BLACK, [200, 210], [200, 298], BORDER_THICKNESS)
    pygame.draw.arc(
        screen,
        DORAEMON_BLACK,
        [125, 150, 150, 150],
        mouth_start_angle,
        mouth_stop_angle,
        BORDER_THICKNESS,
    )

    # Draw whiskers
    pygame.draw.line(screen, DORAEMON_BLACK, [150, 200], [120, 180], BORDER_THICKNESS)
    pygame.draw.line(screen, DORAEMON_BLACK, [150, 210], [120, 210], BORDER_THICKNESS)
    pygame.draw.line(screen, DORAEMON_BLACK, [150, 220], [120, 240], BORDER_THICKNESS)
    pygame.draw.line(screen, DORAEMON_BLACK, [250, 200], [280, 180], BORDER_THICKNESS)
    pygame.draw.line(screen, DORAEMON_BLACK, [250, 210], [280, 210], BORDER_THICKNESS)
    pygame.draw.line(screen, DORAEMON_BLACK, [250, 220], [280, 240], BORDER_THICKNESS)

    # To render on screen, must be the end after all the draw commands.
    pygame.display.flip()

    # Set FPS
    clock.tick(60)

pygame.quit()

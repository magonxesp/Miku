from pygame.time import get_ticks
import pygame.image
import os
import pygame


class ImageSpriteAnimation:

    def __init__(self):
        self.index = 0
        self.images = {
            'right': [],
            'left': []
        }
        self.speed = 1
        self.direction = 'right'
        self.loop_effect = False
        self._is_last_frame = False

    def get_images_list(self, path):
        directory_abs_path = os.path.join(os.path.dirname(__file__), path)
        files = os.listdir(directory_abs_path)
        images = []

        for file in files:
            file_abs_path = os.path.join(directory_abs_path, file)

            if os.path.isdir(file_abs_path) is False:
                try:
                    images.append(pygame.image.load(file_abs_path))
                except pygame.error as e:
                    print("Error: {} => {}".format(e, file_abs_path))

        return images

    def set_direction(self, direction):
        self.direction = direction

    def _update_index(self):
        images_len = len(self.images)

        if self.loop_effect:
            if self._is_last_frame:
                self.index -= (0.1 * self.speed)
            else:
                self.index += (0.1 * self.speed)

            if self.index <= 0:
                self._is_last_frame = False

            if self.index >= images_len:
                self._is_last_frame = True
                self.index = images_len - 1
        else:
            if self.index < images_len:
                self.index += (0.1 * self.speed)

            if self.index >= images_len:
                self.index = 0

    def play(self, *args, **kwargs):
        current_image = int(self.index)
        self._update_index()
        return self.images[self.direction][current_image]

    def stop(self):
        self.index = 0
        return self.images[self.direction][0]


class MikuIdleAnimation(ImageSpriteAnimation):

    def __init__(self):
        super().__init__()
        self.images['right'] = self.get_images_list('assets/miku/idle_right')
        self.images['left'] = self.get_images_list('assets/miku/idle_left')


class MikuRunAnimation(ImageSpriteAnimation):

    def __init__(self):
        super().__init__()
        self.images['right'] = self.get_images_list('assets/miku/run_right')
        self.images['left'] = self.get_images_list('assets/miku/run_left')
        self.stop_image = {
            'right': self.images['right'].pop(),
            'left': self.images['left'].pop()
        }

use sdl2::pixels::PixelFormatEnum;
use sdl2::surface::Surface;

use crate::Moves;

pub struct Level {
    complete: bool,
    move_stack: Vec<Moves>,
}

impl Level {
    pub fn new() -> Self {
        Level {
            complete: false,
            move_stack: Vec::new(),
        }
    }

    pub fn render(&self) -> (Surface, Surface) {
        let left_surface = Surface::new(512, 512, PixelFormatEnum::RGB24).unwrap();
        let right_surface = Surface::new(512, 512, PixelFormatEnum::RGB24).unwrap();
        (left_surface, right_surface)
    }
}

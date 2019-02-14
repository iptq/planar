use sdl2::pixels::PixelFormatEnum;
use sdl2::surface::Surface;

use crate::Moves;

#[derive(Debug, Serialize, Deserialize)]
pub struct Level {
    complete: bool,
    dimensions: (u8, u8),
    move_stack: Vec<Moves>,
}

impl Level {
    pub fn new(dimensions: (u8, u8)) -> Self {
        Level {
            complete: false,
            move_stack: Vec::new(),
            dimensions,
        }
    }

    pub fn render(&self, cell_size: f64) -> (Surface, Surface) {
        let left_surface = Surface::new(512, 512, PixelFormatEnum::RGB24).unwrap();
        let right_surface = Surface::new(512, 512, PixelFormatEnum::RGB24).unwrap();
        (left_surface, right_surface)
    }
}

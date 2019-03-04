use sdl2::pixels::{Color, PixelFormatEnum};
use sdl2::rect::Rect;
use sdl2::surface::Surface;

use crate::renderer::Drawable;
use crate::Point;

pub struct Button {
    x: i32,
    y: i32,
    width: u32,
    height: u32,
    color: Color,
    label: String,
}

impl Button {
    pub fn new(x: i32, y: i32, width: u32, height: u32, color: Color, label: String) -> Button {
        Button {
            x,
            y,
            width,
            height,
            color,
            label,
        }
    }
}

impl Drawable for Button {
    fn get_position(&self) -> Point<i32> {
        Point(self.x, self.y)
    }

    fn get_size(&self) -> Point<u32> {
        Point(self.width, self.height)
    }

    fn draw<'a>(&mut self) -> Surface<'a> {
        let mut surface = Surface::new(self.width, self.height, PixelFormatEnum::RGBA8888).unwrap();
        surface.fill_rect(Rect::new(0, 0, self.width, self.height), self.color);
        surface
    }
}

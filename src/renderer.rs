use sdl2::pixels::{Color, PixelFormatEnum};
use sdl2::rect::Rect;
use sdl2::surface::Surface;

use crate::Point;

pub trait Drawable {
    fn get_position(&self) -> Point<i32>;
    fn get_size(&self) -> Point<u32>;

    fn draw<'a>(&mut self) -> Surface<'a>;
}

pub struct Renderer {
    items: Vec<Box<dyn Drawable>>,
}

impl Renderer {
    pub fn new() -> Renderer {
        Renderer { items: Vec::new() }
    }

    pub fn push(&mut self, item: impl Drawable + 'static) {
        self.items.push(Box::new(item));
    }

    pub fn render<'a>(&mut self) -> (Point<i32>, Surface<'a>) {
        let (min, max) = self.items.iter().fold((None, None), |(min, max), item| {
            let top_left = item.get_position();
            let bottom_right = top_left.clone() + item.get_size().into_signed();
            let min = Some(match min {
                Some(Point(mut x, mut y)) => {
                    if x < top_left.0 {
                        x = top_left.0
                    }
                    if y < top_left.1 {
                        y = top_left.1
                    }
                    Point(x, y)
                }
                None => Point(top_left.0, top_left.1),
            });
            let max = Some(match max {
                Some(Point(mut x, mut y)) => {
                    if x > bottom_right.0 {
                        x = bottom_right.0
                    }
                    if y > bottom_right.1 {
                        y = bottom_right.1
                    }
                    Point(x, y)
                }
                None => Point(bottom_right.0, bottom_right.1),
            });
            (min, max)
        });

        match (min, max) {
            (Some(Point(minx, miny)), Some(Point(maxx, maxy))) => {
                let base = Point(minx, miny);
                let width = maxx - minx;
                let height = maxy - miny;
                let surface =
                    Surface::new(width as u32, height as u32, PixelFormatEnum::RGB24).unwrap();
                let mut canvas = surface.into_canvas().unwrap();

                let texture_creator = canvas.texture_creator();
                for mut item in self.items.iter_mut() {
                    let inner = item.draw();
                    let inner = texture_creator.create_texture_from_surface(inner).unwrap();
                    let dimensions = item.get_size();
                    let position = item.get_position() - base.clone();
                    canvas.copy(
                        &inner,
                        None,
                        Some(Rect::new(
                            position.0,
                            position.1,
                            dimensions.0,
                            dimensions.1,
                        )),
                    );
                }

                (base, canvas.into_surface())
            }
            _ => (
                Point(0, 0),
                Surface::new(1, 1, PixelFormatEnum::RGB24).unwrap(),
            ), // empty
        }
    }
}

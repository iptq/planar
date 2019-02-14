use sdl2::rect::Rect;
use sdl2::render::WindowCanvas;

use super::State;
use crate::Level;

#[derive(Debug)]
pub struct GameState<'a> {
    level: Level<'a>,
}

impl<'a> State for GameState<'a> {
    fn is_transparent(&self) -> bool {
        false
    }

    fn render(&self, canvas: &mut WindowCanvas) {
        let (rows, columns) = self.level.dimensions();
        let (screen_width, screen_height) = canvas.output_size().unwrap();
        // println!("{:?}", (screen_width, screen_height));

        // determine cell size
        let level_ratio = (2.0 * columns as f64 + 6.0) / (rows as f64 + 4.0);
        let screen_ratio = screen_width as f64 / screen_height as f64;
        let (scale, (xoff, yoff)) = if level_ratio > screen_ratio {
            let scale = screen_width / (2 * columns + 6);
            (scale, (0, (screen_height - (rows + 4) * scale) / 2))
        } else {
            let scale = screen_height / (rows + 4);
            (scale, ((screen_width - (2 * columns + 6) * scale) / 2, 0))
        };

        let texture_creator = canvas.texture_creator();
        let (left, right) = self.level.render(scale);
        let (left, right) = (
            texture_creator.create_texture_from_surface(left).unwrap(),
            texture_creator.create_texture_from_surface(right).unwrap(),
        );

        canvas
            .copy(
                &left,
                None,
                Some(Rect::new(
                    (xoff + 2 * scale) as i32,
                    (yoff + 2 * scale) as i32,
                    columns * scale,
                    rows * scale,
                )),
            )
            .unwrap();
        canvas
            .copy(
                &right,
                None,
                Some(Rect::new(
                    (xoff + (4 + columns) * scale) as i32,
                    (yoff + 2 * scale) as i32,
                    columns * scale,
                    rows * scale,
                )),
            )
            .unwrap();
    }
}

impl<'a> GameState<'a> {
    pub fn new(level: Level<'a>) -> Self {
        GameState { level }
    }
}

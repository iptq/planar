use std::time::Duration;

use sdl2::rect::Rect;
use sdl2::render::WindowCanvas;

use super::State;
use crate::{Event, Level, Point};

#[derive(Debug)]
pub struct GameState<'a> {
    level: Level<'a>,
}

impl<'a> State for GameState<'a> {
    fn update(&mut self, _: Duration, events: Vec<Event>) {
        println!("events: {:?}", events);
    }

    fn render(&mut self, canvas: &mut WindowCanvas) {
        let Point(rows, columns) = self.level.dimensions();
        let (screen_width, screen_height) = canvas.output_size().unwrap();

        // determine cell size
        let level_ratio = (2 * columns + 6) as f64 / (rows + 2) as f64;
        let screen_ratio = screen_width as f64 / screen_height as f64;
        let (scale, (xoff, yoff)) = if level_ratio > screen_ratio {
            let scale = screen_width / (2 * columns + 6);
            (scale, (0, (screen_height - (rows + 2) * scale) / 2))
        } else {
            let scale = screen_height / (rows + 2);
            (scale, ((screen_width - (2 * columns + 6) * scale) / 2, 0))
        };

        // render levels into textures
        let texture_creator = canvas.texture_creator();
        let (left, right) = self.level.render(scale);
        let (left, right) = (
            texture_creator.create_texture_from_surface(left).unwrap(),
            texture_creator.create_texture_from_surface(right).unwrap(),
        );

        // render it onto the canvas
        canvas
            .copy(
                &left,
                None,
                Some(Rect::new(
                    (xoff + 2 * scale) as i32,
                    (yoff + scale) as i32,
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
                    (yoff + scale) as i32,
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

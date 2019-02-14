mod events;
mod level;
mod moves;

use std::time::Duration;

use sdl2::render::WindowCanvas;
use sdl2::{event::Event, keyboard::Keycode, pixels::Color};

pub use events::Events;
pub use level::Level;
pub use moves::Moves;

pub struct Game {
    events: Events,
    canvas: WindowCanvas,
}

impl Game {
    pub fn new(canvas: WindowCanvas, events: Events) -> Self {
        Game { canvas, events }
    }

    pub fn iter(&mut self) {
        self.canvas.set_draw_color(Color::RGB(0, 255, 255));
        self.canvas.clear();
        self.canvas.present();
        let mut i = 0;
        'running: loop {
            i = (i + 1) % 255;
            self.canvas.set_draw_color(Color::RGB(i, 64, 255 - i));
            self.canvas.clear();
            for event in self.events.poll_iter() {
                match event {
                    Event::Quit { .. }
                    | Event::KeyDown {
                        keycode: Some(Keycode::Escape),
                        ..
                    } => break 'running,
                    _ => {}
                }
            }
            // The rest of the game loop goes here...

            self.canvas.present();
            ::std::thread::sleep(Duration::new(0, 1_000_000_000u32 / 60));
        }
    }
}

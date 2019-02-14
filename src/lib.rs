#[macro_use]
extern crate serde_derive;

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
    running: bool,
    events: Events,
    canvas: WindowCanvas,
}

impl Game {
    pub fn new(canvas: WindowCanvas, events: Events) -> Self {
        Game {
            running: true,
            canvas,
            events,
        }
    }

    pub fn running(&self) -> bool {
        self.running
    }

    pub fn iter(&mut self) {
        self.canvas.set_draw_color(Color::RGB(0, 100, 200));
        self.canvas.clear();
        for event in self.events.poll_iter() {
            match event {
                Event::Quit { .. }
                | Event::KeyDown {
                    keycode: Some(Keycode::Escape),
                    ..
                } => self.running = false,
                _ => {}
            }
        }
        self.canvas.present();
        ::std::thread::sleep(Duration::new(0, 1_000_000_000u32 / 60));
    }
}

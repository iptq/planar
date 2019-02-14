#[macro_use]
extern crate serde_derive;

mod block;
mod events;
mod level;
mod moves;
mod segment;
mod shape;
pub mod state;

use std::time::{Duration, Instant};

use sdl2::event::Event;
use sdl2::pixels::Color;
use sdl2::render::WindowCanvas;

pub use block::Block;
pub use events::Events;
pub use level::Level;
pub use moves::Moves;
pub use segment::Segment;
pub use shape::{Shape, SlidingDirection};
pub use state::State;

pub struct Game {
    last_update: Instant,
    running: bool,
    state_stack: Vec<Box<State>>,
    events: Events,
    canvas: WindowCanvas,
}

impl Game {
    pub fn new(canvas: WindowCanvas, events: Events) -> Self {
        Game {
            last_update: Instant::now(),
            running: true,
            state_stack: Vec::new(),
            canvas,
            events,
        }
    }

    pub fn running(&self) -> bool {
        self.running
    }

    pub fn iter(&mut self) {
        let now = Instant::now();
        let delta = now - self.last_update;

        self.canvas.set_draw_color(Color::RGB(17, 17, 17));
        self.canvas.clear();

        // gather all the events
        let events = self.events.poll_iter().collect::<Vec<_>>();

        // catch quit event
        for event in events.iter() {
            match event {
                Event::Quit { .. } => self.running = false,
                _ => (),
            }
        }

        // update topmost state
        if let Some(topmost) = self.state_stack.iter().last() {
            topmost.update(delta);
        }

        // render states
        // TODO: optimize by finding out the topmost nontransparent
        for state in self.state_stack.iter() {
            state.render(&mut self.canvas);
        }

        self.canvas.present();
        self.last_update = now;
        ::std::thread::sleep(Duration::new(0, 1_000_000_000u32 / 60));
    }

    pub fn push_state(&mut self, state: impl State + 'static) {
        self.state_stack.push(Box::new(state))
    }
}

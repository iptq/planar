mod game;

use sdl2::event::Event;
use std::fmt::Debug;
use std::time::Duration;

use sdl2::render::WindowCanvas;

pub use self::game::GameState;

pub trait State: Debug {
    fn is_transparent(&self) -> bool;
    fn update(&mut self, _: Duration, _: Vec<Event>) {}
    fn render(&mut self, _: &mut WindowCanvas) {}
}

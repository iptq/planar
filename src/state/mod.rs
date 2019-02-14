mod game;

use std::fmt::Debug;
use std::time::Duration;

use sdl2::render::WindowCanvas;

pub use self::game::GameState;

pub trait State: Debug {
    fn is_transparent(&self) -> bool;
    fn update(&self, _: Duration) {}
    fn render(&self, _: &mut WindowCanvas) {}
}

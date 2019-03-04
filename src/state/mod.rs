mod edit;
mod game;
mod menu;

use std::time::Duration;

use sdl2::render::WindowCanvas;

use crate::Event;

pub use self::edit::EditState;
pub use self::game::GameState;
pub use self::menu::MenuState;

pub trait State {
    fn is_transparent(&self) -> bool {
        false
    }

    fn update(&mut self, _: Duration, _: Vec<Event>) {}

    fn render(&mut self, _: &mut WindowCanvas) {}
}

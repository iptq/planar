mod game;

use std::time::Duration;

pub use self::game::GameState;

pub trait State {
    fn is_transparent(&self) -> bool;
    fn update(&self, _: Duration) {}
    fn render(&self) {}
}

use super::State;
use crate::Level;

pub struct GameState<'a> {
    level: Level<'a>,
}

impl<'a> State for GameState<'a> {
    fn is_transparent(&self) -> bool {
        false
    }
}

impl<'a> GameState<'a> {
    pub fn new(level: Level<'a>) -> Self {
        GameState { level }
    }
}

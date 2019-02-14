use std::fs::File;
use std::io::Read;

use failure::Error;
use planar::{state::GameState, Events, Game, Level};

fn load_level<'a>() -> Result<Level<'a>, Error> {
    let mut file = File::open("levels/1.json")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let repr = serde_json::from_str(&contents)?;
    let level = Level::new(repr)?;
    Ok(level)
}

fn main() {
    let sdl_context = sdl2::init().unwrap();
    let event_pump = sdl_context.event_pump().unwrap();
    let video_subsystem = sdl_context.video().unwrap();

    let window = video_subsystem
        .window("planar", 800, 600)
        .position_centered()
        .build()
        .unwrap();

    let canvas = window.into_canvas().build().unwrap();
    let events = Events::new(event_pump);
    let mut game = Game::new(canvas, events);

    let level = load_level().unwrap();
    let game_state = GameState::new(level);
    game.push_state(game_state);

    while game.running() {
        game.iter();
    }
}

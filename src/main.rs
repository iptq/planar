use std::io::Cursor;

use failure::Error;
use packer::Packer;
use planar::{self, state::GameState, Events, Game, Level, Levels};
use ref_thread_local::{ref_thread_local, RefThreadLocal};
use sdl2::Sdl;

fn load_level<'a>() -> Result<Level<'a>, Error> {
    let repr = serde_json::from_reader(Cursor::new(Levels::get("tutorial.json").unwrap()))?;
    let level = Level::from(repr)?;
    Ok(level)
}

ref_thread_local! {
    static managed sdl_context: Sdl = sdl2::init().unwrap();
    static managed GAME: Game = {
        let event_pump = sdl_context.borrow().event_pump().unwrap();
        let video_subsystem = sdl_context.borrow().video().unwrap();

        let window = video_subsystem
            .window("planar", 1366, 768)
            .resizable()
            .position_centered()
            .build()
            .unwrap();

        let canvas = window.into_canvas().build().unwrap();
        let events = Events::new(event_pump);
        let mut game = Game::new(canvas, events);

        let level = load_level().unwrap();
        let game_state = GameState::new(level);
        game.push_state(game_state);

        game
    };
}

#[cfg(target_arch = "wasm32")]
extern "C" fn main_loop() {
    GAME.borrow_mut().iter();
}

fn main() {
    #[cfg(target_arch = "wasm32")]
    unsafe {
        planar::emscripten::emscripten_set_main_loop(Some(main_loop), 0, 1);
    }

    #[cfg(not(target_arch = "wasm32"))]
    {
        let mut game = GAME.borrow_mut();
        while game.running() {
            game.iter();
        }
    }
}

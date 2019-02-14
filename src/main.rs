use planar::{Events, Game};

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

    while game.running() {
        game.iter();
    }
}

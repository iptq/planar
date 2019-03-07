use std::time::Duration;

use sdl2::pixels::Color;
use sdl2::rect::Rect;
use sdl2::render::WindowCanvas;

use crate::ui::Button;
use crate::Renderer;
use crate::State;
use crate::Event;

pub struct MenuState {
    renderer: Renderer,
    play_btn: usize,
}

impl MenuState {
    pub fn new() -> MenuState {
        let mut renderer = Renderer::new();

        let btn = Button::new(5, 5, 10, 10, Color::RGB(170, 170, 170), "hello".to_owned());
        let play_btn = renderer.insert(btn);

        MenuState { renderer, play_btn }
    }
}

impl State for MenuState {
    fn update(&mut self, _: Duration, events: Vec<Event>) {
    }

    fn render(&mut self, canvas: &mut WindowCanvas) {
        let texture_creator = canvas.texture_creator();
        let (loc, surface) = self.renderer.render();
        let (width, height) = (surface.width(), surface.height());
        let texture = texture_creator
            .create_texture_from_surface(surface)
            .unwrap();
        canvas.copy(&texture, None, Rect::new(loc.0, loc.1, width, height));
    }
}

use std::time::Duration;

use sdl2::surface::Surface;

pub trait Drawable {
    fn draw<'a>(&mut self) -> Surface<'a>;
}

pub enum Easing {
    Linear,
}

pub trait Transition {}

pub struct TransitionInstance<T: Transition> {
    inner: T,
    progress: Duration,
}

impl<T: Transition> TransitionInstance<T> {
    pub fn new(inner: T) -> Self {
        TransitionInstance {
            inner,
            progress: Duration::from_secs(0),
        }
    }
}

pub struct Move<D: Drawable>(pub D);

impl<D: Drawable> Transition for Move<D> {}

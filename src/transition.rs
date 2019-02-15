use std::time::Duration;

use sdl2::surface::Surface;

pub trait Drawable {
    fn draw<'a>(&self) -> Surface<'a>;
}

pub enum TransitionKind {

}

pub struct TransitionInstance {
    inner: Transition,
    progress: Duration,
}

impl TransitionInstance {
    pub fn new(inner: Transition) -> Self {
        TransitionInstance {
            inner,
            progress: Duration::from_secs(0)
        }
    }
}

pub struct Transition {
    kind: TransitionKind,
    duration: Duration,
}

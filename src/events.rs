use sdl2::{event::EventPollIterator, EventPump};

// TODO: eventually have an abstracted view of events that only consist of
// ones that are of interest to the game (i.e. normalize mouse/touch)

pub struct Events {
    event_pump: EventPump,
}

impl Events {
    pub fn new(event_pump: EventPump) -> Self {
        Events { event_pump }
    }

    pub fn poll_iter(&mut self) -> EventPollIterator {
        self.event_pump.poll_iter()
    }
}

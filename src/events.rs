use sdl2::{event::{EventPollIterator, Event as SdlEvent}, EventPump};

// TODO: eventually have an abstracted view of events that only consist of
// ones that are of interest to the game (i.e. normalize mouse/touch)

#[derive(Debug)]
pub enum Event {
    Quit,

    LeftMoveUp,
    LeftMoveDown,
    LeftMoveLeft,
    LeftMoveRight,
    RightMoveUp,
    RightMoveDown,
    RightMoveLeft,
    RightMoveRight,

    Unknown(SdlEvent),
}

pub struct Events {
    event_pump: EventPump,
}

impl From<SdlEvent> for Event {
    fn from(evt: SdlEvent) -> Self {
        match evt {
            SdlEvent::Quit { .. } => Event::Quit,
            evt => Event::Unknown(evt)
        }
    }
}

pub struct EventIterator<'a>(EventPollIterator<'a>);

impl<'a> Iterator for EventIterator<'a> {
    type Item = Event;
    fn next(&mut self) -> Option<Self::Item> {
        self.0.next().map(Event::from)
    }
}

impl Events {
    pub fn new(event_pump: EventPump) -> Self {
        Events { event_pump }
    }

    pub fn iter<'a>(&mut self) -> EventIterator {
        EventIterator(self.event_pump.poll_iter())
    }
}

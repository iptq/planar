#[derive(Debug, PartialEq, Eq, Hash)]
pub enum Shape {}

#[derive(Debug, PartialEq, Eq, Hash)]
pub enum SlidingDirection {
    Horizontal,
    Vertical,
}

#[derive(Debug, PartialEq, Eq, Hash)]
pub enum Direction {
    Up,
    Down,
    Left,
    Right,
}

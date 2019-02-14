#[derive(Debug, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum Shape {
    Rectangle,
    TopLeft,
    TopRight,
    BottomLeft,
    BottomRight,
}

#[derive(Debug, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum SlidingDirection {
    Horizontal,
    Vertical,
}

#[derive(Debug, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum Direction {
    Up,
    Down,
    Left,
    Right,
}

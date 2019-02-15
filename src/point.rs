use std::ops::Add;

use crate::Direction;

#[derive(Clone, Debug, Serialize, Deserialize, Eq, PartialEq, Hash)]
pub struct Point<T>(pub T, pub T);

impl<T: Add<Output = T>> Add for Point<T> {
    type Output = Point<T>;

    fn add(self, rhs: Point<T>) -> Self::Output {
        Point(self.0 + rhs.0, self.1 + rhs.1)
    }
}

impl Add<Direction> for Point<u32> {
    type Output = Point<u32>;

    fn add(mut self, rhs: Direction) -> Self::Output {
        match rhs {
            Direction::Up => self.0 -= 1,
            Direction::Down => self.0 += 1,
            Direction::Left => self.1 -= 1,
            Direction::Right => self.1 += 1,
        };
        self
    }
}

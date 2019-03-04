use std::ops::{Add, Sub};

use crate::Direction;

#[derive(Clone, Debug, Serialize, Deserialize, Eq, PartialEq, Hash)]
pub struct Point<T>(pub T, pub T);

impl<T: Add<Output = T>> Add for Point<T> {
    type Output = Point<T>;

    fn add(self, rhs: Point<T>) -> Self::Output {
        Point(self.0 + rhs.0, self.1 + rhs.1)
    }
}

impl<T: Sub<Output = T>> Sub for Point<T> {
    type Output = Point<T>;

    fn sub(self, rhs: Point<T>) -> Self::Output {
        Point(self.0 - rhs.0, self.1 - rhs.1)
    }
}

impl Add<Direction> for Point<i32> {
    type Output = Point<i32>;

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

impl Point<i32> {
    pub fn into_unsigned(self) -> Point<u32> {
        Point(self.0 as u32, self.1 as u32)
    }
}

impl Point<u32> {
    pub fn into_signed(self) -> Point<i32> {
        Point(self.0 as i32, self.1 as i32)
    }
}

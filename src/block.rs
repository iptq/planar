use std::sync::Arc;

use failure::Error;
use sdl2::pixels::Color;

use crate::{Point, Segment, SegmentRepr, SlidingDirection};

#[derive(Debug, Serialize, Deserialize)]
pub struct ColorRepr(u8, u8, u8);

#[derive(Debug, Serialize, Deserialize)]
pub struct BlockRepr {
    pub position: Point<u32>,
    pub segments: Vec<SegmentRepr>,
    pub movable: bool,
    pub direction: SlidingDirection,
    pub color: ColorRepr,
}

#[derive(Debug)]
pub struct Block {
    pub position: Point<u32>,
    pub segments: Vec<Arc<Segment>>,
    pub movable: bool,
    direction: SlidingDirection,
    color: Color,
}

impl Block {
    pub fn from(repr: BlockRepr) -> Result<Self, Error> {
        let mut block = Block {
            position: repr.position,
            segments: Vec::new(),
            movable: repr.movable,
            direction: repr.direction,
            color: Color::from((repr.color.0, repr.color.1, repr.color.2)),
        };

        for repr in repr.segments {
            let segment = Segment::from(&block, repr)?;
            block.segments.push(Arc::new(segment));
        }

        Ok(block)
    }

    pub fn get_position(&self) -> Point<u32> {
        self.position.clone()
    }

    pub fn get_direction(&self) -> SlidingDirection {
        self.direction.clone()
    }

    pub fn get_color(&self) -> Color {
        self.color
    }
}

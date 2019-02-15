use failure::{err_msg, Error};
use sdl2::pixels::Color;
use sdl2::pixels::PixelFormatEnum;
use sdl2::surface::Surface;

use crate::{Block, Point, Shape, SlidingDirection};

#[derive(Debug, Serialize, Deserialize)]
pub struct SegmentRepr {
    pub rel_position: Point<u32>,
    pub z: u32,
    pub shape: Shape,
}

#[derive(Debug)]
pub struct Segment {
    pub rel_position: Point<u32>,
    pub z: u32,
    color: Color,
    direction: SlidingDirection,
    shape: Shape,
}

impl Segment {
    pub fn from(parent: &Block, repr: SegmentRepr) -> Result<Self, Error> {
        Ok(Segment {
            rel_position: repr.rel_position,
            z: repr.z,
            color: parent.get_color(),
            direction: parent.get_direction(),
            shape: repr.shape,
        })
    }

    pub fn get_relative_position(&self) -> Point<u32> {
        self.rel_position.clone()
    }

    pub fn get_z(&self) -> u32 {
        self.z
    }

    pub fn get_shape(&self) -> Shape {
        self.shape.clone()
    }

    pub fn get_direction(&self) -> SlidingDirection {
        self.direction.clone()
    }

    pub fn get_color(&self) -> Color {
        self.color
    }

    pub fn render<'a>(&self, cell_size: u32) -> Result<Surface<'a>, Error> {
        let surface =
            Surface::new(cell_size, cell_size, PixelFormatEnum::RGB24).map_err(err_msg)?;
        Ok(surface)
    }
}

use failure::{err_msg, Error};
use sdl2::pixels::PixelFormatEnum;
use sdl2::surface::Surface;

use crate::{Block, Shape, SlidingDirection};

#[derive(Debug, Serialize, Deserialize)]
pub struct SegmentRepr {
    pub rel_position: (u32, u32),
    pub z: u32,
    pub shape: Shape,
}

#[derive(Debug)]
pub struct Segment {
    direction: SlidingDirection,
    shape: Shape,
}

impl Segment {
    pub fn from(parent: &Block, repr: SegmentRepr) -> Result<Self, Error> {
        Ok(Segment {
            direction: parent.get_direction(),
            shape: repr.shape,
        })
    }

    pub fn get_shape(&self) -> Shape {
        self.shape.clone()
    }

    pub fn render<'a>(&self, cell_size: u32) -> Result<Surface<'a>, Error> {
        let surface =
            Surface::new(cell_size, cell_size, PixelFormatEnum::RGB24).map_err(err_msg)?;
        Ok(surface)
    }
}

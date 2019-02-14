use std::collections::HashMap;
use std::sync::Arc;

use debug_stub_derive::DebugStub;
use failure::Error;
use sdl2::pixels::{Color, PixelFormatEnum};
use sdl2::surface::Surface;

use crate::{Block, BlockRepr, Moves, Segment, Shape, SlidingDirection};

#[derive(Debug, Serialize, Deserialize)]
pub struct LevelRepr {
    pub version: u8,
    pub dimensions: (u32, u32),
    pub blocks: Vec<BlockRepr>,
}

#[derive(DebugStub, Default)]
pub struct Level<'a> {
    blocks: Vec<Arc<Block>>,
    segments: Vec<Arc<Segment>>,
    dimensions: (u32, u32),

    cell_map: HashMap<(i32, i32), i32>,
    complete: bool,
    move_stack: Vec<Moves>,
    #[debug_stub = "OpaqueHashmap"]
    segment_cache: HashMap<(Shape, SlidingDirection, Color), Surface<'a>>,
}

impl<'a> Level<'a> {
    pub fn new(repr: LevelRepr) -> Result<Self, Error> {
        let mut level = Level::default();
        level.dimensions = repr.dimensions;
        Ok(level)
    }

    pub fn dimensions(&self) -> (u32, u32) {
        self.dimensions
    }

    pub fn render(&self, cell_size: u32) -> (Surface, Surface) {
        let left_surface = Surface::new(
            self.dimensions.0 * cell_size,
            self.dimensions.1 * cell_size,
            PixelFormatEnum::RGB24,
        )
        .unwrap();
        let right_surface = Surface::new(
            self.dimensions.0 * cell_size,
            self.dimensions.1 * cell_size,
            PixelFormatEnum::RGB24,
        )
        .unwrap();
        (left_surface, right_surface)
    }
}

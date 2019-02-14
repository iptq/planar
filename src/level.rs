use std::collections::HashMap;
use std::sync::Arc;

use debug_stub_derive::DebugStub;
use failure::Error;
use sdl2::pixels::{Color, PixelFormatEnum};
use sdl2::rect::Rect;
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
    segment_cache: HashMap<(u32, Shape, SlidingDirection, Color), Surface<'a>>,
}

impl<'a> Level<'a> {
    pub fn from(repr: LevelRepr) -> Result<Self, Error> {
        let mut level = Level::default();
        level.dimensions = repr.dimensions;

        // load blocks
        for repr in repr.blocks {
            let block = Block::from(repr)?;
            for segment in block.segments.iter() {
                let segment = segment.clone();
                level.segments.push(segment);
            }
            level.blocks.push(Arc::new(block));
        }
        println!("{:?}", level.segment_cache.len());

        Ok(level)
    }

    pub fn dimensions(&self) -> (u32, u32) {
        self.dimensions
    }

    fn render_segment(
        &self,
        segment: impl AsRef<Segment>,
        cell_size: u32,
    ) -> Result<Surface<'a>, Error> {
        let segment = segment.as_ref();
        segment.render(cell_size)
        // level.segment_cache.insert(
        //     (
        //         segment.get_shape(),
        //         block.get_direction(),
        //         block.get_color(),
        //     ),
        //     segment.render(cell_size)?,
        // );
    }

    pub fn render(&self, cell_size: u32) -> (Surface, Surface) {
        let (rows, columns) = self.dimensions;
        let left_surface = Surface::new(
            columns * cell_size,
            rows * cell_size,
            PixelFormatEnum::RGB24,
        )
        .unwrap();
        let right_surface = Surface::new(
            columns * cell_size,
            rows * cell_size,
            PixelFormatEnum::RGB24,
        )
        .unwrap();

        let (mut left_canvas, mut right_canvas) = (
            left_surface.into_canvas().unwrap(),
            right_surface.into_canvas().unwrap(),
        );

        let mut layers = [&mut left_canvas, &mut right_canvas];
        for layer in layers.iter_mut() {
            layer.set_draw_color(Color::from((200, 200, 200)));
            for r in 0..rows {
                for c in 0..columns {
                    layer
                        .fill_rect(Rect::new(
                            (cell_size * c) as i32,
                            (cell_size * r) as i32,
                            cell_size - 1,
                            cell_size - 1,
                        ))
                        .unwrap();
                }
            }
        }

        (left_canvas.into_surface(), right_canvas.into_surface())
    }
}

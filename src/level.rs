use std::collections::{HashMap, HashSet};
use std::sync::Arc;

use debug_stub_derive::DebugStub;
use failure::Error;
use sdl2::pixels::{Color, PixelFormatEnum};
use sdl2::rect::Rect;
use sdl2::render::{Canvas, RenderTarget};
use sdl2::surface::Surface;

use crate::{
    Block, BlockRepr, Direction, Moves, Player, PlayerRepr, Point, Segment, Shape, SlidingDirection,
};

#[derive(Debug, Serialize, Deserialize)]
pub struct LevelRepr {
    pub version: u8,
    pub dimensions: Point<u32>,
    pub blocks: Vec<BlockRepr>,
    pub players: (PlayerRepr, PlayerRepr),
}

#[derive(Debug)]
enum Cell {
    Single(Arc<Segment>),
    // self.0 / self.1
    Diagonal(Arc<Segment>, Arc<Segment>),
    // self.0 \ self.1
    Diagonal2(Arc<Segment>, Arc<Segment>),
}

#[derive(DebugStub)]
pub struct Level<'a> {
    blocks: Vec<Arc<Block>>,
    segments: Vec<Arc<Segment>>,
    dimensions: Point<u32>,
    players: (Player, Player),

    cell_map: HashMap<(i32, i32), Cell>,
    complete: bool,
    move_stack: Vec<Moves>,

    #[debug_stub = "OpaqueHashmap"]
    segment_cache: HashMap<(u32, Shape, SlidingDirection, Color), Surface<'a>>,
}

impl<'a> Level<'a> {
    pub fn from(repr: LevelRepr) -> Result<Self, Error> {
        let player_left = Player::from(repr.players.0)?;
        let player_right = Player::from(repr.players.1)?;

        let mut level = Level {
            blocks: Vec::new(),
            segments: Vec::new(),
            dimensions: repr.dimensions,
            players: (player_left, player_right),

            cell_map: HashMap::new(),
            complete: false,
            move_stack: Vec::new(),

            segment_cache: HashMap::new(),
        };

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

    pub fn dimensions(&self) -> Point<u32> {
        self.dimensions.clone()
    }

    fn try_move_rec(
        &self,
        block: impl AsRef<Block>,
        direction: Direction,
        moveset: &mut HashSet<()>,
    ) {
        let block = block.as_ref();

        // check if each of its segments can move
        for segment in block.segments.iter() {
            // where's this segment going to go?
            let target = block.get_position() + segment.get_relative_position() + direction.clone();
        }
    }

    fn try_move(&self, block: impl AsRef<Block>, direction: Direction) {
        let mut moves = HashSet::new();
        self.try_move_rec(block, direction, &mut moves)
    }

    fn render_segment(
        &mut self,
        segment: impl AsRef<Segment>,
        cell_size: u32,
    ) -> Result<Surface<'a>, Error> {
        let segment = segment.as_ref();
        let key = (
            cell_size,
            segment.get_shape(),
            segment.get_direction(),
            segment.get_color(),
        );

        let mut result_surface =
            Surface::new(cell_size, cell_size, PixelFormatEnum::RGBA8888).unwrap();
        let entry = self.segment_cache.get(&key);
        match entry {
            Some(entry) => {
                entry.blit(None, &mut result_surface, None).unwrap();
            }
            None => {
                let result = segment.render(cell_size)?;
                result.blit(None, &mut result_surface, None).unwrap();
                self.segment_cache.insert(key, result);
            }
        };

        Ok(result_surface)
    }

    pub fn render(&mut self, cell_size: u32) -> (Surface, Surface) {
        let Point(rows, columns) = self.dimensions;
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

        let mut render = Vec::new();
        for block in self.blocks.iter() {
            layers[0].set_draw_color(block.get_color());
            layers[1].set_draw_color(block.get_color());

            for segment in block.segments.iter() {
                let Point(mut r, mut c) = block.get_position();
                let Point(relr, relc) = segment.get_relative_position();
                r += relr;
                c += relc;

                let z = segment.get_z();
                render.push((
                    z as usize,
                    Rect::new(
                        (cell_size * c) as i32,
                        (cell_size * r) as i32,
                        cell_size - 1,
                        cell_size - 1,
                    ),
                    segment.clone(),
                ));
            }
        }

        for (z, rect, segment) in render {
            let texture_creator = layers[z].texture_creator();
            let surface = self.render_segment(segment, cell_size).unwrap();
            let texture = texture_creator
                .create_texture_from_surface(surface)
                .unwrap();
            layers[z].copy(&texture, None, rect).unwrap();
        }

        (left_canvas.into_surface(), right_canvas.into_surface())
    }
}

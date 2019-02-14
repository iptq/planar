use crate::{SegmentRepr, SlidingDirection};

#[derive(Debug, Serialize, Deserialize)]
pub struct ColorRepr(u8, u8, u8);

#[derive(Debug, Serialize, Deserialize)]
pub struct BlockRepr {
    pub position: (u32, u32),
    pub segments: Vec<SegmentRepr>,
    pub movable: bool,
    pub direction: SlidingDirection,
    pub color: ColorRepr,
}

#[derive(Debug)]
pub struct Block {}

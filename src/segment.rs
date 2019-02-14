use crate::shape::Shape;

#[derive(Debug, Serialize, Deserialize)]
pub struct SegmentRepr {
    pub rel_position: (u32, u32),
    pub z: u32,
    pub shape: Shape,
}

#[derive(Debug)]
pub struct Segment {}

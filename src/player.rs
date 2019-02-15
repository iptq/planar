use crate::Point;
use failure::Error;

#[derive(Debug, Serialize, Deserialize)]
pub struct PlayerRepr {
    pub position: Point<u32>,
    pub z: u32,
}

#[derive(Debug)]
pub struct Player {
    position: Point<u32>,
    z: u32,
}

impl Player {
    pub fn from(repr: PlayerRepr) -> Result<Player, Error> {
        Ok(Player {
            position: repr.position,
            z: repr.z,
        })
    }
}

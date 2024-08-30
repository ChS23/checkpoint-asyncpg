from langgraph.checkpoint.base import (
    ChannelVersions,
    Checkpoint,
    CheckpointMetadata,
    CheckpointTuple,
    get_checkpoint_id,
)
from langgraph.checkpoint.asyncpg.base import BasePostgresSaver
from langgraph.checkpoint.serde.base import SerializerProtocol


class AsyncPostgresSaver(BasePostgresSaver):
    def __init__(self):
        super().__init__(serde=serde)
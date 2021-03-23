import datetime
from enum import Enum, unique

from .owner import Owner
from .primitives.base import BaseTolokaObject


class Attachment(BaseTolokaObject, spec_enum='Type', spec_field='attachment_type'):
    """Attachment

    Files uploaded by users are saved in Toloka.
    Attributes:
        id: File ID.
        name: File name.
        details: Infomation about the pool, the task, and the user who uploaded the file.
        created: The date when the file was uploaded to Toloka.
        media_type: MIME type of the data.
        owner: Owner
    """

    @unique
    class Type(Enum):
        ASSIGNMENT_ATTACHMENT = 'ASSIGNMENT_ATTACHMENT'

    ASSIGNMENT_ATTACHMENT = Type.ASSIGNMENT_ATTACHMENT

    class Details(BaseTolokaObject):
        """Infomation about the pool, the task, and the user who uploaded the file.

        Attributes:
            user_id: ID of the user who uploaded the file.
            assignment_id: ID of the task suite assignment to a user.
            pool_id: Pool ID.
        """

        user_id: str
        assignment_id: str
        pool_id: str

    id: str
    name: str
    details: Details
    created: datetime.datetime
    media_type: str

    owner: Owner


class AssignmentAttachment(Attachment, spec_value=Attachment.Type.ASSIGNMENT_ATTACHMENT):
    pass

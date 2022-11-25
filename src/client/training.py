__all__ = ['Training']
import datetime
from enum import unique
from typing import Dict, List

from .owner import Owner
from .primitives.base import BaseTolokaObject
from ..util._codegen import attribute, codegen_attr_attributes_setters
from ..util._extendable_enum import ExtendableStrEnum


@codegen_attr_attributes_setters
class Training(BaseTolokaObject):
    """A training pool.

    A training pool contains tasks with known solutions and hints for Tolokers. Use training pools:
    - To train Tolokers so they solve general tasks better.
    - To select Tolokers who successfully completed training tasks.

    To link a trining pool to a general pool setup the [Pool](toloka.client.pool.Pool.md).[quality_control](toloka.client.quality_control.QualityControl.md).[training_requirement](toloka.client.quality_control.QualityControl.TrainingRequirement.md) parameter.

    For more information, see [Adding a training](https://toloka.ai/en/docs/guide/concepts/train).

    Attributes:
        project_id: The ID of the project containing the training.
        private_name: The training pool name. It is visible to the requester only.
        may_contain_adult_content: The presence of adult content.
        assignment_max_duration_seconds: Time limit to complete a task suite.
            Take into account loading a page with a task suite and sending responses to the server. It is recommended that you set at least 60 seconds.
        mix_tasks_in_creation_order:
            * True — Tasks are grouped in suites in the order they were created.
            * False — Tasks are chosen for a task suite in a random order.

            Default: False.
        shuffle_tasks_in_task_suite:
            * True — Tasks from a task suite are shuffled on the page.
            * False — Tasks from a task suite are placed on the page in the order they were created.

            Default: False.
        training_tasks_in_task_suite_count: The number of training tasks in one suite.
        task_suites_required_to_pass: The number of task suites that must be completed by a Toloker to get a training skill.
        retry_training_after_days: The training has to be completed again after the specified number of days to continue working with general tasks.
             If the parameter is not specified, then the training skill is issued for an unlimited time.
        inherited_instructions:
            * True — Project instructions are used in the training pool.
            * False — Instruction, specified in the `public_instructions` parameter, are used.

            Default: False.
        public_instructions: Instructions for Tolokers used when the `inherited_instructions` parameter is False. Describe there how to complete training tasks.
            You can use HTML markup inside `public_instructions`.
        metadata: A dictionary with metadata.
        owner: A training pool owner.
        id: The ID of the training pool. Read only.
        status: A training pool status. Read only.
        last_close_reason: A reason why the training pool was closed last time.
        created: The UTC date and time when the training pool was created. Read only.
        last_started: The UTC date and time when the training pool was started last time. Read only.
        last_stopped: The UTC date and time when the training pool was stopped last time. Read only.
    """

    @unique
    class CloseReason(ExtendableStrEnum):
        """A reason for closing a pool.

        Attributes:
            MANUAL: A pool was closed by a requester.
            EXPIRED: The lifetime of the main pool has expired.
            COMPLETED: All main pool tasks were completed.
            NOT_ENOUGH_BALANCE: There is not enough money to run the main pool.
            ASSIGNMENTS_LIMIT_EXCEEDED: A limit of 2 millions assignments is reached.
            BLOCKED: The requester's account was blocked.
        """
        MANUAL = 'MANUAL'
        EXPIRED = 'EXPIRED'
        COMPLETED = 'COMPLETED'
        NOT_ENOUGH_BALANCE = 'NOT_ENOUGH_BALANCE'
        ASSIGNMENTS_LIMIT_EXCEEDED = 'ASSIGNMENTS_LIMIT_EXCEEDED'
        BLOCKED = 'BLOCKED'
        FOR_UPDATE = 'FOR_UPDATE'

    @unique
    class Status(ExtendableStrEnum):
        """The status of a training pool.

        Attributes:
            OPEN: The training pool is open.
            CLOSED: The training pool is closed.
            ARCHIVED: The training pool is archived.
            LOCKED: The training pool is locked.
        """
        OPEN = 'OPEN'
        CLOSED = 'CLOSED'
        ARCHIVED = 'ARCHIVED'
        LOCKED = 'LOCKED'

    project_id: str
    private_name: str
    may_contain_adult_content: bool
    assignment_max_duration_seconds: int
    mix_tasks_in_creation_order: bool
    shuffle_tasks_in_task_suite: bool
    training_tasks_in_task_suite_count: int
    task_suites_required_to_pass: int
    retry_training_after_days: int
    inherited_instructions: bool
    public_instructions: str

    metadata: Dict[str, List[str]]
    owner: Owner

    # Readonly
    id: str = attribute(readonly=True)
    status: Status = attribute(readonly=True)
    last_close_reason: CloseReason = attribute(readonly=True)
    created: datetime.datetime = attribute(readonly=True)
    last_started: datetime.datetime = attribute(readonly=True)
    last_stopped: datetime.datetime = attribute(readonly=True)

    def is_open(self) -> bool:
        return self.status == Training.Status.OPEN

    def is_closed(self) -> bool:
        return self.status == Training.Status.CLOSED

    def is_archived(self) -> bool:
        return self.status == Training.Status.ARCHIVED

    def is_locked(self) -> bool:
        return self.status == Training.Status.LOCKED

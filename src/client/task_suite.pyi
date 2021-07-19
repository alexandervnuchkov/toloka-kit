from datetime import datetime
from toloka.client.primitives.base import BaseTolokaObject
from toloka.client.primitives.infinite_overlap import InfiniteOverlapParametersMixin
from toloka.client.primitives.parameter import Parameters
from toloka.client.task import BaseTask
from typing import (
    Any,
    Dict,
    List,
    Optional,
    overload
)
from uuid import UUID

class TaskSuite(InfiniteOverlapParametersMixin, BaseTolokaObject):
    """A set of tasks issued to the performer at a time

    TaskSuite can contain one or more tasks. The execution price is charged for one TaskSuite.
    Performers receive exactly one TaskSuite when they take on your task.

    Attributes:
        pool_id: The ID of the pool that task suite are uploaded to.
        tasks: Data for the tasks.
        reserved_for: IDs of users who will have access to the task suite.
        unavailable_for: IDs of users who shouldn't have access to the task suite.
        issuing_order_override: The priority of a task suite among other sets in the pool. Defines the order in which
            task suites are assigned to performers. The larger the parameter value, the higher the priority.
            This parameter can be used if the pool has issue_task_suites_in_creation_order: true.
            Allowed values: from -99999.99999 to 99999.99999.
        mixed: Type of operation for creating a task suite:
            * True - Automatically with the "smart mixing" option (for details, see Yandex.Toloka requester's guide).
            * False - Manually.
        traits_all_of:
        traits_any_of:
        traits_none_of_any:
        longitude: The longitude of the point on the map for the task suite.
        latitude: The latitude of the point on the map for the task suite.
        id: ID of a task suite. Read only field.
        remaining_overlap: How many times will this Task Suite be issued to performers. Read only field.
        automerged: The task suite flag is created after task merging. Read Only field. Value:
            * True - The task suite is generated as a result of merging identical tasks.
            * False - A standard task suite created by "smart mixing" or by the requester.
        created: The UTC date and time when the task suite was created. Read Only field.
    """

    def __init__(
        self,
        *,
        infinite_overlap=None,
        overlap=None,
        pool_id: Optional[str] = None,
        tasks: Optional[List[BaseTask]] = ...,
        reserved_for: Optional[List[str]] = None,
        unavailable_for: Optional[List[str]] = None,
        issuing_order_override: Optional[float] = None,
        mixed: Optional[bool] = None,
        traits_all_of: Optional[List[str]] = None,
        traits_any_of: Optional[List[str]] = None,
        traits_none_of_any: Optional[List[str]] = None,
        longitude: Optional[float] = None,
        latitude: Optional[float] = None,
        id: Optional[str] = None,
        remaining_overlap: Optional[int] = None,
        automerged: Optional[bool] = None,
        created: Optional[datetime] = None
    ) -> None:
        """Method generated by attrs for class TaskSuite.
        """
        ...

    @overload
    def add_base_task(
        self,
        *,
        input_values: Optional[Dict[str, Any]] = None,
        known_solutions: Optional[List[BaseTask.KnownSolution]] = None,
        message_on_unknown_solution: Optional[str] = None
    ) -> 'TaskSuite': ...

    @overload
    def add_base_task(self, base_task: BaseTask) -> 'TaskSuite': ...

    _unexpected: Optional[Dict[str, Any]]
    _infinite_overlap: Optional[bool]
    _overlap: Optional[int]
    pool_id: Optional[str]
    tasks: Optional[List[BaseTask]]
    reserved_for: Optional[List[str]]
    unavailable_for: Optional[List[str]]
    issuing_order_override: Optional[float]
    mixed: Optional[bool]
    traits_all_of: Optional[List[str]]
    traits_any_of: Optional[List[str]]
    traits_none_of_any: Optional[List[str]]
    longitude: Optional[float]
    latitude: Optional[float]
    id: Optional[str]
    remaining_overlap: Optional[int]
    automerged: Optional[bool]
    created: Optional[datetime]


class TaskSuiteCreateRequestParameters(Parameters):
    """Parameters for TaskSuite creation controlling

    Attributes:
        operation_id: Operation ID for asynchronous loading of task suites.
        skip_invalid_items: Validation parameters:
            * True - Create the task suites that passed validation. Skip the rest of the task suites.
            * False - If at least one of the task suites didn't pass validation, stop the operation and
                don't create the task suites.
        allow_defaults: Overlap settings:
            * True - Use the overlap that is set in the pool parameters.
            * False - Use the overlap that is set in the task suite parameters (in the overlap field).
        open_pool: Open the pool immediately after creating a task suite, if the pool is closed.
        async_mode: How the request is processed:
            * True — deferred. The query results in an asynchronous operation running in the background.
                Answer contains information about the operation (start and end time, status, number of sets).
            * False — synchronous. Answer contains information about the generated sets of tasks.
                You can send a maximum of 5000 task sets in a single request.
    """

    def __init__(
        self,
        *,
        operation_id: Optional[UUID] = None,
        skip_invalid_items: Optional[bool] = None,
        allow_defaults: Optional[bool] = None,
        open_pool: Optional[bool] = None,
        async_mode: Optional[bool] = True
    ) -> None:
        """Method generated by attrs for class TaskSuiteCreateRequestParameters.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    operation_id: Optional[UUID]
    skip_invalid_items: Optional[bool]
    allow_defaults: Optional[bool]
    open_pool: Optional[bool]
    async_mode: Optional[bool]


class TaskSuiteOverlapPatch(BaseTolokaObject):
    """Parameters to stop issuing a specific TaskSuite
    """

    def __init__(self, *, overlap: Optional[int] = None) -> None:
        """Method generated by attrs for class TaskSuiteOverlapPatch.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    overlap: Optional[int]


class TaskSuitePatch(InfiniteOverlapParametersMixin, BaseTolokaObject):
    """Parameters for changing specific TaskSuite

    Attributes:
        issuing_order_override: The priority of a task suite among other sets in the pool. Defines the order in which
            task suites are assigned to performers. The larger the parameter value, the higher the priority.
            This parameter can be used if the pool has issue_task_suites_in_creation_order: true.
            Allowed values: from -99999.99999 to 99999.99999.
        open_pool: Open the pool immediately after changing a task suite, if the pool is closed.
    """

    def __init__(
        self,
        *,
        infinite_overlap=None,
        overlap=None,
        issuing_order_override: Optional[float] = None,
        open_pool: Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class TaskSuitePatch.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    _infinite_overlap: Optional[bool]
    _overlap: Optional[int]
    issuing_order_override: Optional[float]
    open_pool: Optional[bool]

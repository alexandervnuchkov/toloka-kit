__all__ = [
    'Pipeline',
]
import datetime
import toloka.streaming.observer
import toloka.streaming.storage
import typing


class Pipeline:
    """An entry point for toloka streaming pipelines.
    Allow you to register multiple observers and call them periodically
    while at least one of them may resume.

    Attributes:
        period: Period of observers calls. By default, 60 seconds.
        storage: Optional storage object to save pipeline's state.
            Allow to recover from previous state in case of failure.

    Examples:
        Get assignments from segmentation pool and send them for verification to another pool.

        >>> def handle_submitted(events: List[AssignmentEvent]) -> None:
        >>>     verification_tasks = [create_verification_task(item.assignment) for item in events]
        >>>     toloka_client.create_tasks(verification_tasks, open_pool=True)
        >>>
        >>> def handle_accepted(events: List[AssignmentEvent]) -> None:
        >>>     do_some_aggregation([item.assignment for item in events])
        >>>
        >>> async_toloka_client = AsyncMultithreadWrapper(toloka_client)
        >>>
        >>> observer_123 = AssignmentsObserver(async_toloka_client, pool_id='123')
        >>> observer_123.on_submitted(handle_submitted)
        >>>
        >>> observer_456 = AssignmentsObserver(async_toloka_client, pool_id='456')
        >>> observer_456.on_accepted(handle_accepted)
        >>>
        >>> pipeline = Pipeline()
        >>> pipeline.register(observer_123)
        >>> pipeline.register(observer_456)
        >>> await pipeline.run()
        ...

        One-liners version.

        >>> pipeline = Pipeline()
        >>> pipeline.register(AssignmentsObserver(toloka_client, pool_id='123')).on_submitted(handle_submitted)
        >>> pipeline.register(AssignmentsObserver(toloka_client, pool_id='456')).on_accepted(handle_accepted)
        >>> await pipeline.run()
        ...

        With external storage.

        >>> from toloka.streaming import S3Storage, ZooKeeperLocker
        >>> locker = ZooKeeperLocker(...)
        >>> storage = S3Storage(locker=locker, ...)
        >>> pipeline = Pipeline(storage=storage)
        >>> await pipeline.run()  # Save state after each iteration. Try to load saved at start.
        ...
    """

    def register(self, observer: toloka.streaming.observer.BaseObserver) -> toloka.streaming.observer.BaseObserver:
        """Register given observer.

        Args:
            observer: Observer object.

        Returns:
            The same observer object. It's usable to write one-liners.

        Examples:
            Register observer.

            >>> observer = SomeObserver(pool_id='123')
            >>> observer.do_some_preparations(...)
            >>> toloka_loop.register(observer)
            ...

            One-line version.

            >>> toloka_loop.register(SomeObserver(pool_id='123')).do_some_preparations(...)
            ...
        """
        ...

    def observers_iter(self) -> typing.Iterator[toloka.streaming.observer.BaseObserver]:
        """Iterate over registered observers.

        Returns:
            An iterator over all registered observers except deleted ones.
            May contain observers sheduled to deletion and not deleted yet.
        """
        ...

    def run(self) -> None: ...

    def __init__(
        self,
        period: datetime.timedelta = ...,
        storage: typing.Optional[toloka.streaming.storage.BaseStorage] = None,
        *,
        name: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class Pipeline.
        """
        ...

    period: datetime.timedelta
    storage: typing.Optional[toloka.streaming.storage.BaseStorage]
    name: typing.Optional[str]
    _observers: typing.Dict[int, toloka.streaming.observer.BaseObserver]
    _got_sigint: bool

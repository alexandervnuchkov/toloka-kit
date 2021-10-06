__all__ = [
    'AsyncInterfaceWrapper',
    'AsyncMultithreadWrapper',
    'ComplexException',
    'ensure_async',
    'get_task_traceback',
]
import asyncio.events
import typing


class ComplexException(Exception):
    """Exception to aggregate multiple exceptions occured.
    Unnderlying exceptions are stored in the `exceptions` attribute.

    Attributes:
        exceptions: List of underlying exceptions.
    """

    def __init__(self, exceptions: typing.List[Exception]) -> None:
        """Method generated by attrs for class ComplexException.
        """
        ...

    exceptions: typing.List[Exception]


def ensure_async(func: typing.Callable) -> typing.Callable[..., typing.Awaitable]:
    """Ensure given callable is async.

    Note, that it doesn't provide concurrency by itself!
    It just allow to treat sync and async callables in the same way.

    Args:
        func: Any callable: synchronous or asynchronous.
    Returns:
        Wrapper that return awaitable object at call.
    """
    ...

T = typing.TypeVar('T')

class AsyncInterfaceWrapper(typing.Generic[T]):
    """Wrap arbitrary object to be able to await any of it's methods even if it's sync.

    Note, that it doesn't provide concurrency by itself!
    It just allow to treat sync and async callables in the same way.
    """

    def __init__(self, wrapped:T): ...


class AsyncMultithreadWrapper(typing.Generic[T]):
    """Wrap arbitrary object to run each of it's methods in a separate thread.

    Examples:
        Simple usage example.

        >>> class SyncClassExample:
        >>>     def sync_method(self, sec):
        >>>         time.sleep(sec)  # Definitely not async.
        >>>         return sec
        >>>
        >>> obj = AsyncMultithreadWrapper(SyncClassExample())
        >>> await asyncio.gather(*[obj.sync_method(1) for _ in range(10)])
        ...
    """

    def __init__(
        self,
        wrapped: T,
        pool_size: int = 10,
        loop: typing.Optional[asyncio.events.AbstractEventLoop] = None
    ): ...


def get_task_traceback(task: asyncio.Task) -> typing.Optional[str]:
    """Get traceback for given task as string.
    Return traceback as string if exists. Or None if there was no error.
    """
    ...
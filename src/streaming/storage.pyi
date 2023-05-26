__all__ = [
    'BaseStorage',
    'JSONLocalStorage',
    'S3Storage',
]
import toloka.streaming.locker
import typing
import typing_extensions


Pickleable = typing.TypeVar('Pickleable')

class BaseStorage:
    def lock(self, key: str) -> typing.ContextManager[typing.Any]: ...

    def save(
        self,
        base_key: str,
        data: typing.Dict[str, Pickleable]
    ) -> None: ...

    def load(
        self,
        base_key: str,
        keys: typing.Sequence[str]
    ) -> typing.Optional[typing.Dict[str, Pickleable]]: ...

    def cleanup(
        self,
        base_key: str,
        keys: typing.Sequence[str],
        lock: typing.Any
    ) -> None: ...


class BaseExternalLockerStorage(BaseStorage):
    def lock(self, key: str) -> typing.ContextManager[typing.Any]: ...

    def cleanup(
        self,
        base_key: str,
        keys: typing.Sequence[str],
        lock: typing.Any
    ) -> None: ...

    def __init__(self, *, locker: typing.Optional[toloka.streaming.locker.BaseLocker] = None) -> None:
        """Method generated by attrs for class BaseExternalLockerStorage.
        """
        ...

    locker: typing.Optional[toloka.streaming.locker.BaseLocker]


class JSONLocalStorage(BaseExternalLockerStorage):
    """Simplest local storage to dump state of a pipeline and restore in case of restart.

    Attributes:
        dirname: Directory to store pipeline's state files. By default, "/tmp".
        locker: Optional locker object. By default, FileLocker with the same dirname is used.

    Example:
        Allow pipeline to dump it's state to the local storage.

        >>> pipeline = Pipeline(storage=JSONLocalStorage())
        >>> ...
        >>> await pipeline.run()  # Will load from storage at the start and save after each iteration.
        ...

        Set locker explicitly.

        >>> storage = JSONLocalStorage('/store-data-here', locker=FileLocker('/store-locks-here'))
        ...
    """

    class DefaultNearbyFileLocker(toloka.streaming.locker.BaseLocker):
        ...

    def __attrs_post_init__(self) -> None: ...

    def save(
        self,
        base_key: str,
        data: typing.Dict[str, Pickleable]
    ) -> None: ...

    def load(
        self,
        base_key: str,
        keys: typing.Sequence[str]
    ) -> typing.Optional[typing.Dict[str, Pickleable]]: ...

    def cleanup(
        self,
        base_key: str,
        keys: typing.Sequence[str],
        lock: typing.Any
    ) -> None: ...

    def __init__(
        self,
        dirname: str = '/tmp',
        *,
        locker: typing.Optional[toloka.streaming.locker.BaseLocker] = ...
    ) -> None:
        """Method generated by attrs for class JSONLocalStorage.
        """
        ...

    locker: typing.Optional[toloka.streaming.locker.BaseLocker]
    dirname: str


class ObjectSummaryCollection(typing_extensions.Protocol):
    def filter(
        self,
        Prefix,
        **kwargs
    ) -> 'ObjectSummaryCollection': ...

    def delete(self, **kwargs): ...

    def __init__(
        self,
        *args,
        **kwargs
    ): ...


class BucketType(typing_extensions.Protocol):
    def upload_fileobj(
        self,
        Fileobj,
        Key,
        ExtraArgs=None,
        **kwargs
    ): ...

    def download_fileobj(
        self,
        Fileobj,
        ExtraArgs=None,
        **kwargs
    ): ...

    def __init__(
        self,
        *args,
        **kwargs
    ): ...

    objects: ObjectSummaryCollection


class S3Storage(BaseExternalLockerStorage):
    """Storage that save to AWS S3 using given boto3 client.

    {% note warning %}

    Requires toloka-kit[s3] extras. Install it with the following command:

    ```shell
    pip install toloka-kit[s3]
    ```

    {% endnote %}

    Attributes:
        bucket: Boto3 bucket object.
        locker: Optional locker object. By default, no locker is used.

    Examples:
        Create new instance.

        >>> !pip install toloka-kit[s3]
        >>> import boto3
        >>> import os
        >>> session = boto3.Session(
        ...     aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        ...     aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        ... )
        >>> resource = session.resource('s3', region_name=os.getenv('AWS_DEFAULT_REGION', 'us-east-2'))
        >>> bucket = resource.Bucket('my-bucket')
        >>> storage = S3Storage(bucket)
        ...

        Use with pipelines.

        >>> storage = S3Storage(bucket=bucket, locker=ZooKeeperLocker(kazoo_client, '/lock-dir'))
        >>> pipeline = Pipeline(storage=storage)
        >>> ...
        >>> await pipeline.run()  # Will load from storage at the start and save after each iteration.
        ...
    """

    def save(
        self,
        base_key: str,
        data: typing.Dict[str, Pickleable]
    ) -> None: ...

    def load(
        self,
        base_key: str,
        keys: typing.Sequence[str]
    ) -> typing.Dict[str, Pickleable]: ...

    def cleanup(
        self,
        base_key: str,
        keys: typing.Sequence[str],
        lock: typing.Any
    ) -> None: ...

    def __init__(
        self,
        bucket: BucketType,
        *,
        locker: typing.Optional[toloka.streaming.locker.BaseLocker] = None
    ) -> None:
        """Method generated by attrs for class S3Storage.
        """
        ...

    locker: typing.Optional[toloka.streaming.locker.BaseLocker]
    bucket: BucketType

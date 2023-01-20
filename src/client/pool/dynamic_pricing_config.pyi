__all__ = [
    'DynamicPricingConfig',
]
import toloka.client.primitives.base
import toloka.util._extendable_enum
import typing


class DynamicPricingConfig(toloka.client.primitives.base.BaseTolokaObject):
    """The dynamic pricing settings.

    A price per task suite can be variable depending on a Toloker's skill.
    If a Toloker is not covered by dynamic pricing settings then the default price is used. It is set in the `reward_per_assignment` pool parameter.

    Attributes:
        type: The dynamic pricing type. Only `SKILL` type is supported now.
        skill_id: The ID of the skill that dynamic pricing is based on.
        intervals: A list of skill intervals and prices.
            The intervals must not overlap.
    """

    class Type(toloka.util._extendable_enum.ExtendableStrEnum):
        """Dynamic pricing type.
        """

        SKILL = 'SKILL'

    class Interval(toloka.client.primitives.base.BaseTolokaObject):
        """Skill level interval with the associated price per task suite.

        The lower and upper skill bounds are included in the interval.

        Attributes:
            from_: The lower bound of the interval.
            to: The upper bound of the interval.
            reward_per_assignment: The price per task suite for a Toloker with the specified skill level.
        """

        def __init__(
            self,
            *,
            from_: typing.Optional[int] = None,
            to: typing.Optional[int] = None,
            reward_per_assignment: typing.Optional[float] = None
        ) -> None:
            """Method generated by attrs for class DynamicPricingConfig.Interval.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        from_: typing.Optional[int]
        to: typing.Optional[int]
        reward_per_assignment: typing.Optional[float]

    def __init__(
        self,
        type: typing.Union[Type, str, None] = None,
        skill_id: typing.Optional[str] = None,
        intervals: typing.Optional[typing.List[Interval]] = None
    ) -> None:
        """Method generated by attrs for class DynamicPricingConfig.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    type: typing.Optional[Type]
    skill_id: typing.Optional[str]
    intervals: typing.Optional[typing.List[Interval]]

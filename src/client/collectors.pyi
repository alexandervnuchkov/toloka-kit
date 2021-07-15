from enum import Enum
from toloka.client.conditions import RuleCondition
from toloka.client.util._codegen import BaseParameters
from typing import (
    Any,
    Dict,
    List,
    Optional,
    overload
)
from uuid import UUID

class CollectorConfig(BaseParameters):
    """Base class for all collectors

    Attriutes:
        uuid: Id for this collector. Pay attention! If you clone the pool, you will have same collector in old and new pools.
            So collectors can behave a little unexpectedly. For example they start gather "history_size" patameter
            from both pools.
    """

    class Type(Enum):
        """An enumeration.
        """

        GOLDEN_SET = 'GOLDEN_SET'
        MAJORITY_VOTE = 'MAJORITY_VOTE'
        CAPTCHA = 'CAPTCHA'
        INCOME = 'INCOME'
        SKIPPED_IN_ROW_ASSIGNMENTS = 'SKIPPED_IN_ROW_ASSIGNMENTS'
        ANSWER_COUNT = 'ANSWER_COUNT'
        ASSIGNMENT_SUBMIT_TIME = 'ASSIGNMENT_SUBMIT_TIME'
        ACCEPTANCE_RATE = 'ACCEPTANCE_RATE'
        ASSIGNMENTS_ASSESSMENT = 'ASSIGNMENTS_ASSESSMENT'
        USERS_ASSESSMENT = 'USERS_ASSESSMENT'
        TRAINING = 'TRAINING'

    @overload
    def __init__(self, *, uuid: Optional[UUID] = None) -> None:
        """Method generated by attrs for class CollectorConfig.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        parameters: Optional[BaseParameters.Parameters] = None,
        uuid: Optional[UUID] = None
    ) -> None:
        """Method generated by attrs for class CollectorConfig.
        """
        ...

    def validate_condition(self, conditions: List[RuleCondition]): ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[BaseParameters.Parameters]
    uuid: Optional[UUID]


class AcceptanceRate(CollectorConfig):
    """Results of checking the answers of the performer

    If non-automatic acceptance (assignment review) is set in the pool, add a rule to:
    - Set the performer's skill based on their responses.
    - Block access for performers who give incorrect responses.

    Used with conditions:
    * TotalAssignmentsCount - How many assignments from this performer were checked.
    * AcceptedAssignmentsRate - Percentage of how many assignments were accepted from this performer out of all checked assignment.
    * RejectedAssignmentsRate - Percentage of how many assignments were rejected from this performer out of all checked assignment.

    Used with actions:
    * RestrictionV2 - Block access to projects or pools.
    * ApproveAllAssignments - Approve all replies from the performer.
    * RejectAllAssignments - Reject all replies from the performer.
    * SetSkill - Set perfmer skill value.
    * SetSkillFromOutputField - Set performer skill value from source.

    Example:
        How to ban a performer in this project if he makes mistakes.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>> collector=toloka.collectors.AcceptanceRate(),
        >>>     conditions=[
        >>>         toloka.conditions.TotalAssignmentsCount > 2,
        >>>         toloka.conditions.RejectedAssignmentsRate > 35,
        >>>     ],
        >>>     action=toloka.actions.RestrictionV2(
        >>>         scope=toloka.user_restriction.UserRestriction.PROJECT,
        >>>         duration=15,
        >>>         duration_unit='DAYS',
        >>>         private_comment='Performer often make mistakes',
        >>>     )
        >>> )
        ...
    """

    @overload
    def __init__(self, *, uuid: Optional[UUID] = None) -> None:
        """Method generated by attrs for class AcceptanceRate.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        parameters: Optional[BaseParameters.Parameters] = None,
        uuid: Optional[UUID] = None
    ) -> None:
        """Method generated by attrs for class AcceptanceRate.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[BaseParameters.Parameters]
    uuid: Optional[UUID]


class AnswerCount(CollectorConfig):
    """How many assignment was accepted from performer

    Use this rule if you want to:
    - Get responses from as many performers as possible (for this purpose, set a low threshold, such as one task suite).
    - Protect yourself from robots (for this purpose, the threshold should be higher, such as 10% of the pool's tasks).
    - Mark performers completing a task so that you can filter them later in the checking project.

    Used with conditions:
    * AssignmentsAcceptedCount - How many assignment was accepted from performer

    Used with actions:
    * RestrictionV2 - Block access to projects or pools.
    * ApproveAllAssignments - Approve all replies from the performer.
    * RejectAllAssignments - Reject all replies from the performer.
    * SetSkill - Set perfmer skill value.

    Example:
        How to mark performers completing a task so that you can filter them later in the checking project.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AnswerCount(),
        >>>     conditions=[toloka.conditions.AssignmentsAcceptedCount > 0],
        >>>     action=toloka.actions.SetSkill(skill_id=some_skill_id, skill_value=1),
        >>> )
        ...
    """

    @overload
    def __init__(self, *, uuid: Optional[UUID] = None) -> None:
        """Method generated by attrs for class AnswerCount.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        parameters: Optional[BaseParameters.Parameters] = None,
        uuid: Optional[UUID] = None
    ) -> None:
        """Method generated by attrs for class AnswerCount.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[BaseParameters.Parameters]
    uuid: Optional[UUID]


class AssignmentsAssessment(CollectorConfig):
    """Processing rejected and accepted assignments

    This rule is helpful when you need to:
    - Resend rejected assignments for re-completion to other performers. If you rejected an assignment, you may want it
    to be completed by another performer instead of the one whose response you rejected. To do this, you can increase
    the overlap for this assignment only. This is especially helpful if you have the overlap value set to 1.
    - Save money on re-completing assignments that you have already accepted. If you reviewed and accepted an assignment,
    it may not make sense for other users to complete the same assignment. To avoid this, you can reduce the overlap for
    accepted assignments only.

    Used with conditions:
    * PendingAssignmentsCount - Number of Assignments pending checking.
    * AcceptedAssignmentsCount - How many times this assignment was accepted.
    * RejectedAssignmentsCount - How many times this assignment was rejected.
    * AssessmentEvent - Assessment of the assignment changes its status to the specified one.

    Used with actions:
    * ChangeOverlap - Increase the overlap of the set of tasks.

    Example:
        How to resend rejected assignments for re-completion to other performers.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AssignmentsAssessment(),
        >>>     conditions=[toloka.conditions.AssessmentEvent == toloka.conditions.AssessmentEvent.REJECT],
        >>>     action=toloka.actions.ChangeOverlap(delta=1, open_pool=True),
        >>> )
        ...
    """

    @overload
    def __init__(self, *, uuid: Optional[UUID] = None) -> None:
        """Method generated by attrs for class AssignmentsAssessment.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        parameters: Optional[BaseParameters.Parameters] = None,
        uuid: Optional[UUID] = None
    ) -> None:
        """Method generated by attrs for class AssignmentsAssessment.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[BaseParameters.Parameters]
    uuid: Optional[UUID]


class AssignmentSubmitTime(CollectorConfig):
    """Filtering cheating performers who respond too quickly

    Helpful when you need to:
    - Use this Restrict the pool access for performers who respond too quickly.
    - Provide protection from robots.

    Used with conditions:
    * TotalSubmittedCount - The number of assignments a specific performer completed.
    * FastSubmittedCount - The number of assignments a specific performer completed too fast.

    Used with actions:
    * RestrictionV2 - Block access to projects or pools.
    * ApproveAllAssignments - Approve all replies from the performer.
    * RejectAllAssignments - Reject all replies from the performer.
    * SetSkill - Set perfmer skill value.

    Attributes:
        parameters.fast_submit_threshold_seconds: The task suite completion time (in seconds).
            Everything that is completed faster is considered a fast response.
        parameters.history_size: The number of the recent task suites completed by the performer.

    Example:
        How to reject all assignments if performer sends answers too fast.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AssignmentSubmitTime(history_size=5, fast_submit_threshold_seconds=20),
        >>>     conditions=[toloka.conditions.FastSubmittedCount > 3],
        >>>     action=toloka.actions.RejectAllAssignments(public_comment='Too fast answering. You are cheater!')
        >>> )
        ...
    """

    class Parameters(BaseParameters.Parameters):
        def __init__(
            self,
            *,
            fast_submit_threshold_seconds: Optional[int] = None,
            history_size: Optional[int] = None
        ) -> None:
            """Method generated by attrs for class AssignmentSubmitTime.Parameters.
            """
            ...

        _unexpected: Optional[Dict[str, Any]]
        fast_submit_threshold_seconds: Optional[int]
        history_size: Optional[int]

    @overload
    def __init__(
        self,
        *,
        uuid: Optional[UUID] = None,
        fast_submit_threshold_seconds: Optional[int] = None,
        history_size: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class AssignmentSubmitTime.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        uuid: Optional[UUID] = None,
        parameters: Optional[Parameters] = None
    ) -> None:
        """Method generated by attrs for class AssignmentSubmitTime.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[Parameters]
    uuid: Optional[UUID]


class Captcha(CollectorConfig):
    """Captchas provide a high level of protection from robots

    Used with conditions:
    * StoredResultsCount - How many times the performer entered captcha.
    * SuccessRate - Percentage of correct answers of the performer to the captcha.
    * FailRate - Percentage of wrong answers of the performer to the captcha.

    Used with actions:
    * RestrictionV2 - Block access to projects or pools.
    * ApproveAllAssignments - Approve all replies from the performer.
    * RejectAllAssignments - Reject all replies from the performer.
    * SetSkill - Set perfmer skill value.
    * SetSkillFromOutputField - Set performer skill value from source.

    Attributes:
        parameters.history_size: The number of times the performer was shown a captcha recently.

    Example:
        How to ban a performer in this project if he mistakes in captcha.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.set_captcha_frequency('MEDIUM')
        >>> new_pool.quality_control.add_action(
        >>> collector=toloka.collectors.Captcha(history_size=5),
        >>>     conditions=[
        >>>         toloka.conditions.SuccessRate < 60,
        >>>     ],
        >>>     action=toloka.actions.RestrictionV2(
        >>>         scope=toloka.user_restriction.UserRestriction.PROJECT,
        >>>         duration=15,
        >>>         duration_unit='DAYS',
        >>>         private_comment='Performer often make mistakes in captcha',
        >>>     )
        >>> )
        ...
    """

    class Parameters(BaseParameters.Parameters):
        def __init__(self, *, history_size: Optional[int] = None) -> None:
            """Method generated by attrs for class Captcha.Parameters.
            """
            ...

        _unexpected: Optional[Dict[str, Any]]
        history_size: Optional[int]

    @overload
    def __init__(
        self,
        *,
        uuid: Optional[UUID] = None,
        history_size: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class Captcha.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        uuid: Optional[UUID] = None,
        parameters: Optional[Parameters] = None
    ) -> None:
        """Method generated by attrs for class Captcha.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[Parameters]
    uuid: Optional[UUID]


class GoldenSet(CollectorConfig):
    """How performer answers on control tasks

    Use control tasks to assign a skill to performers based on their responses and ban performers who submit incorrect responses.

    Don't use it if:
    - You have a lot of response options.
    - Users need to attach a file to their assignment.
    - Users need to transcribe text.
    - Users need to select objects in a photo.
    - Tasks don't have a correct or incorrect response. For example: "Which image do you like best?" or
    "Choose the page design option that you like best".

    Used with conditions:
    * TotalAnswersCount - The number of completed control and training tasks.
    * CorrectAnswersRate - The percentage of correct responses in training and control tasks.
    * IncorrectAnswersRate - The percentage of incorrect responses in training and control tasks.
    * GoldenSetAnswersCount - The number of completed control tasks
    * GoldenSetCorrectAnswersRate - The percentage of correct responses in control tasks.
    * GoldenSetIncorrectAnswersRate - The percentage of incorrect responses in control tasks.

    Used with actions:
    * RestrictionV2 - Block access to projects or pools.
    * ApproveAllAssignments - Approve all replies from the performer.
    * RejectAllAssignments - Reject all replies from the performer.
    * SetSkill - Set perfmer skill value.
    * SetSkillFromOutputField - Set performer skill value from source.

    Attributes:
        parameters.history_size: The number of the performer's last responses to control tasks.

    Example:
        How to approve all assignments if performer doing well with golden tasks.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.GoldenSet(history_size=5),
        >>>     conditions=[toloka.conditions.GoldenSetCorrectAnswersRate > 90],
        >>>     action=toloka.actions.ApproveAllAssignments()
        >>> )
        ...
    """

    class Parameters(BaseParameters.Parameters):
        def __init__(self, *, history_size: Optional[int] = None) -> None:
            """Method generated by attrs for class GoldenSet.Parameters.
            """
            ...

        _unexpected: Optional[Dict[str, Any]]
        history_size: Optional[int]

    @overload
    def __init__(
        self,
        *,
        uuid: Optional[UUID] = None,
        history_size: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class GoldenSet.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        uuid: Optional[UUID] = None,
        parameters: Optional[Parameters] = None
    ) -> None:
        """Method generated by attrs for class GoldenSet.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[Parameters]
    uuid: Optional[UUID]


class Income(CollectorConfig):
    """Limit the performer's daily earnings in the pool

    Helpful when you need to:
    - Get responses from as many performers as possible.

    Used with conditions:
    * IncomeSumForLast24Hours - The performer earnings for completed tasks in the pool over the last 24 hours.

    Used with actions:
    * RestrictionV2 - Block access to projects or pools.
    * ApproveAllAssignments - Approve all replies from the performer.
    * RejectAllAssignments - Reject all replies from the performer.
    * SetSkill - Set perfmer skill value.

    Example:
        How to ban a performer in this project if he made enough answers.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.Income(),
        >>>     conditions=[toloka.conditions.IncomeSumForLast24Hours > 1],
        >>>     action=toloka.actions.RestrictionV2(
        >>>         scope=toloka.user_restriction.UserRestriction.PROJECT,
        >>>         duration=15,
        >>>         duration_unit='DAYS',
        >>>         private_comment='No need more answers from this performer',
        >>>     )
        >>> )
        ...
    """

    @overload
    def __init__(self, *, uuid: Optional[UUID] = None) -> None:
        """Method generated by attrs for class Income.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        parameters: Optional[BaseParameters.Parameters] = None,
        uuid: Optional[UUID] = None
    ) -> None:
        """Method generated by attrs for class Income.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[BaseParameters.Parameters]
    uuid: Optional[UUID]


class MajorityVote(CollectorConfig):
    """Majority vote is a quality control method based on coinciding responses from the majority

    The response chosen by the majority is considered correct, and other responses are considered incorrect.
    Depending on the percentage of correct responses, you can either increase the user's skill value, or ban the user from tasks.

    Used with conditions:
    * TotalAnswersCount - The number of completed tasks by the performer.
    * CorrectAnswersRate - The percentage of correct responses.
    * IncorrectAnswersRate - The percentage of incorrect responses.

    Used with actions:
    * RestrictionV2 - Block access to projects or pools.
    * ApproveAllAssignments - Approve all replies from the performer.
    * RejectAllAssignments - Reject all replies from the performer.
    * SetSkill - Set perfmer skill value.
    * SetSkillFromOutputField - Set performer skill value from source.

    Attributes:
        parameters.answer_threshold: The number of users considered the majority (for example, 3 out of 5).
        parameters.history_size: The maximum number of the user's recent responses in the project to use for calculating
            the percentage of correct responses. If this field is omitted, the calculation is based on all the user's
            responses in the pool.

    Example:
        How to ban a performer in this project if he made enough answers.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.MajorityVote(answer_threshold=2),
        >>>     conditions=[
        >>>         toloka.conditions.TotalAnswersCount > 9,
        >>>         toloka.conditions.CorrectAnswersRate < 60,
        >>>     ],
        >>>     action=toloka.actions.RejectAllAssignments(public_comment='Too low quality')
        >>> )
        ...
    """

    class Parameters(BaseParameters.Parameters):
        def __init__(
            self,
            *,
            answer_threshold: Optional[int] = None,
            history_size: Optional[int] = None
        ) -> None:
            """Method generated by attrs for class MajorityVote.Parameters.
            """
            ...

        _unexpected: Optional[Dict[str, Any]]
        answer_threshold: Optional[int]
        history_size: Optional[int]

    @overload
    def __init__(
        self,
        *,
        uuid: Optional[UUID] = None,
        answer_threshold: Optional[int] = None,
        history_size: Optional[int] = None
    ) -> None:
        """Method generated by attrs for class MajorityVote.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        uuid: Optional[UUID] = None,
        parameters: Optional[Parameters] = None
    ) -> None:
        """Method generated by attrs for class MajorityVote.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[Parameters]
    uuid: Optional[UUID]


class SkippedInRowAssignments(CollectorConfig):
    """Skipping tasks is considered an indirect indicator of the quality of responses.

    You can block access to a pool or project if a user skips multiple task suites in a row.

    Used with conditions:
    * SkippedInRowCount - How many tasks in a row the performer skipped.

    Used with actions:
    * RestrictionV2 - Block access to projects or pools.
    * ApproveAllAssignments - Approve all replies from the performer.
    * RejectAllAssignments - Reject all replies from the performer.
    * SetSkill - Set perfmer skill value.

    Example:
        How to ban a performer in this project if he skipped tasks.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.SkippedInRowAssignments(),
        >>>     conditions=[toloka.conditions.SkippedInRowCount > 3],
        >>>     action=toloka.actions.RestrictionV2(
        >>>         scope=toloka.user_restriction.UserRestriction.PROJECT,
        >>>         duration=15,
        >>>         duration_unit='DAYS',
        >>>         private_comment='Lazy performer',
        >>>     )
        >>> )
        ...
    """

    @overload
    def __init__(self, *, uuid: Optional[UUID] = None) -> None:
        """Method generated by attrs for class SkippedInRowAssignments.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        parameters: Optional[BaseParameters.Parameters] = None,
        uuid: Optional[UUID] = None
    ) -> None:
        """Method generated by attrs for class SkippedInRowAssignments.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[BaseParameters.Parameters]
    uuid: Optional[UUID]


class Training(CollectorConfig):
    @overload
    def __init__(self, *, uuid: Optional[UUID] = None) -> None:
        """Method generated by attrs for class Training.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        parameters: Optional[BaseParameters.Parameters] = None,
        uuid: Optional[UUID] = None
    ) -> None:
        """Method generated by attrs for class Training.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[BaseParameters.Parameters]
    uuid: Optional[UUID]


class UsersAssessment(CollectorConfig):
    """Recompletion of assignments from banned users

    If you or the system banned a performer and you want someone else to complete their tasks.
    This rule will help you do this automatically.

    Used with conditions:
    * PoolAccessRevokedReason - Reason for loss of access of the performer to the current pool.
    * SkillId - The performer no longer meets the specific skill filter.

    Used with actions:
    * ChangeOverlap - Increase the overlap of the set of tasks.

    Example:
        How to resend rejected assignments for re-completion to other performers.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.UsersAssessment(),
        >>>     conditions=[toloka.conditions.PoolAccessRevokedReason == toloka.conditions.PoolAccessRevokedReason.RESTRICTION],
        >>>     action=toloka.actions.ChangeOverlap(delta=1, open_pool=True),
        >>> )
        ...
    """

    @overload
    def __init__(self, *, uuid: Optional[UUID] = None) -> None:
        """Method generated by attrs for class UsersAssessment.
        """
        ...

    @overload
    def __init__(
        self,
        *,
        parameters: Optional[BaseParameters.Parameters] = None,
        uuid: Optional[UUID] = None
    ) -> None:
        """Method generated by attrs for class UsersAssessment.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    parameters: Optional[BaseParameters.Parameters]
    uuid: Optional[UUID]

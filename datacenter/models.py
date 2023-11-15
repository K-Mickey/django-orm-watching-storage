from django.db import models
from django.utils.timezone import localtime, timedelta


SEC_IN_MINUTE = 60
SEC_IN_HOUR = 3600


def format_duration(duration: float) -> str:
    dur_in_hours = duration // SEC_IN_HOUR
    dur_in_minutes = (duration % SEC_IN_HOUR) // SEC_IN_MINUTE
    dur_in_seconds = duration % SEC_IN_MINUTE
    return f"{dur_in_hours:02.0f}:{dur_in_minutes:02.0f}:{dur_in_seconds:02.0f}"


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self) -> float:
        time_leave = self.leaved_at
        if not time_leave:
            time_leave = localtime()

        return (time_leave - self.entered_at).total_seconds()

    def is_visit_long(self, minutes: int = 60) -> bool:
        duration = self.get_duration()
        dur_in_minutes = duration // SEC_IN_MINUTE
        return dur_in_minutes >= minutes

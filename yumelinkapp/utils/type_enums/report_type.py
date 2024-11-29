from enum import Enum


class ReportType(Enum):
    content = "Content filter violation"
    hate = "Hate speech"
    inappropriate_content = 'Inappropriate Content'
    violence = 'Violence'
    cyberbully = "Cyberbullying"
    fake_user = "Identity impersonation"
    fake = "Fake news"
    child_exploitation = 'Child Exploitation'
    scam_fraud = 'Scam or Fraud'
    other = "Other"

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        """Returns the choices as a list of tuples."""
        return [(status.name, status.value) for status in cls]

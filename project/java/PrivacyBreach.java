package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class for a recorded incident in which PII was processed in a manner that violates applicable privacy safeguarding requirements. Tracks breach details, affected PII categories, notification obligations, remediation actions, and lessons learned.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PrivacyBreach extends NamedEntity {

  private ZonedDateTime breachDatetime;
  private ZonedDateTime discoveryDatetime;
  private String breachDescription;
  private List<String> affectedPiiCategories;
  private String affectedPrincipalsCount;
  private List<PrivacySafeguardingRequirement> violatedRequirements;
  private String breachSeverity;
  private List<String> immediateActions;
  private boolean notificationRequired;
  private List<String> notificationsMade;
  private List<String> remediationActions;
  private String lessonsLearned;
  private ZonedDateTime closureDatetime;

}
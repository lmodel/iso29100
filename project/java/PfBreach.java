package example;

/* metamodel_version: 1.12.0 */
/* version: 2024 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A time when PII was handled against a safeguarding requirement: what happened, who was told and what was done.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfBreach  {

  private List<PfPiiItem> pfConcernedPii;
  private ZonedDateTime pfBreachOccurred;
  private ZonedDateTime pfBreachDiscovered;
  private ZonedDateTime pfBreachClosed;
  private Integer pfPrincipalsAffected;
  private List<PfSafeguardingRequirement> pfBreachedRequirements;
  private String pfBreachSeverity;
  private List<String> pfImmediateActions;
  private Boolean pfNotificationRequired;
  private List<String> pfNotifications;
  private List<String> pfRemediation;
  private String pfLessons;
  private URI pfId;
  private String title;
  private String description;


}
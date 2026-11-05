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
  One person's agreement to the processing of their PII for stated purposes, and where it stands.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfConsent  {

  private List<String> pfPurposes;
  private List<PfPiiItem> pfConcernedPii;
  private List<String> pfEvidence;
  private PfPiiPrincipal pfPrincipal;
  private String pfConsentMechanism;
  private ZonedDateTime pfConsentGiven;
  private String pfConsentState;
  private ZonedDateTime pfConsentWithdrawn;
  private URI pfId;
  private String title;
  private String description;


}
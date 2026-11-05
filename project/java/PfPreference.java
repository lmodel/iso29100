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
  What one person has said they want done, or not done, with their PII.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfPreference  {

  private PfPiiPrincipal pfPrincipal;
  private String pfPreferenceScope;
  private Boolean pfWantsAnonymity;
  private Boolean pfWantsPseudonymity;
  private List<String> pfRefusedOperations;
  private List<String> pfRefusedRecipients;
  private LocalDate pfPreferenceRecorded;
  private URI pfId;
  private String title;
  private String description;


}
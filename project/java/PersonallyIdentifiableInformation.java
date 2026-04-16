package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class representing a data element or attribute set that can be linked back to a natural person — either directly or through combination with other attributes. Captures sensitivity classification, identifier type, pseudonymization status, retention schedule, and processing operations applicable to the data.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PersonallyIdentifiableInformation extends NamedEntity {

  private List<String> piiCategory;
  private String sensitivityLevel;
  private String identifierType;
  private boolean isPseudonymized;
  private boolean isAnonymized;
  private String linkabilityRisk;
  private String applicableToPrincipal;
  private String retentionSchedule;
  private List<String> processingOperations;

}
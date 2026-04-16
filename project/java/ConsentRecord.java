package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class documenting a PII principal's agreement to processing of their PII for stated purposes. Records the consent mechanism used, scope, current status, and withdrawal date — supporting auditability of the consent and choice privacy principle.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ConsentRecord extends NamedEntity {

  private String principalRef;
  private ZonedDateTime consentDate;
  private String consentMechanism;
  private List<String> processingPurposesConsented;
  private List<String> piiCategoriesConsented;
  private ZonedDateTime withdrawalDate;
  private String consentStatus;
  private String consentEvidenceRef;

}
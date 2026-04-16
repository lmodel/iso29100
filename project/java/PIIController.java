package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class for an organization or individual that determines why and how PII is processed. Captures appointed processors, legal bases relied upon, privacy policy reference, and data protection officer details. Bears ultimate accountability for privacy principle adherence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PIIController extends PrivacyStakeholder {

  private List<String> processingPurposes;
  private List<String> legalBases;
  private List<PIIProcessor> appointedProcessors;
  private PrivacyPolicy privacyPolicyRef;
  private String dataProtectionOfficer;

}